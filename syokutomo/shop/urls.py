from django.urls import path

from . import views


app_name = 'shop'
urlpatterns = [
    path('',views.IndexView.as_view(),name="index"),
    path('mypage/',views.MypageView.as_view(),name="mypage"),
    path('terms/',views.TermsView.as_view(),name="terms"),
        path('mypage/info/<int:pk>/',
         views.shop_infoView.as_view(), name="info"),
    path('mypage/info/shop_update/<int:pk>/',
         views.shop_updateView.as_view(), name="shop_update"),
]