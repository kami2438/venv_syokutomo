from django.urls import path

from . import views


app_name = 'prime'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('choice_login/', views.Choice_loginView.as_view(), name='choice_login'),
    path('terms/', views.TermsView.as_view(), name="terms"),
    path('reservation/', views.ReservationView.as_view(), name="reservation"),
    path('main_regis_user/', views.Prime_main_regis_userViews.as_view(), name=",main_regis_user"),
    path('main_regis_shop/', views.Prime_main_regis_shopViews.as_view(), name=",main_regis_shop"),
    path('main_regis_driver/', views.Prime_main_regis_driverViews.as_view(), name=",main_regis_driver"),
]