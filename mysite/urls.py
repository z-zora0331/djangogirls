"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, re_path, include
from django.contrib import admin

from device.views import deviceView

admin.autodiscover()
# 讓r'^admin/'，對應到include(admin.site.urls) 

urlpatterns = [
    # url(regex, view)
    
    # Local test
    re_path(r'^admin/', admin.site.urls, name='admin'),
    # 原: path('admin/', admin.site.urls),
    re_path(r'', include('blog.urls')),
    
    # 台南數據中心
    path('iot/v1/device/', deviceView.get),
    path('device/id/', deviceView.getId),
    path('device/post/', deviceView.post),
]