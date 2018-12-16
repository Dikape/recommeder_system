from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login_, name='login'),
    path('profile/', views.profile, name='profile'),
    # path('search/', views.site.urls),
    # path('materials/<slug:title>/', views.site.urls),
    # path('materials/<slug:title>/recomendations/', views.site.urls),
    # path('materials/<slug:title>/<int:id>/', views.site.urls),
]
