from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.postgres import fields
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.contrib import messages

from django.views import generic
from prime.models import *
from .models import *
from .forms import *
from django.views.generic.edit import CreateView

# Create your views here.


class IndexView(generic.TemplateView):
    template_name = "shop_index.html"


class MypageView(LoginRequiredMixin, generic.ListView):
    template_name = "shop_mypage.html"
    model = T1_shop
    pk_url_kwarg = "id"
    print('get')

    def get_queryset(self):
        informations = T1_shop.objects.filter(user=self.request.user)
        print('2')
        return informations


class TermsView(generic.TemplateView):
    template_name = "shop_terms_of_service.html"

# class MerchandiseView(LoginRequiredMixin, generic.MerchandiseView):
#    model = T1_shop
#    template_name = 'shop_merchandise.html'

#    def get_queryset(self):
#        users = T1_shop.object.filter(user=self.request.user).order_by('-created_at')
#        return users


class shop_infoView(LoginRequiredMixin, generic.DetailView):
    model = T1_shop
    template_name = "shop_info.html"


class shop_updateView(LoginRequiredMixin, generic.UpdateView):
    model = T1_shop
    template_name = "shop_update.html"
    form_class = shop_updateForm

    def get_success_url(self):
        return reverse_lazy('shop:info', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "更新に失敗しました。")
        return super().form_invalid(form)


class FoodCreateView(LoginRequiredMixin, generic.CreateView):
    model = T4_food
    template_name = 'food_create.html'
    form_class = Food_createform
    success_url = reverse_lazy('prime:food_list')

    def form_valid(self, form):
        food_list = form.save(commit=False)
        food_list.user = self.request.user
        food_list.save()
        messages.success(self.request, '商品追加しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        message.error(self.request, '商品追加失敗しました。')
        return super().form_invalid(form)


class FoodListView(LoginRequiredMixin, generic.ListView):
    model = T4_food
    template_name = 'food_list.html'

    def get_queryset(self):

        # ログインしているユーザーとT1_shopテイブルに同じユーザーを選択し、そのidをlistに入れる
        t1id = list(T1_shop.objects.filter(
            user=self.request.user).values_list('id'))
        # t1_shop_id__in  list の中にt1_shop_idを取り出します
        food_q = T4_food.objects.filter(
            t1_shop_id__in=t1id).order_by('t4_create_at')

        return food_q


class FoodDetailView(LoginRequiredMixin, generic.DetailView):
    model = T4_food
    template_name = 'food_detail.html'
    # ルーティングの変数名、変数はモジュールにある変数
    pk_url_kwarg = 't1_shop_id'

    def get_queryset(self):

        # ログインしているユーザーとT1_shopテイブルに同じユーザーを選択し、そのidをlistに入れる
        t1id = list(T1_shop.objects.filter(
            user=self.request.user).values_list('id'))
        # t1_shop_id__in  list の中にt1_shop_idを取り出します
        food_q = T4_food.objects.filter(
            t1_shop_id__in=t1id).order_by('t4_create_at')

        return food_q


class FoodDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = T4_food
    template_name = 'food_delete.html'
    success_url = reverse_lazy('shop:food_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, '商品を削除しました。')
        return super().delete(request, *args, **kwargs)


class FoodUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = T4_food
    template_name = 'food_update.html'
    form_class = Food_createform

    def get_success_url(self):
        return reverse_lazy('shop:food_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '商品更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '商品更新に失敗しました。')
        return super().form_invalid(form)


class CheckReviewView(LoginRequiredMixin, generic.ListView):
    model = T6_review
    template_name = 'shop_check_review.html'
    # def get_queryset(self):
    #     shop=T1_shop.objects.filter(user=self.request.user)
    #     print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
    #     print(shop)
    #     review = T6_review.objects.filter(t1_shop_id=shop.pk)
    #     print(review)
    #     print('xxxxxxxxx')
    #     return review
    def get_context_data(self, **kwargs):
        shop=T1_shop.objects.filter(user=self.request.user)
        context = super().get_context_data(**kwargs)
        context["review"]=T6_review.objects.filter(t1_shop_id=shop)
        print(context["review"])
        return context
