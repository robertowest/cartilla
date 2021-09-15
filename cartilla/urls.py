from django.urls import path

# from django.views.generic import TemplateView
# urlpatterns = [
#     path('', TemplateView.as_view(template_name="cartilla/index.html")),
# ]

from cartilla.views import IndexView

urlpatterns = [
    path('', IndexView.as_view()),
]
