from os import name
from django.urls import path, re_path
from . import views
# from myapp.forms import up

urlpatterns = [
    #Persons
    path('', views.index, name='index'),
    path('updatePerson/<int:pk>/', views.updatePerson, name='update-person'),
    path('add_person', views.add_person, name='add_person'),
    path('delete/<int:pk>/', views.delete_person, name='delete_person'),


    #Products
    re_path(r'^produit/$', views.product, name='product'),
    path('update/<int:pk>/', views.updateProduct, name='update-product'),
    path('add_product', views.add_product, name='add_product'),
    path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),


    #Store
    re_path(r'^magasin/$', views.store, name='store'),
    path('updateStore/<int:pk>/', views.updateStore, name='update-store'),
    path('add_store', views.add_store, name='add_store'),
    path('delete_store/<int:pk>/', views.delete_store, name='delete_store'),

    #Profile Store
    re_path(r'^profilemagasin/$', views.profile, name='profile'),
    path('updateProfile/<int:pk>/', views.updateProfilStore, name='update-profile'),
    path('delete_profileStore/<int:pk>/', views.delete_profileStore, name='delete_profileStore'),
    path('add_profileStore', views.add_profileStore, name='add_profileStore'),
  

    # path('', views.hello, name='index'),
]