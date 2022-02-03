from http.client import HTTPResponse
from lib2to3.pgen2 import driver
from pyexpat import model
from re import template
from unicodedata import category
from urllib import request
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.postgres import fields
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.contrib import messages

from django.views import generic
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.db.models import Q

# Create your views here.


class IndexView(generic.TemplateView):
    template_name = "user_index.html"
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

    #     order = T2_order.objects.filter(user=self.request.user)
    #     context['order'] = order

    #     return context


class MypageView(generic.ListView, LoginRequiredMixin):
    template_name = "user_mypage.html"
    model = T5_user
    pk_url_kwarg = "id"

    def get_queryset(self):
        print('get')
        informations = T5_user.objects.filter(user=self.request.user)
        return informations


class TermsView(generic.TemplateView):
    template_name = "user_terms.html"


class ListView(LoginRequiredMixin, generic.ListView):
    model = T1_shop
    template_name = 'user_shop_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category = T8_shop_category.objects.all()
        context['category'] = category

        return context

    def get_queryset(self):
        # print(user)
        informations = T1_shop.objects.filter(
            user__area=self.request.user.area).order_by("t1_favorite_count").reverse()
        # GETのURLクエリパラメータを取得する
        # 該当のクエリパラメータが存在しない場合は、[]が返ってくる
        q_category = self.request.GET.getlist('category')
        q_name = self.request.GET.get('name')

        # if q_category is not None:

        #     informations = informations.filter(t8_shop_category_id=q_category)
        # print(q_category)
        if len(q_category) != 0:
            # print(q_category)
            # kinds = [x for x in q_category if x in ["1", "2"]]
            informations = informations.filter(
                t8_shop_category_id__id=q_category[0])

        if q_name is not None:
            informations = informations.filter(
                t1_shop_name_prime__icontains=q_name)

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
        context["like"] = T11_love.objects.filter(
            user=self.request.user, t1_shop_id=self.kwargs['pk'])
        print(context["like"])
        return context


def love(request, pk):
    params = {'form': LikeForm(), }
    print("")
    if (request.method == 'POST'):
        user = request.user
        id = T1_shop.objects.filter(id=pk)[0]
        vex = T11_love.objects.filter(user=user, t1_shop_id=id)
        if vex.first() is None:
            like = T11_love(user=user, t1_shop_id=id)
            like.save()
            shop = id
            shop.t1_favorite_count = int(shop.t1_favorite_count)+1
            shop.save
        else:
            vex.delete()
            shop = id
            shop.t1_favorite_count = int(shop.t1_favorite_count)-1
            shop.save

    return redirect("user:product", pk)


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
        user.is_active = False
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = T2_order.objects.filter(
            user=self.request.user, t2_order_count__gte=1)
        context['order'] = order
        return context


class LikeView(LoginRequiredMixin, generic.ListView):
    model = T11_love
    template_name = "user_like.html"

    def get_queryset(self):
        likes = T11_love.objects.select_related(
            't1_shop_id').filter(user=self.request.user)
        if likes.first():
            sn_list = []
            for like in likes:
                sn_list.append(like.t1_shop_id)
            return list(set(sn_list))
        else:
            return None


class OrderDetail(LoginRequiredMixin, generic.CreateView):
    model = T3_order_detail
    template_name = "order_detail.html"
    form_class = OrderDetailForm

    def get_success_url(self):
        return reverse_lazy('user:list')

    def form_valid(self, form):
        # food = request.GET.get("food")
        print("se")
        order = form.save(commit=False)
        order.user = self.request.user
        user=T5_user.objects.filter(user=self.request.user)[0]
        order.t4_food_id = T4_food.objects.filter(id=self.kwargs['id'])[0]
        order.t3_payment = order.t3_amount*order.t4_food_id.t4_price+180
        order.t2_order_id = T2_order.objects.filter(id=self.kwargs['pk'])[0]
        driver = T7_delivery_man.objects.filter(
            user__area=self.request.user.area).order_by('?')[0]
        order.t7_delivery_man_id = driver
        order.save()
        if order.t3_payment>user.t5_charge_remain:
            user.t5_charge_remain=0
            messages.success(self.request, '不足分は登録支払い方法によって引き落とされました。')
        else:
            user.t5_charge_remain=user.t5_charge_remain-order.t3_payment
        user.save()
        messages.success(self.request, '注文が登録されました。')
        return super().form_valid(form)
        # messages.success(self.request, '注文が登録されました。')
        # return super().form_valid(form)


# class CreateReview(LoginRequiredMixin, generic.CreateView):
#     model=T6_review
#     template_name="user_createview.html"
#     from_class=ReviewForm
class FoodSearchView(LoginRequiredMixin, generic.ListView):
    template_name = "food_search.html"

    def get_queryset(self):
        q_word = self.request.GET.get('search')
        if q_word:
            object_list = T4_food.objects.filter(Q(t9_food_category_id__t9_food_category_name__icontains=q_word) |
                                                 Q(t4_ingredients__icontains=q_word) | Q(t4_food_name__icontains=q_word))
            if object_list:
                return object_list
            else:
                object_list = T1_shop.objects.filter(Q(t1_shop_name_prime__icontains=q_word) | Q(t8_shop_category_id__t8_shop_category_name__icontains=q_word
                                                                                                 ))
                return object_list
        else:
            object_list = T4_food.objects.all()
            return object_list




class OrderLog(LoginRequiredMixin, generic.ListView):
    model = T3_order_detail
    template_name = 'order_log.html'
    def get_queryset(self):
        
        informations = T3_order_detail.objects.filter(user=self.request.user)
        return informations
    
class CreateReviewView(LoginRequiredMixin,generic.CreateView):
    template_name="user_create_view.html"
    model = T6_review
    form_class = User_ReviewForm

    def get_success_url(self):
        return reverse_lazy('user:product', kwargs={'pk': self.kwargs['pk']})
    def form_valid(self, form):
        review = form.save(commit=False)
        shop=T1_shop.objects.filter(id=self.kwargs['pk'])[0]
        star=(review.t6_star*0.1+shop.t1_review_ave)*0.93
        if star>5:
            star=5
        elif star<1:
            star=1
        shop.t1_review_ave=star
        review.t1_shop_id = shop
        review.save()
        shop.save()
        messages.success(self.request, 'レビューが登録されました。')
        return super().form_valid(form)
