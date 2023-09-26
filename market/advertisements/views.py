from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, FormView,
                                  ListView, UpdateView)

from .forms import AdvertForm
from .models import AdvertModel, ReplyModel


class AdvertList(ListView):
    model = AdvertModel
    paginate_by = 10


class AdvertDetail(DetailView):
    model = AdvertModel


class AdvertFormView(LoginRequiredMixin, FormView):
    model = AdvertModel
    form_class = AdvertForm


class AdvertCreate(CreateView, AdvertFormView):
    ...


class AdvertUpdate(UpdateView, AdvertFormView):
    ...


class AdvertDelete(LoginRequiredMixin, DeleteView):
    model = AdvertModel
    success_url = reverse_lazy('my')


class ReplyList(ListView):
    model = ReplyModel
    paginate_by = 10
