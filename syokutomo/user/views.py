from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.postgres import fields
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.contrib import messages

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
    template_name = 'user_shop_list.html'

#    def get_queryset(self):
 #       users = T1_shop.object.filter(
  #          user=self.request.user).order_by('-created_at')
   #     return users


class user_informationView(LoginRequiredMixin, generic.DetailView):
    model = T5_user
    template_name = "user_information.html"
    # pk_url_kwarg = "id"

    # def get_queryset(self):
    #     informations = T5_user.objects.filter(user=self.request.user)
    #     return informations

class user_updateView(LoginRequiredMixin, generic.UpdateView):
    model =T5_user
    template_name = 'user_update.html'
    form_class = User_UpdateForm

    def get_success_url(self):
        return reverse_lazy('user:info',kwargs={'pk':self.kwargs['pk']})

    def form_valid(self,form):
        messages.success(self.request,'更新しました。')
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.error(self.request,"更新に失敗しました。")
        return super().form_invalid(form)


class user_ChargeView(LoginRequiredMixin, generic.CreateView):
    model =T12_charge
    form_class=Charge_form
    template_name = "user_charge.html"
    success_url = reverse_lazy('user:mypage')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["T5_user"]=T5_user.objects.filter(
            user=self.request.user)[0]
        return context
    def form_valid(self, form):
        messages.success(self.request,'仮完了')
        chuser=T5_user.objects.filter(
            user=self.request.user)[0]
        charge=T12_charge.objects.all().order_by('t12_create_at')[0]
        messages.success(self.request,'zzzz')
        n=int(charge.t12_charge_amount)+int(chuser.t5_charge_remain)
        chuser.t5_charge_remain=n
        charge.t12_charge_remain_ex=n
        messages.success(self.request,'djffeijij')
        chuser.save()
        messages.success(self.request,'チャージされました。')
        return super().form_valid(form)
