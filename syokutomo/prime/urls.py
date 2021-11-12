from django.urls import path

from . import views


app_name = 'prime'
urlpatterns = [
    path('',views.IndexView.as_view(),name="index"),
    path('choice_login',views.Choice_loginView.as_view(),name='choice_login'),
]