from ast import Add, Store
import imp
from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import *
from myapp.forms import *

# Create your views here.

def index(request, *args, **kwargs):
    persons = Person.objects.all()
    persons_Male = Person.objects.filter(sex='M')
    persons_Female = Person.objects.filter(sex='F')
    persons_major = Person.objects.filter(age__gt=18)

    context = {
        'persons': persons,
        'persons_major': persons_major,
        'persons_Male': persons_Male,
        'persons_Female': persons_Female,
    }

    return render(request, 'index.html', context,)

def add_person(request, *args):

    context={}

    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {'form': form }

    return render(request, 'add_person.html', context,)

def add_product(request, *args):

    context={}

    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('product')

    context = {'form': form }
    return render(request, 'add_product.html', context,)
        

def add_store(request, *args):

    context={}
    form = StoreForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('store')

    context = {'form': form }
    return render(request, 'add_store.html', context,)


def add_profileStore(request, *args):

    context={}
    form = ProfilStoreForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('profile')

    context = {'form': form }
    return render(request, 'add_profileStore.html', context,)


    
def updatePerson(request, *args, **kwargs):
    obj = get_object_or_404(
        Person,
        pk=kwargs.get('pk')
    )

    if request.method == 'GET':
        form = PersonForm(
            initial={
                'name': obj.name,
                'age': obj.age,
                'sex': obj.sex,
                'country': obj.country,
            }
        )

        context = {'form': form }

        return render(request, 'updatePerson.html', context,)

    if request.method == 'POST':
        form = PersonForm(
            request.POST,
            request.FILES,
            initial={
                'name': obj.name,
                'age': obj.age,
                'sex': obj.sex,
                'country': obj.country,
            }
        )

        context = {'form': form }
        
        if form.is_valid():
            print(form.cleaned_data)
            obj.name = form.cleaned_data.get('name')
            obj.sex = form.cleaned_data.get('sex')
            obj.age = form.cleaned_data.get('age')
            obj.country = form.cleaned_data.get('country')
            obj.save()
            return redirect('index')

        return render(request, 'updatePerson.html', context,)

def product(request, *args, **kwargs):
    products = Produit.objects.all()
    context = {
        'products': products,
    }

    return render(request, 'products.html', context,)

def updateProduct(request, *args, **kwargs):
    obj = get_object_or_404(
        Produit,
        pk=kwargs.get('pk')
    )
    if request.method == 'GET':
        form = ProductForm(
            initial={
                'name': obj.name,
                'country': obj.country,
                'price': obj.price,
            }
        )
        context = {'form': form }

        return render(request, 'updatePerson.html', context,)

    if request.method == 'POST':
        form = ProductForm(
            request.POST,
            request.FILES,
            initial={
                'name': obj.name,
                'country': obj.country,
                'price': obj.price,
            }
        )

        context = { 'form': form }
        
        if form.is_valid():
            print(form.cleaned_data)
            obj.name = form.cleaned_data.get('name')
            obj.country = form.cleaned_data.get('country')
            obj.created_at = form.cleaned_data.get('created_at')
            obj.updated_at = form.cleaned_data.get('updated_at')
            obj.save()
            return redirect('product')

        return render(request, 'updateProduct.html', context,)

def store(request, *args, **kwargs):
    stores = Magasin.objects.all()

    context = {
        'stores': stores,
    }

    return render(request, 'store.html', context,)

def updateStore(request, *args, **kwargs):
    obj = get_object_or_404(
        Magasin,
        pk=kwargs.get('pk')
    )
    
    if request.method == 'GET':
        form = StoreForm(
            initial={
                'name': obj.name,
                'country': obj.country,
            }
        )
        context = {'form': form}

        return render(request, 'updateStore.html', context,)

    if request.method == 'POST':
        form = StoreForm(
            request.POST,
            request.FILES,
            initial={
                'name': obj.name,
                'country': obj.country,
            }
        )

        context = {'form': form }

        if form.is_valid():
            print(form.cleaned_data)
            obj.name = form.cleaned_data.get('name')
            obj.country = form.cleaned_data.get('country')
            obj.created_at = form.cleaned_data.get('created_at')
            obj.updated_at = form.cleaned_data.get('updated_at')
            obj.save()
            return redirect('store')

        return render(request, 'updateStore.html', context,)

def profile(request, *args, **kwargs):
    profiles = ProfileMagasin.objects.all()

    context = {
        'profiles': profiles,
    }

    return render(request, 'profilStore.html', context,)

def updateProfilStore(request, *args, **kwargs):
    obj = get_object_or_404(
        ProfileMagasin,
        pk=kwargs.get('pk')
    )

    if request.method == 'GET':
        form = ProfilStoreForm(
            initial={
                'email': obj.email,
                'phone': obj.phone,
            }
        )
    
        context = {'form': form }

        return render(request, 'updateStore.html', context,)

    if request.method == 'POST':
        form = StoreForm(
            request.POST,
            request.FILES,
            initial={
                'email': obj.email,
                'phone': obj.phone,
            }
        )

        context = {'form': form}
        
        if form.is_valid():
            print(form.cleaned_data)
            obj.email = form.cleaned_data.get('email')
            obj.phone = form.cleaned_data.get('phone')
            obj.created_at = form.cleaned_data.get('created_at')
            obj.updated_at = form.cleaned_data.get('updated_at')
            obj.magasin = form.cleaned_data.get('magasin_id')
            obj.save()
            return redirect('store')

        return render(request, 'updateStore.html', context,)

def delete_person(request, **kwargs):
    context = {}

    obj = get_object_or_404(
        Person,
        pk=kwargs.get('pk')
    )

    if request.method == "POST":
        obj.delete()
        return redirect('index')

    return render(request, 'delete.html', context)

def delete_product(request, **kwargs):
    context = {}

    obj = get_object_or_404(
        Produit,
        pk=kwargs.get('pk')
    )

    if request.method == "POST":
        obj.delete()
        return redirect('product')

    return render(request, 'delete.html', context)

def delete_store(request, **kwargs):
    context = {}

    obj = get_object_or_404(
        Magasin,
        pk=kwargs.get('pk')
    )

    if request.method == "POST":
        obj.delete()
        return redirect('store')

    return render(request, 'delete.html', context)

def delete_profileStore(request, **kwargs):
    context = {}

    obj = get_object_or_404(
        ProfileMagasin,
        pk=kwargs.get('pk')
    )

    if request.method == "POST":
        obj.delete()
        return redirect('profile')

    return render(request, 'delete.html', context)