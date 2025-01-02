from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'Event_Name',
            'Description',
            'Date',
            'Time',
            'Location',
            'Category',
            'Status',
            'OrganizerID',
            'Budget',
        ]
