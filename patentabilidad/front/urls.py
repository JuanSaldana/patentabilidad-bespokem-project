from django.urls import path, include
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path("", views.index, name="index"),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('front/icons/favicon.ico')), name="favicon.ico"),
    
    # authenticate views
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout")
]
