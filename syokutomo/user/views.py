from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from django.views import generic

from .models import *
from .forms import *

# Create your views here.


class IndexView(generic.TemplateView):
    template_name = "user_index.html"


class MypageView(generic.TemplateView):
    template_name = "user_mypage.html"


class TermsView(generic.TemplateView):
    template_name = "user_terms.html"


class ListView(LoginRequiredMixin, generic.ListView):
    model = T1_shop
    template_name = 'user_shoplist.html'

    def get_queryset(self):
        users = T1_shop.object.filter(
            user=self.request.user).order_by('-created_at')
        return users


class user_informationView(LoginRequiredMixin, generic.UpdateView):
    model = T5_user
    template_name = "user_information.html"
    form_class =

    def get_queryset(self):
        informations = T5_user.objects.filter(user=self.request.user)
        return informations
