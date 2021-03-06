import logging

from django.urls import reverse_lazy

from django.views import generic

# from .forms import ReservationForm
from .forms import *

from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
# Create your views here.

logger = logging.getLogger(__name__)


class IndexView(generic.TemplateView):
    template_name = "index.html"


class Choice_loginView(generic.TemplateView):
    template_name = 'choice_login.html'


class TermsView(generic.TemplateView):
    template_name = "prime_terms.html"


class ReservationView(generic.FormView):
    template_name = "prime_reservation.html"
    form_class = ReservationForm
    success_url = reverse_lazy('prime:index')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)


class Regis_userViews(LoginRequiredMixin, generic.CreateView):
    template_name = 'regis_user.html'
    model = T5_user
    form_class = Regis_userForm
    success_url = reverse_lazy('user:index')


    def form_valid(self, form):
        # 新しい変数のuserは大文字表記
        User = form.save(commit=False)
        User.user = self.request.user
        User.save()
        messages.success(self.request, "本登録が完了しました")
        self.request.user.address=User.t5_address
        self.request.user.main_regist=True
        self.request.user.save()
        return super().form_valid(form)


class Regis_shopViews(LoginRequiredMixin,generic.FormView):
    template_name = 'regis_shop.html'
    form_class =Regis_shopForm
    model=T1_shop
    success_url=reverse_lazy('shop:index')
    def form_valid(self, form):
        shop=form.save(commit=False)
        shop.user=self.request.user
        shop.save()
        messages.success(self.request,"本登録が完了しました")
        self.request.user.main_regist=True
        self.request.user.save()
        return super().form_valid(form)

class Regis_driverViews(LoginRequiredMixin,generic.FormView):
    template_name = 'regis_driver.html'
    model=T7_delivery_man
    form_class =Regis_driverForm
    success_url=reverse_lazy('driver:index')
    def form_valid(self, form):
        driver=form.save(commit=False)
        driver.user=self.request.user
        driver.save()
        messages.success(self.request,"本登録が完了しました")
        self.request.user.main_regist=True
        self.request.user.save()
        return super().form_valid(form)

# class Food_tempListViews(LoginRequiredMixin,generic.ListView):
#     model=T4_food
#     template_name='temp_list.html'

#     def get_queryset(self,**kwargs):
#         #<input type="text" name="input_type_name" ...>  in search templates　
#         form_input=self.request.GET.get('input_type_name','')
#         t4_ingredients=T4_food.objects.filter(t4_ingredients__icontains=form_input)
#         return t4_ingredients