"""chalearnweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.urls import include, re_path, path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from .users import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include("chalearnlap.users.urls")),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'file/upload/', views.file_upload, name = 'jfu_file_upload' ),
    re_path(r'image/upload/', views.image_upload, name = 'jfu_image_upload' ),
    re_path(r"^search/", include("watson.urls", namespace="watson")),
    re_path(r'^$', views.home, name="home"),
    path('', include('django_prometheus.urls')),
]

handler404 = 'chalearnlap.users.views.handler404'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
