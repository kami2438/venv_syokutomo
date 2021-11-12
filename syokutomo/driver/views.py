from django.views import generic

# Create your views here.


class IndexView(generic.TemplateView):
    template_name = "driver_index.html"


class MypageView(generic.TemplateView):
    template_name = "driver_mypage.html"


class TermsView(generic.TemplateView):
    template_name = "driver_terms.html"
