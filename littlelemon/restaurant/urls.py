from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("menu/", views.menu_page, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
    path("book/", views.book_page, name="book"),
    path("menu-api/", views.MenuView.as_view()),
    path("api-token-auth/", obtain_auth_token),
]
