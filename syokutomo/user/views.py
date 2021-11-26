from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic

from prime.models import T1_shop

# Create your views here.


class IndexView(generic.TemplateView):
    template_name = "user_index.html"


class MypageView(generic.TemplateView):
    template_name = "user_mypage.html"


class TermsView(generic.TemplateView):
    template_name = "user_terms.html"

class ListView(LoginRequiredMixin, generic.ListView):
    model = T1_shop
    template_name = 'user_shoplist.html'

    def get_queryset(self):
        users = T1_shop.object.filter(user=self.request.user).order_by('-created_at')
        return users