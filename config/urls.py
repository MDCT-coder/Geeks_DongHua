"""Geeks_DongHua URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static

from config import settings
from config.router import router
from home import index
from fix.views import fix

urlpatterns = [
    url(r'^admin/+', admin.site.urls),

    url(r'^api/', include(router.urls, namespace='rest_framework')),

    url(r'^$', index, name='index'),
    url(r'fix/$', fix),
    url(r'user/', include('myuser.urls', namespace='myuser')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
