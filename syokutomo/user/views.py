from django.views import generic

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "user_index.html"