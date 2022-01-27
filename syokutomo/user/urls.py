from django.urls import path

from . import views


app_name = 'user'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('mypage/', views.MypageView.as_view(), name="mypage"),
    path('terms/', views.TermsView.as_view(), name="terms"),
    path('list/', views.ListView.as_view(), name="list"),
    path('mypage/info/<int:pk>/', views.user_informationView.as_view(), name="info"),
    path('mypage/info/user_update/<int:pk>/',
         views.user_updateView.as_view(), name="user_update"),
    path('charge/', views.ChargeView.as_view(), name="charge"),
    path('list/product/<int:pk>/', views.user_productView.as_view(), name="product"),
    path('mypage/charge_history/',
         views.ChargeHistoryView.as_view(), name="charge_history"),
    path('list/product/order/<int:pk>/',
         views.CreateOrderView.as_view(), name="create_order"),
    path('mypage/delete/<int:pk>',
         views.DeleteUserView.as_view(), name="delete_user"),
    path('list/product/food_list/<int:pk>',
         views.FoodDetailView.as_view(), name="food_detail"),
     path('list/product/food_list/<int:pk>/love',
         views.love, name="love"),
     path('like', views.LikeView.as_view(), name="user_like"),
]
