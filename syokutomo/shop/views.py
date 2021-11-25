from django.views import generic



# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "shop_index.html"

class MypageView(generic.TemplateView):
    template_name = "shop_mypage.html"

class TermsView(generic.TemplateView):
    template_name = "shop_terms_of_service.html"

#class ListView(LoginRequiredMixin, generic.ListView):
#    model = T1_shop
#    template_name = 'shop_list.html'

#    def get_queryset(self):
#        shops = T1_shop.object.filter(user=self.request.user).order_by('-created_at')
#        return shop
