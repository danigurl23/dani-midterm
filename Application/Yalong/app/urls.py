from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    ContactPageView,
    EventListView,
    EventDetailView,
    EventCreateView,
    EventUpdateView,
    EventDeleteView,
    OrganizerListView,
)


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutPageView.as_view(), name='about'),
    path('contact', ContactPageView.as_view(), name='contact'),
    path('Event', EventListView.as_view(), name='Event'),
    path('Event/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('Event/create/', EventCreateView.as_view(), name='event_create'),
    path('Event/<int:pk>/update/', EventUpdateView.as_view(), name='event_update'),
    path('Event/<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),
    path('Organizer', OrganizerListView.as_view(), name='Organizer'),
]
