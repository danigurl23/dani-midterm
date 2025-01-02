from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Event, Organizer
from django.views.generic import ListView
from .models import Organizer
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Event
from .forms import EventForm

class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'app/event_create.html'

    def get_success_url(self):
        return reverse_lazy('contact')  

class OrganizerListView(ListView):
    model = Organizer
    template_name = 'app/Organizer.html'
    context_object_name = 'organizers'

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class ContactPageView(TemplateView):
    template_name = 'app/contact.html'

class EventListView(ListView):
    model = Event
    template_name = 'app/Event.html'
    context_object_name = 'events'

class EventDetailView(DetailView):
    model = Event
    template_name = 'app/event_detail.html'
    context_object_name = 'event'

class EventUpdateView(UpdateView):
    model = Event
    template_name = 'app/event_update.html'
    fields = ['Event_Name', 'Description', 'Date', 'Time', 'Location', 'Category', 'Status', 'OrganizerID', 'Budget']
    success_url = reverse_lazy('Event')  
class EventDeleteView(DeleteView):
    model = Event
    template_name = 'app/event_delete.html'
    success_url = reverse_lazy('Event') 