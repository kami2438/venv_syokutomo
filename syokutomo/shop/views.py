from django.views import generic

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "shop_index.html"

class MypageView(generic.TemplateView):
    template_name = "shop_mypage.html"
