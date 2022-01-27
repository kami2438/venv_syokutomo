from http.client import HTTPResponse
from pyexpat import model
from re import template
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.postgres import fields
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.contrib import messages

from django.views import generic
from django.shortcuts import render,redirect
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
        return informations


class TermsView(generic.TemplateView):
    template_name = "user_terms.html"


class ListView(LoginRequiredMixin, generic.ListView):
    model = T1_shop
    template_name = 'user_shop_list.html'

    def get_queryset(self):
        # print(user)
        informations = T1_shop.objects.filter(
            user__area=self.request.user.area)
        # print(informations)
        # print(type(informations))
        # l=[]
        # for i in informations:
        #     print(i.user.area)
        #     if(i.user.area ==self.request.user.area):
        #         [i.user]+=l
        return informations


class user_informationView(LoginRequiredMixin, generic.DetailView):
    model = T5_user
    template_name = "user_information.html"


class user_updateView(LoginRequiredMixin, generic.UpdateView):
    model = T5_user
    template_name = 'user_update.html'
    form_class = User_UpdateForm

    def get_success_url(self):
        return reverse_lazy('user:info', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "更新に失敗しました。")
        return super().form_invalid(form)


class ChargeView(LoginRequiredMixin, generic.CreateView):
    model = T12_charge
    form_class = Charge_form
    template_name = "user_charge.html"
    success_url = reverse_lazy('user:mypage')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["T5_user"] = T5_user.objects.filter(
            user=self.request.user)[0]
        return context

    def form_valid(self, form):
        charge = form.save(commit=False)
        charge.user = self.request.user
        charge.save
        print("1")
        chuser = T5_user.objects.filter(
            user=self.request.user)[0]
        amount = form.cleaned_data.get('t12_charge_amount')
        print(amount)
        n = int(amount)+int(chuser.t5_charge_remain)
        chuser.t5_charge_remain = n
        print("3")
        chuser.save()
        return super().form_valid(form)


class user_productView(LoginRequiredMixin, generic.DetailView):
    model = T1_shop
    template_name = "user_product.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["food"] = T4_food.objects.filter(
            t1_shop_id=self.kwargs['pk'])
        context["like"]=T11_love.objects.filter(user=self.request.user,t1_shop_id=self.kwargs['pk'])
        return context
    def loveaa(self,request):
        print("move")
        done=T11_love.objects.filter(user=self.request.user,t1_shop_id=self.kwargs['pk'])
        if request.method == 'GET':
            if 'like' in request.GET:
                print("ok")
                if done is None:
                    T11_love.objects.get_or_create(user=self.request.user,t1_shop_id=self.kwargs['pk'])
                    print("kk")
            if 'unlike' in request.GET:
                if done :
                    done.delete()
            print("save")
            return reverse_lazy('user:index')

    # def get(self, request, *args, **kwargs):
    #     """Handle GET requests: instantiate a blank version of the form."""
    #     return self.render_to_response(self.loveaa(request=request))
    

    # def get(self,request,*args,**kwargs):
    #     print("ssssssssss")

    #     return HTTPResponse("ffffffffff")



def love(self,request=request,pk):
    # print("move")
    # done=T11_love.objects.filter(user=self.request.user,t1_shop_id=self.kwargs['pk'])
    # if request.method == 'POST':
    #     if 'like' in request.POST:
    #         print("ok")
    #         if done is None:
    #             T11_love.objects.get_or_create(user=self.request.user,t1_shop_id=self.kwargs['pk'])
    #             print("kk")
    #     if 'unlike' in request.POST:
    #         if done :
    #             done.delete()
    #     print("save")
    #     return reverse_lazy('user:product', kwargs={'pk': self.kwargs['pk']})
    params = {'form' : LikeForm(),}
    print("")
    if (request.method == 'POST'):
        user=self.request.user
        id={'pk': self.kwargs['pk']}
        like = T11_love(user=user, t1_shop_id=id)
        like.save()
        return redirect(to = 'index')

    return render(request, 'user/index.html', params)


class ChargeHistoryView(generic.ListView, LoginRequiredMixin):
    model = T12_charge
    template_name = "user_charge_history.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["history"] = T12_charge.objects.filter(
            user=self.request.user)
        return context


class CreateOrderView(LoginRequiredMixin, generic.CreateView):
    model = T2_order
    template_name = "user_order.html"
    form_class = Orderform

    def get_success_url(self):
        return reverse_lazy('user:product', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        order = form.save(commit=False)
        shoppk = self.kwargs['pk']
        order.t1_shop_id = T1_shop.objects.filter(id=shoppk)[0]
        order.user = self.request.user
        order.save()
        messages.success(self.request, '注文が登録されました。')
        return super().form_valid(form)


class DeleteUserView(LoginRequiredMixin, generic.DeleteView):
    model = T5_user
    template_name = "delete_user.html"
    # success_url = reverse_lazy('user:index')

    def get_success_url(self):
        return reverse('prime:index')

    def delete(self, request, *args, **kwargs):

        user = self.request.user
        user.is_active=False
        user.save()
        return super().delete(request, *args, **kwargs)
    # def form_valid(self,form):
    #     user=self.request.user
    #     user.is_active= False
    #     user.save()
    #     return super().form_valid(form)


class FoodDetailView(LoginRequiredMixin, generic.DetailView):
    model = T4_food
    template_name = "user_food_detail.html"

# これオブジェクトallしたらそうなっちゃうんだー？ トムブラウン
# 烏賊
# class LikeView(LoginRequiredMixin, generic.ListView):
#     model=T11_love
#     template_name="user_like.html"
#     def get_queryset(self):
#         like=T11_love.objects.filter(user=self.request.user)
#         return like
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         likes= T11_love.objects.select_related('t1_shop_id').filter(user=self.request.user)
#         if likes.first():
#             sn_list=[]
#             for like in likes:
#                 sn_list.append(like.t1_shop_id)
#             print(sn_list)
#         context["shops"] = sn_list
#         return context

class LikeView(LoginRequiredMixin, generic.ListView):
    model=T11_love
    template_name="user_like.html"
    def get_queryset(self):
        likes= T11_love.objects.select_related('t1_shop_id').filter(user=self.request.user)
        if likes.first():
            sn_list=[]
            for like in likes:
                sn_list.append(like.t1_shop_id)
        return list(set(sn_list))
