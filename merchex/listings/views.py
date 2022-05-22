from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band, Title


def bands_list(request):   #request est une demande HTTPrequest
    bands = Band.objects.all()
    return render(request, 'listings/bands_list.html', {'bands': bands})

def band_detail(request, band_id):  # notez le paramètre id supplémentaire
    band = Band.objects.get(id=band_id)
    return render(request,
          'listings/band_detail.html',
         {'band': band}) # nous passons l'id au modèle



def about(request):
    return render(request, 'listings/about.html')


def listings(request):
    titles = Title.objects.all()
    return render(request, 'listings/listings.html', {'titles': titles})


def listings_detail(request, title_id):
    title = Title.objects.get(id=title_id)
    return render(request, 'listings/listing_detail.html', {'title': title})


def contact_us(request):
    return HttpResponse('<h1>Contact Us</h1> <p>Nous sommes ici pour vous !</p>')

