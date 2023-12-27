from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("menu/", views.MenuView.as_view()),
    path("", views.home, name="home"),
    path("api-token-auth/", obtain_auth_token),
]
