from re import template
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.postgres import fields
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import generic

from .models import *
from .forms import *

# Create your views here.


class IndexView(generic.TemplateView):
    template_name = "driver_index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        driver=T7_delivery_man.objects.filter(user=self.request.user)[0]
        orderdetail = T3_order_detail.objects.filter(t7_delivery_man_id=driver,t2_order_id__t2_order_deliver_status__lt=3)
        # order=T2_order.objects.filter()
        order=[]
        for i in orderdetail:
            order.append(i.t2_order_id)
        order=list(set(order))
        context['order'] = order

        return context

def Action(request,pk):
    print("oooo")
    if (request.method == 'POST'):
        print("eeee")
        user = request.user
        order = T2_order.objects.filter(id=pk)[0]
        # vex = T11_love.objects.filter(user=user, t1_shop_id=id)
        order.t2_order_deliver_status+=1
        if order.t2_order_deliver_status==2:
            order.t2_order_count-=1
        order.save()
        return redirect("driver:index")


class MypageView(LoginRequiredMixin, generic.ListView):
    template_name = "driver_mypage.html"
    model = T7_delivery_man
    pk_url_kwarg = "id"

    def get_queryset(self):
        informations = T7_delivery_man.objects.filter(user=self.request.user)
        return informations


class TermsView(generic.TemplateView):
    template_name = "driver_terms.html"


class StatusView(generic.TemplateView):
    template_name = "driver_status.html"


class driver_infoView(LoginRequiredMixin, generic.DetailView):
    model = T7_delivery_man
    template_name = "driver_info.html"


class driver_updateView(LoginRequiredMixin, generic.UpdateView):
    model = T7_delivery_man
    template_name = 'driver_update.html'
    form_class = driver_updateForm

    def get_success_url(self):
        return reverse_lazy('driver:info', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '?????????????????????')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "??????????????????????????????")
        return super().form_invalid(form)


class driver_scheduleView(LoginRequiredMixin, generic.ListView):
    model = T3_order_detail
    template_name = 'driver_schedule.html'


# class DeleteDriverView(LoginRequiredMixin, generic.DeleteView):
#     model = T7_delivery_man
#     template_name = "delete_user.html"
#     # success_url = reverse_lazy('user:index')

#     def get_success_url(self):
#         return reverse('prime:index')

#     def delete(self, request, *args, **kwargs):

#         user = self.request.user
#         user.is_active = False
#         user.save()
#         return super().delete(request, *args, **kwargs)
