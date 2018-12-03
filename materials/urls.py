from django.urls import path
from . import views

app_name = 'materials'

urlpatterns = [
    path('', views.index, name='index'),
    path('materials/<slug:slug>/', views.materials, name='materials'),
    path('materials/<slug:slug>/recommendations/', views.recommendations, name='recommendations'),
    path('materials/<slug:slug>/<int:id>/', views.material_details, name='details'),
]
