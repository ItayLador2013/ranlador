from django.db import models

# Create your models here.

class Resume(models.Model):
    resume = models.FileField(upload_to="assets/", blank=True)

class Home(models.Model):
    backgroundImage = models.FileField(upload_to="images/", blank=True)
    altBackgroundImage = models.FileField(upload_to="images/", blank=True)
    name = models.CharField(max_length=300, blank=True)
    profileImage = models.FileField(upload_to="images/", blank=True)
    title = models.CharField(max_length=300, blank=True)
    bio = models.TextField(blank=True)
    scheduleLing = models.TextField
    research = models.TextField(blank=True)

class Interest(models.Model):
    interest = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    icon = models.FileField(upload_to="images/", blank=True)

    def __str__(self):
        return self.interest

class Image(models.Model):
    image = models.FileField(upload_to="images/", blank=True)

class Research(models.Model):
    title = models.CharField(max_length=300, blank=True)
    publisher = models.CharField(max_length=300, blank=True)
    pdf = models.FileField(upload_to="assets/papers/", blank=True )
    images = models.ManyToManyField(Image, blank=True, related_name="+")
    date = models.DateField(blank=True, null=True, max_length=300)
    dateStr = models.CharField(blank=True, max_length=300)
    collaborators = models.TextField(blank=True)
    abstract = models.TextField(blank=True)
    keywords = models.TextField(blank=True)
    
    def __str__(self):
        return "(" + str(self.id) + ") - " + self.title

class Location(models.Model):
    title = models.TextField(blank=True)
    number = models.CharField(max_length=300, blank=True)
    address = models.CharField(max_length=300, blank=True)
    location = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.title

class Email(models.Model):
    email = models.CharField(max_length=300, blank=True)
    
    def __str__(self):
        return self.email

class Contact(models.Model):
    phone = models.CharField(max_length=300, blank=True)
    emails = models.ManyToManyField(Email, blank=True, related_name="+")

class UserContact(models.Model):
    ip = models.CharField(max_length=300, blank=True)
    email = models.CharField(max_length=300, blank=True)
    name = models.CharField(max_length=300, blank=True)
    message = models.TextField(blank=True)
    datetime = models.DateTimeField(blank=True, null=True)
    phone = models.CharField(max_length=300, blank=True)
    
    def __str__(self):
        return str(self.id) + " - " + self.name + " " + " " + " - " + str(self.datetime)

