"""abastos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^sell/', include('sell.urls')),
    url(r'^$', views.homepage),
    url(r'^homepage/', views.homepage, name="homepage"),
    url(r'^byproduct/(?P<slug>[\w-]+)/$', views.byproduct, name="byproduct"),
    url(r'^products/', include('products.urls')),
    url(r'^locations/', include('locations.urls')),
    url(r'^myMessages/', include('myMessages.urls'))
]

urlpatterns+=staticfiles_urlpatterns()
