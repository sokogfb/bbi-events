from django.shortcuts import render


def about(request):
    return render(request, template_name="about.html")


def contact(request):
    return render(request, template_name="contact.html")


def gallery(request):
    return render(request, template_name="gallery.html")


def index(request):
    return render(request, template_name="index.html")
