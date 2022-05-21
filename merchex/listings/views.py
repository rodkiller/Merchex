from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band, Title


def hello(request):   #request est une demande HTTPrequest
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', {'bands': bands})


def about(request):
    return render(request, 'listings/about.html')


def listings(request):
    titles = Title.objects.all()
    return render(request, 'listings/listings.html', {'titles': titles})


def contact_us(request):
    return HttpResponse('<h1>Contact Us</h1> <p>Nous sommes ici pour vous !</p>')

