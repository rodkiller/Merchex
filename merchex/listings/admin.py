from django.contrib import admin
from listings.models import Band, Title


class BandAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'year_formed', 'genre') # liste les champs que nous voulons sur l'affichage de la liste


class ListingAdmin(admin.ModelAdmin):
    list_display = ('name', 'band')


# Register your models here.
admin.site.register(Band, BandAdmin)
admin.site.register(Title, ListingAdmin)
