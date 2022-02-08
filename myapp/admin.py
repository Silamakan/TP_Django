from django.contrib import admin
from myapp.models import Person
from myapp.models import Produit
from myapp.models import Magasin
# Register your models here.

admin.site.register(Person)
admin.site.register(Produit)
admin.site.register(Magasin)
