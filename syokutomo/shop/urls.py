from django.urls import path

from . import views


app_name = 'shop'
urlpatterns = [
    path('',views.IndexView.as_view(),name="index"),
    path('mypage/',views.MypageView.as_view(),name="mypage"),
    path('terms/',views.TermsView.as_view(),name="terms"),
#    path('merchandise/', views.MerchandiseView.as_view(),name="merchandise"),
]