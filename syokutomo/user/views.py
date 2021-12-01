from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.postgres import fields
from django.urls import reverse_lazy
from django.urls.base import reverse

from django.views import generic

from .models import *
from .forms import *

# Create your views here.


class IndexView(generic.TemplateView):
    template_name = "user_index.html"


class MypageView(generic.ListView, LoginRequiredMixin):
    template_name = "user_mypage.html"
    model = T5_user
    pk_url_kwarg = "id"

    def get_queryset(self):
        print('get')
        informations = T5_user.objects.filter(user=self.request.user)
        informations = informations
        print(type(self.request.user))
        print(type(informations))
        print("--------------------------------")
        print(vars(informations))
        return informations
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print(context)
    #     return context


class TermsView(generic.TemplateView):
    template_name = "user_terms.html"


class ListView(LoginRequiredMixin, generic.ListView):
    model = T1_shop
    template_name = 'user_shoplist.html'

    def get_queryset(self):
        users = T1_shop.object.filter(
            user=self.request.user).order_by('-created_at')
        return users


class user_informationView(LoginRequiredMixin, generic.DetailView):
    model = T5_user
    template_name = "user_information.html"
    pk_url_kwarg = "id"

    def get_queryset(self):
        informations = T5_user.objects.filter(user=self.request.user)
        return informations
