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
    template_name = "shop_index.html"

class MypageView(generic.ListView):
    template_name = "shop_mypage.html"
    model = T1_shop
    pk_url_kwarg = "id"

    def get_queryset(self):
        informations = T1_shop.objects.filter(user=self.request.user)
        return informations

class TermsView(generic.TemplateView):
    template_name = "shop_terms_of_service.html"

#class MerchandiseView(LoginRequiredMixin, generic.MerchandiseView):
#    model = T1_shop
#    template_name = 'shop_merchandise.html'

#    def get_queryset(self):
#        users = T1_shop.object.filter(user=self.request.user).order_by('-created_at')
#        return users

class shop_infoView(LoginRequiredMixin, generic.ListView):
    model = T1_shop
    template_name = "shop_info.html"

class shop_updateView(LoginRequiredMixin, generic.UpdateView):
    model = T1_shop
    template_name = "shop_update.html"
    form_class = shop_updateForm

    def get_success_url(self):
        return reverse_lazy('shop:info',kwargs={'pk':self.kwargs['pk']})

    def form_valid(self,form):
        messages.success(self.request,'更新しました。')
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.error(self.request,"更新に失敗しました。")
        return super().form_invalid(form)