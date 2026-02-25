from django.urls import path,include
from .views import GoogleSocialAccount

urlpatterns = [
    path('',include('dj_rest_auth.urls')),
    path('registration/',include('dj_rest_auth.registration.urls')),
    path('google/',GoogleSocialAccount.as_view())
]
