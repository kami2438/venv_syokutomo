from django.urls import path

from . import views


app_name = 'user'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('mypage/', views.MypageView.as_view(), name="mypage"),
    path('terms/', views.TermsView.as_view(), name="terms"),
    path('list/', views.ListView.as_view(), name="list"),
    path('mypage/info/<int:pk>/',
         views.user_informationView.as_view(), name="info"),
    path('mypage/info/user_update/<int:pk>/',
         views.user_updateView.as_view(), name="user_update"),
     path('mypage/chrage/',views.user_ChrageView.as_view(),name="chrage")
]
