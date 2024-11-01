from django.db.models.query import QuerySet
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Chord, Category, LiturgicalTime, Mass
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

class ChordView(TemplateView):
    template_name = 'home.html'

# Create Chords

class CategoryCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"coordenador"
    model = Category
    fields = ['name']
    template_name = 'create/create-category.html'
    success_url = reverse_lazy('list-category')


class LiturgicalTimeCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"coordenador"
    model = LiturgicalTime
    fields = ['name']
    template_name = 'create/create-liturgical-time.html'
    success_url = reverse_lazy('list-liturgical-time')


class ChordCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"coordenador"
    model = Chord
    fields = '__all__'
    template_name = 'create/create-chord.html'
    success_url = reverse_lazy('list-chords')

    
class MassCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"coordenador"
    model = Mass
    fields = '__all__'
    template_name = 'create/create-mass.html'
    success_url = reverse_lazy('list-mass')


# Update Chords

class CategoryUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"coordenador"
    model = Category
    fields = ['name']
    template_name = 'edit/update-category.html'
    success_url = reverse_lazy('list-category')


class LiturgicalTimeUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"coordenador"
    model = LiturgicalTime
    fields = ['name']
    template_name = 'edit/update-liturgical-time.html'
    success_url = reverse_lazy('list-liturgical-time')


class ChordUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"coordenador"
    model = Chord
    fields = '__all__'
    template_name = 'edit/update-chord.html'
    success_url = reverse_lazy('list-chords')


class MassUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"coordenador"
    model = Mass
    fields = '__all__'
    template_name = 'edit/update-mass.html'
    success_url = reverse_lazy('list-mass')

# Delete Chords

class CategoryDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"coordenador"
    model = Category
    template_name = 'delete/delete-category.html'
    success_url =reverse_lazy('list-category')


class LiturgicalTimeDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"coordenador"
    model = LiturgicalTime
    template_name = 'delete/delete-liturgical-time.html'
    success_url = reverse_lazy('list-liturgical-time')


class ChordDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"coordenador"
    model = Chord
    template_name = 'delete/delete-chord.html'
    success_url = reverse_lazy('list-chords')


# List Chords

class CategoryList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"coordenador"
    model = Category
    template_name = 'list/list-category.html'


class LiturgicalTimeList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"coordenador"
    model = LiturgicalTime
    template_name = 'list/list-liturgical-time.html'


class ChordList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Chord
    template_name = 'list/list-chords.html'


class MassList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Mass
    template_name = 'list/list-mass.html'
    
    def get_queryset(self):
        date = self.request.GET.get('date')
        mass = Mass.objects.filter(date = date)

        return mass