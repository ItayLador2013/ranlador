from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
from django.http import Http404
from datetime import datetime
from datetime import date
import csv
import pandas as pd
from .models import Resume, Home, Interest, Research, Image, Location, Contact, UserContact, Email
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

HOME_DESCRIPTION = "Dr. Ran Lador is an assistant professor in the Department of Orthopedic surgery at McGovern Medical School at The University of Texas Health Science Center at Houston (UTHealth). Certified by the Israeli Board of Orthopedic Surgery, Dr. Lador specializes in the surgical care of complex spinal disorders and Orthopedic Trauma with an emphasis in spinal trauma and tumors, degenerative spinal disorders, revision spinal surgery, use of advanced technologies including navigation and minimal invasive techniques."
KEY = "Ran, Lador, Ran Lador, Spine, Surgeon, Spine Surgeon"

def index(request):
    if request.method == "GET":
        key_words = KEY

        return render(request, "home/index.html", {
            "home": Home.objects.all()[len(Home.objects.all())-1],
            'resume': Resume.objects.all()[len(Resume.objects.all())-1],
            "interests": Interest.objects.all(),
            "page_title": "Home",
            "description": HOME_DESCRIPTION,
            "key_words": key_words,
            'locations': Location.objects.all(),
            'contact': Contact.objects.all()[len(Contact.objects.all())-1],
            'homepage': True,
        })

def research(request):
    if request.method == "GET":
        key_words = KEY + ", Publications, Spinal Research, Research"
        research = Research.objects.all().order_by('-date')

        return render(request, "home/research.html", {
            "research": research,
            "home": Home.objects.all()[len(Home.objects.all())-1],
            'page_title': "Publications",
            "description": Home.objects.all()[len(Home.objects.all())-1].research,
            "key_words": key_words,
            'resume': Resume.objects.all()[len(Resume.objects.all())-1],
            'locations': Location.objects.all(),
            'contact': Contact.objects.all()[len(Contact.objects.all())-1],
        })

def paper(request, paperID, paperTitle):
    if request.method == "GET":
        key_words = KEY + ", Publications, Spinal Research, Research"
        try:
            paper = Research.objects.get(id=paperID)
            pt = paper.title.replace("?", "")
            paperTitle = paperTitle.replace("?", "")
            if pt != paperTitle: 
                raise Http404
        except Research.DoesNotExist:
            raise Http404

        if len(paper.keywords) > 0:
            key_words += ", " + paper.keywords
        key_words += ", " + paper.title + ", " + paper.publisher

        return render(request, "home/paper.html", {
            "paper": paper,
            "home": Home.objects.all()[len(Home.objects.all())-1],
            'page_title': "Publications",
            "description": paper.abstract,
            "key_words": key_words,
            'resume': Resume.objects.all()[len(Resume.objects.all())-1],
            'locations': Location.objects.all(),
            'contact': Contact.objects.all()[len(Contact.objects.all())-1],
        })

def reviews(request):
    if request.method == "GET":
        key_words = KEY + ", reviews, patient expirience, patient, expirience"

        return render(request, "home/reviews.html", {
            "home": Home.objects.all()[len(Home.objects.all())-1],
            'resume': Resume.objects.all()[len(Resume.objects.all())-1],
            "interests": Interest.objects.all(),
            "page_title": "Home",
            "description": HOME_DESCRIPTION,
            "key_words": key_words,
            'locations': Location.objects.all(),
            'contact': Contact.objects.all()[len(Contact.objects.all())-1],
        })

def contact(request):
    if request.method == "GET":
        key_words = KEY + ", contact, patient, patient, schedule, appointment, schedule appointment"

        return render(request, "home/contact.html", {
            "home": Home.objects.all()[len(Home.objects.all())-1],
            'resume': Resume.objects.all()[len(Resume.objects.all())-1],
            "interests": Interest.objects.all(),
            "page_title": "Home",
            "description": HOME_DESCRIPTION,
            "key_words": key_words,
            'locations': Location.objects.all(),
            'contact': Contact.objects.all()[len(Contact.objects.all())-1],
            'homepage': False
        })

@csrf_exempt
def send(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")
        message = data.get("message")

        subject = name + " would like to schedule an appointment with Dr. Ran Lador"

        html_content = render_to_string('home/email2.html', {'subject': subject, 'message': message, 'email': email, 'phone': phone, 'name': name})
        text_content = strip_tags(html_content)  # Strip HTML tags for the plain text version
        addresses = []
        addresses += list(Email.objects.all())
        mail = EmailMultiAlternatives(
            subject=subject,
            body=text_content,
            to=addresses,  # List of recipient email addresses
        )
        mail.attach_alternative(html_content, "text/html")
        mail.send()

        html_content = render_to_string('home/email.html', {'subject': subject, 'message': message, 'email': email, 'phone': phone, 'name': name})
        mail = EmailMultiAlternatives(
            subject="Confirmation: appointment schedule request with Dr. Ran Lador",
            body=text_content,
            to=[email],  # List of recipient email addresses
        )
        mail.attach_alternative(html_content, "text/html")
        mail.send()

        ip = request.META.get('REMOTE_ADDR')
        UserContact.objects.create(name=name, datetime=datetime.now(), email=email, message=message, phone=phone, ip=ip)

        return JsonResponse(True, safe=False)