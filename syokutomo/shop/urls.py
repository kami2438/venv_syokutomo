from django.urls import path

from . import views


app_name = 'shop'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('mypage/', views.MypageView.as_view(), name="mypage"),
    path('terms/', views.TermsView.as_view(), name="terms"),
    path('mypage/info/<int:pk>/',
         views.shop_infoView.as_view(), name="info"),
    path('mypage/info/shop_update/<int:pk>/',
         views.shop_updateView.as_view(), name="shop_update"),
    path('food-list/', views.FoodListView.as_view(), name='food_list'),
    path('food-detail/<t1_shop_id>/',
         views.FoodDetailView.as_view(), name='food_detail'),
    path('food-update/<int:pk>/', views.FoodUpdateView.as_view(), name='food_update'),
    path('food-delete/<int:pk>/', views.FoodDeleteView.as_view(), name='food_delete'),
    path('check_review/', views.CheckReviewView.as_view(), name='check_review'),
    path('food-create/', views.FoodCreateView.as_view(), name='food_create'),
    path('food_list_ex/<int:pk>/',
         views.FoodListExView.as_view(), name='food_list_ex'),
    #     path('delivery_status/<int:pk>/',
    #          views.DeliveryStatusView.as_view(), name='delivery_status'),
]
