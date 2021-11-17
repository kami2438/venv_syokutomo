import logging

from django.urls import reverse_lazy

from django.views import generic

from .forms import ReservationForm

from django.contrib import messages
# Create your views here.

logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name = "index.html"


class Choice_loginView(generic.TemplateView):
    template_name = 'choice_login.html'


class TermsView(generic.TemplateView):
    template_name = "prime_terms.html"


class ReservationView(generic.FormView):
    template_name = "prime_reservation.html"
    form_class = ReservationForm
    success_url = reverse_lazy('prime:index')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class Regis_userViews(generic.TemplateView):
    template_name = 'regis_user.html'

class Regis_shopViews(generic.TemplateView):
    template_name = 'regis_shop.html'

class Regis_driverViews(generic.TemplateView):
    template_name = 'regis_driver.html'
