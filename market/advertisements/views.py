from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, FormView,
                                  ListView, UpdateView, View)
from django_filters.views import FilterView

from .filters import ReplyModelFilterSet
from .forms import AdvertForm, ReplyForm
from .models import AdvertModel, ReplyModel
from .signals import reply_is_accepted


class AdvertList(ListView):
    model = AdvertModel
    paginate_by = 10


class AdvertDetail(DetailView):
    model = AdvertModel


class AdvertFormView(LoginRequiredMixin, FormView):
    model = AdvertModel
    form_class = AdvertForm


class AdvertCreate(CreateView, AdvertFormView):
    def post(self, request, *args, **kwargs):
        self.user = request.user
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        advert = form.save(commit=False)
        advert.user = self.user
        return super().form_valid(form)


class AdvertUpdate(UpdateView, AdvertFormView):
    ...


class AdvertDelete(LoginRequiredMixin, DeleteView):
    model = AdvertModel
    success_url = reverse_lazy('my')


class ReplyFilter(LoginRequiredMixin, FilterView):
    model = ReplyModel
    filterset_class = ReplyModelFilterSet

    def get(self, request, *args, **kwargs):
        self.user = request.user
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = ReplyModel.objects.filter(advert__user=self.user)
        return queryset


class ReplyCreate(LoginRequiredMixin, CreateView):
    model = ReplyModel
    form_class = ReplyForm
    success_url = reverse_lazy('advert_list')

    def post(self, request, *args, **kwargs):
        self.user = request.user
        self.advert = get_object_or_404(AdvertModel, pk=kwargs['pk'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        reply = form.save(commit=False)
        reply.user = self.user
        reply.advert = self.advert
        return super().form_valid(form)


class ReplyDelete(LoginRequiredMixin, DeleteView):
    model = ReplyModel
    success_url = reverse_lazy('my')


class ReplyAccept(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        reply = get_object_or_404(ReplyModel, pk=kwargs['pk'])
        advert = reply.advert
        reply.is_accepted = True
        advert.has_accepted_reply = True
        reply.save()
        advert.save()
        reply_is_accepted.send_robust(sender=reply.pk, email=reply.user.email)
        return redirect('my')
