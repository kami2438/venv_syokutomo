from django.views import generic

# Create your views here.


class IndexView(generic.TemplateView):
    template_name = "index.html"


class Choice_loginView(generic.TemplateView):
    template_name = 'choice_login.html'


class TermsView(generic.TemplateView):
    template_name = "prime_terms.html"


class ReservationView(generic.FormView):
    template_name = "prime_reservation.html"
    form_class = ReservationForm
