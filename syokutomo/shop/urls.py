from django.urls import path

from . import views


app_name = 'shop'
urlpatterns = [
    path('',views.IndexView.as_view(),name="index"),
    path('mypage',views.MypageView.as_view(),name="mypage")
]