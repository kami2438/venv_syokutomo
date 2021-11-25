from django.urls import path

from . import views


app_name = 'prime'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('choice_login/', views.Choice_loginView.as_view(), name='choice_login'),
    path('terms/', views.TermsView.as_view(), name="terms"),
    path('reservation/', views.ReservationView.as_view(), name="reservation"),
    path('regis_user/', views.Regis_userViews.as_view(), name="regis_user"),
    # path('regis_shop/', views.Regis_shopViews.as_view(), name="regis_shop"),
    # path('regis_driver/', views.Regis_driverViews.as_view(), name="regis_driver"),
]
