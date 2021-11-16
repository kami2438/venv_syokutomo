from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse_lazy

class MyCrmAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        resolved_url = super().get_login_redirect_url(request)
        user_obj = request.user
        try:
            groupsettings = user_obj.groupsettings
        except:
            resolved_url = reverse_lazy("settings_form")
        return resolved_url