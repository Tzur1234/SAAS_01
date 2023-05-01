from django.urls import path, include, re_path
from django.views.generic import TemplateView
app_name = 'core'
urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/demo.html"), name="demo")
]
