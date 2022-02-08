from dataclasses import fields
import email
from email.mime import image
from django import forms
from django.conf import settings
from myapp.models import Person
# from myproject.myapp.models import Person

class Form(forms.ModelForm):
    name = forms.CharField(max_length=100, help_text = "Enter a name")
    age = forms.IntegerField(help_text = "Enter an age")
    sex = forms.CharField(max_length=100, help_text = "Enter a sex")
    country = forms.CharField(max_length=100, help_text = "Enter a country")

    class Meta:
        model = Person
        fields = [
            "name",
            "age",
            "sex",
            "country",
        ]
        # fields = ('name',)
        # fields = ('age',)
        # fields = ('sex',)
        # fields = ('country',)

class PersonForm(Form):
    name=forms.CharField(required=True, max_length=200, strip=True, min_length=2,
         widget=forms.TextInput(
            attrs={
                'type':'text',
                'class': 'form-control',
                'placeholder': 'Votre Nom',
            }
        )
    )

    age = forms.IntegerField(required=True, max_value=150, min_value=5,
        widget=forms.NumberInput(
            attrs={
                'type':'number'
            }
        )    
    )

    sex = forms.ChoiceField( required=True, choices=[(x, y) for (x, y) in settings.SEXE],
        widget=forms.Select(
            attrs={
                'type': 'select'
            }
        )
    )

    country = forms.ChoiceField(required=True, choices=[(x, y) for (x, y) in settings.COUNTRIES],
        widget=forms.Select(
            attrs={
                'type':'select'
            }
        )
    )

class AddPersonForm(forms.Form):
    name=forms.CharField(required=True, max_length=200, strip=True, min_length=2,
         widget=forms.TextInput(
            attrs={
                'type':'text',
                'class': 'form-control'
            }
        )
    )

    age = forms.IntegerField(required=True, max_value=150, min_value=5,
        widget=forms.NumberInput(
            attrs={
                'type':'number'
            }
        )    
    )

    sex = forms.ChoiceField( required=True, choices=[(x, y) for (x, y) in settings.SEXE],
        widget=forms.Select(
            attrs={
                'type': 'select'
            }
        )
    )

    country = forms.ChoiceField(required=True, choices=[(x, y) for (x, y) in settings.COUNTRIES],
        widget=forms.Select(
            attrs={
                'type':'select'
            }
        )
    )


class ProductForm(forms.Form):
    name=forms.CharField(required=True, max_length=200, strip=True, min_length=2,
         widget=forms.TextInput(
            attrs={
                'type':'text'
            }
        )
    )

    #liste de choix ou x est affiché dans montableau et y ma formulaire
    country = forms.ChoiceField(required=True, choices=[(x, y) for (x, y) in settings.COUNTRIES],
        widget=forms.Select(
            attrs={
                'type':'select'
                # 'class': 'form-control'
            }
        )
    )

    price = forms.DecimalField(required=True, min_value=2,
        widget=forms.NumberInput(
            attrs={
                'type': 'number'
            }
        )    
    )

    image = forms.ImageField(required=False,
        widget=forms.FileInput()
    )


class StoreForm(forms.Form):
    name=forms.CharField(required=True, max_length=200, strip=True, min_length=2,
         widget=forms.TextInput(
            attrs={
                'type':'text'
            }
        )
    )

    country = forms.ChoiceField( required=True, choices=[(x, y) for (x, y) in settings.COUNTRIES],
        widget=forms.Select(
            attrs={
                'type':'select'
            }
        )
    )

class ProfilStoreForm(forms.Form):
    email=forms.EmailField(required=True, max_length=100, min_length=5,
         widget=forms.EmailInput(
            attrs={
                'type':'email'
            }
        )
    )

    phone = forms.IntegerField(required=True, max_value=200, min_value=5,
        widget=forms.NumberInput(
            attrs={
                'type':'number'
            }
        )    
    )


# class PersonForms(forms.ModelForm):
#     class Meta:
#         fields('name', 'age')
#         data = data.