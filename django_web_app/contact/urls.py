from django.urls import path

from . import views
from .views import SignUpView
from django.views.generic.base import TemplateView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("", TemplateView.as_view(template_name="contact.html"), name="contact_index"),
]