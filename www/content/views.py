from django.views import generic
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse_lazy


class ContactFormView(generic.TemplateView):
    template_name = 'content/contact.html'


class HomeView(generic.TemplateView):
    template_name = 'content/home.html'


class BiographyView(generic.TemplateView):
    template_name = 'content/biography.html'
