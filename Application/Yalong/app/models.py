from django.db import models

class Post(models.Model):
     title = models.CharField(max_length=100)
     author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
     body = models.TextField()

     def __str__(self):
          return self.title

class Event(models.Model):
     Event_ID = models.AutoField(primary_key=True)
     Event_Name = models.CharField(max_length=120)
     Description = models.TextField(max_length=500)
     Date = models.CharField(max_length=120)
     Time = models.CharField(max_length=120)
     Location = models.CharField(max_length=200)
     Category = models.CharField(max_length=200)
     Status = models.CharField(max_length=200, choices=[ 
         ('Scheduled', 'Scheduled'), 
         ('Completed', 'Completed'),
         ('Cancelled', 'Cancelled') 
     ])
     OrganizerID = models.ForeignKey("Organizer", on_delete=models.CASCADE)
     Budget = models.FloatField()

     def __str__(self):
          return self.Event_Name

class Organizer(models.Model):
     Organizer_ID = models.AutoField(primary_key=True)
     Name = models.CharField(max_length=120)
     Contact_Information = models.CharField(max_length=120)
     Role = models.CharField(max_length=120, choices=[ 
         ('Event Coordinator', 'Event Coordinator'), 
         ('Venue Manager', 'Venue Manager'),
         ('Marketing and Promotion', 'Marketing and Promotion')
     ])

     def __str__(self):
          return self.Name

class Venue(models.Model):
     Venue_ID = models.AutoField(primary_key=True)
     Name = models.CharField(max_length=200)
     Location = models.CharField(max_length=200)
     Capacity = models.IntegerField()
     Type = models.CharField(max_length=120, choices=[ 
         ('outdoor', 'outdoor'), 
         ('indoor', 'indoor')
     ])
     Availability = models.BooleanField()
     Pricing = models.IntegerField()

     def __str__(self):
          return self.Name

class Attendee(models.Model):
     Attendee_ID = models.AutoField(primary_key=True)
     Name = models.CharField(max_length=200)
     Contact_Information = models.CharField(max_length=120)
     Ticket_Type = models.ForeignKey("Ticket", on_delete=models.CASCADE)
     Payment_Status = models.CharField(max_length=120)
     EventRegistration_Date = models.ForeignKey("Event", on_delete=models.CASCADE)

     def __str__(self):
          return self.Name

class Ticket(models.Model):
     Ticket_ID = models.AutoField(primary_key=True)
     Event_ID = models.ForeignKey("Event", on_delete=models.CASCADE)
     Ticket_Type = models.CharField(max_length=120, choices=[ 
         ('GA', 'GA'), 
         ('VIP', 'VIP'), 
         ('Reserved Seating', 'Reserved Seating'),
         ('Discount', 'Discount'), 
         ('Group', 'Group')
     ])
     Price = models.IntegerField()
     Status = models.CharField(max_length=120, choices=[ 
         ('Available', 'Available'), 
         ('Reserved', 'Reserved'), 
         ('Sold', 'Sold'),
         ('Paid', 'Paid'), 
         ('Cancelled/Refunded', 'Cancelled/Refunded'), 
         ('Expired', 'Expired') 
     ])
     DateOfIssue = models.DateField()

     def __str__(self):
          return self.Ticket_Type

class Team(models.Model):
     Services = models.CharField(max_length=100, choices=[ 
         ('Catering', 'Catering'), 
         ('Audio/Visual', 'Audio/Visual'),
         ('Photography', 'Photography')
     ])
     Contact_Information = models.CharField(max_length=100)
     Contract_Status = models.CharField(max_length=100, choices=[ 
         ('Active', 'Active'), 
         ('Expired', 'Expired'),
         ('Terminated', 'Terminated'), 
         ('Suspended', 'Suspended'), 
         ('Under Negotiation', 'Under Negotiation')
     ])

     def __str__(self):
          return self.Services
