from django.urls import path,include
from .views import HealView

urlpatterns = [
    path('',HealView.as_view()),
    path('auth/',include('apps_v1.users.urls'))
]
