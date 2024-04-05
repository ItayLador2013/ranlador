from django.contrib import admin
from .models import Resume, Home, Interest, Research, Image, Location, Contact, Email, UserContact
# Register your models here.

admin.site.register(Resume)
admin.site.register(Home)
admin.site.register(Interest)
admin.site.register(Research)
admin.site.register(Image)
admin.site.register(Location)
admin.site.register(Contact)
admin.site.register(Email)
admin.site.register(UserContact)