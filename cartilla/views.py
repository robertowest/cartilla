from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "cartilla/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Cartilla"
        context['subtitulo'] = "Menú a la Carta"
        context['mensaje'] = "Carta de productos por categorías"
        return context
