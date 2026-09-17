from django.urls import path
from . import views

urlpatterns =[
    path('',views.inicio),
    path('',views.listar_livros, name='listar')
]