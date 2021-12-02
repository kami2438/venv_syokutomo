from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.postgres import fields
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.contrib import messages

from django.views import generic

from .models import *
# from .forms import *

# Create your views here.


class IndexView(generic.TemplateView):
    template_name = "driver_index.html"


class MypageView(LoginRequiredMixin, generic.ListView):
    template_name = "driver_mypage.html"
    model =T7_delivery_man
    pk_url_kwarg = "id"

    def get_queryset(self):
        informations = T7_delivery_man.objects.filter(user=self.request.user)
        return informations

class TermsView(generic.TemplateView):
    template_name = "driver_terms.html"

class StatusView(generic.TemplateView):
    template_name = "driver_status.html"


class driver_infoView(LoginRequiredMixin, generic.DetailView):
    model = T7_delivery_man
    template_name = "driver_info.html"
