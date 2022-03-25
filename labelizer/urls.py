"""labelizer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from logic import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('label/',views.next),
    path('',views.load,name='load'),
    path('read/',views.read_csv,name='read'),
    path('prec/',views.prec,name='prev'),
    path('label_it/<str:label>/',views.label,name='label'),
    path('next/',views.next,name='next'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
