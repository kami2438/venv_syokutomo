from django.urls import path

from . import views


app_name = 'prime'
urlpatterns = [
    path('',views.IndexView.as_view(),name="index"),
]