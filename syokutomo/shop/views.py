from django.views import generic

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "shop_index.html"

class MypageView(generic.TemplateView):
    template_name = "shop_mypage.html"

class TermsView(generic.TemplateView):
    template_name = "shop_terms_of_service.html"

#class MerchandiseView(LoginRequiredMixin, generic.MerchandiseView):
    model = T1_shop
    template_name = 'shop_merchandise.html'

    def get_queryset(self):
        users = T1_shop.object.filter(user=self.request.user).order_by('-created_at')
        return users