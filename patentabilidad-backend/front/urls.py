from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    
    # authenticate views
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout")
]
