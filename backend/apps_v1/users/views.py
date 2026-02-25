from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
# Create your views here.

class GoogleSocialAccount(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter