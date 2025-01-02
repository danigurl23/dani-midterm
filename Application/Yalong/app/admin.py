from django.contrib import admin
from .models import Post, Event, Organizer, Attendee, Venue, Ticket, Team

# Register your models here.
admin.site.register(Post)
admin.site.register(Event)
admin.site.register(Organizer)
admin.site.register(Attendee)
admin.site.register(Venue)
admin.site.register(Ticket)
admin.site.register(Team)


