from django.shortcuts import render


def about(request):
    template_name = 'about.html'
    return render(request, template_name)


def contact(request):
    template_name = 'contact.html'
    return render(request, template_name)


def gallery(request):
    template_name = 'gallery.html'
    return render(request, template_name)


def index(request):
    template_name = 'index.html'
    return render(request, template_name)
