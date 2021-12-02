from django.urls import path

from . import views


app_name = 'driver'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('mypage', views.MypageView.as_view(), name="mypage"),
    path('terms', views.TermsView.as_view(), name="terms"),
    path('status', views.StatusView.as_view(), name="status"),
    path('mypage/info/<int:pk>', views.driver_infoView.as_view(), name="info"),
]
