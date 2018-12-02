from django.urls import path
from . import views

app_name = 'materials'

urlpatterns = [
    path('', views.index, name='index'),
    # path('search/', views.site.urls),
    # path('materials/<slug:title>/', views.site.urls),
    # path('materials/<slug:title>/recomendations/', views.site.urls),
    # path('materials/<slug:title>/<int:id>/', views.site.urls),
]
