from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, FormView,
                                  ListView, UpdateView)

from .forms import AdvertForm
from .models import AdvertModel, ReplyModel, User
from django.shortcuts import get_object_or_404


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
        self.user = get_object_or_404(User, username=request.user.username)
        return super(AdvertCreate, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        advert = form.save(commit=False)
        advert.user = self.user
        return super().form_valid(form)


class AdvertUpdate(UpdateView, AdvertFormView):
    ...


class AdvertDelete(LoginRequiredMixin, DeleteView):
    model = AdvertModel
    success_url = reverse_lazy('my')


class ReplyList(ListView):
    model = ReplyModel
    paginate_by = 10
