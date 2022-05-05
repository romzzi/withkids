"""tutorialdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import index, list, details, search, write, result, result_full
from main.views import result_in, result_out, result_free, result_charge
from main.views import result_theme_park, result_building_tower, result_mountain
from main.views import result_historical_site, result_park, result_shopping
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('list/', list, name='list'),
    path('<int:pk>/', details, name='details'),
    path('search/', search, name='search'),
    path('search/<int:pk>/', details, name='search_details'),
    path('write/', write, name='write'),
    path('result/', result, name='result'),
    path('result_full/', result_full, name='result_full'),
    path('result_full/<int:pk>/', details, name='result_full_details'),
    path('result_in/', result_in, name='result_in'),
    path('result_in/<int:pk>/', details, name='result_in_details'),
    path('result_out/', result_out, name='result_out'),
    path('result_out/<int:pk>/', details, name='result_out_details'),
    path('result_free/', result_free, name='result_free'),
    path('result_free/<int:pk>/', details, name='result_free_details'),
    path('result_charge/', result_charge, name='result_charge'),
    path('result_charge/<int:pk>/', details, name='result_charge_details'),
    path('result_theme_park/', result_theme_park, name='result_theme_park'),
    path('result_theme_park/<int:pk>/', details, name='result_theme_park_details'),
    path('result_building_tower/', result_building_tower, name='result_building_tower'),
    path('result_building_tower/<int:pk>/', details, name='result_building_tower_details'),
    path('result_mountain/', result_mountain, name="result_mountain"),
    path('result_mountain/<int:pk>/', details, name='result_mountain_details'),
    path('result_historical_site/', result_historical_site, name="result_historical_site"),
    path('result_historical_site/<int:pk>/', details, name='result_historical_site_details'),
    path('result_park/', result_park, name="result_park"),
    path('result_park/<int:pk>/', details, name='result_park_details'),
    path('result_shopping/', result_shopping, name="result_shopping"),
    path('result_shopping/<int:pk>/', details, name='result_shopping_details'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)