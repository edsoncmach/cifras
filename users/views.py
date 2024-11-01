from django.views.generic import TemplateView

class UserView(TemplateView):
    template_name = 'list-mass.html'
