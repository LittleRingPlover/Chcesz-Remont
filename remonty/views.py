from django.http import Http404
from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail


def custom_404(request, exception):
    facebook = Contact.objects.get()
    fixly = Contact.objects.get()
    phone_number = Contact.objects.get()
    context = {'facebook': facebook,
               'fixly': fixly,
               'phone_number': phone_number}
    return render(request, 'remonty/404.html', context)


def index(request):
    facebook = Contact.objects.get()
    fixly = Contact.objects.get()
    phone_number = Contact.objects.get()
    context = {'facebook': facebook,
               'fixly': fixly,
               'phone_number': phone_number}
    return render(request, 'remonty/index.html', context)


def services(request):
    all_services = Service.objects.all()
    service_info = ServiceDescription.objects.get()
    phone_number = Contact.objects.get()
    facebook = Contact.objects.get()
    fixly = Contact.objects.get()
    context = {'all_services': all_services,
               'service_info': service_info,
               'phone_number': phone_number,
               'facebook': facebook,
               'fixly': fixly}
    return render(request, 'remonty/uslugi.html', context)


def about_me(request):
    info = AboutMe.objects.get()
    phone_number = Contact.objects.get()
    facebook = Contact.objects.get()
    fixly = Contact.objects.get()
    context = {'info': info,
               'phone_number': phone_number,
               'facebook': facebook,
               'fixly': fixly}
    return render(request, 'remonty/o-mnie.html', context)


def gallery(request):
    categories = Category.objects.all()
    phone_number = Contact.objects.get()
    facebook = Contact.objects.get()
    fixly = Contact.objects.get()
    cat_id = request.GET.get('categories')

    try:
        if cat_id and cat_id.isnumeric():
            category = Category.objects.get(pk=cat_id)
            filtered_images = Gallery.objects.filter(category=category).order_by('publication_date')
        else:
            filtered_images = Gallery.objects.all().order_by('publication_date')
    except Category.DoesNotExist:
        raise Http404("Wybrana kategoria nie istnieje.")

    context = {'filtered_images': filtered_images,
               'categories': categories,
               'phone_number': phone_number,
               'facebook': facebook,
               'fixly': fixly}
    return render(request, 'remonty/galeria.html', context)


def contact(request):
    name = Contact.objects.get()
    phone_number = Contact.objects.get()
    email = Contact.objects.get()
    facebook = Contact.objects.get()
    fixly = Contact.objects.get()

    context = {'name': name,
               'phone_number': phone_number,
               'email': email,
               'facebook': facebook,
               'fixly': fixly,
               }
    return render(request, 'remonty/kontakt.html', context)
