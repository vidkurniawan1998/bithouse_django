"""userdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from userdjanggo.views import form_tambah_user, tambah_user, lihat_user, ubah_user, hapus_user


urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/user', form_tambah_user, name='form_tambah_user'),
    path('form/user/process', tambah_user),
    path('user/', lihat_user, name='lihat_user'),
    path('user/ubah/<int:id_user>', ubah_user, name='ubah_user'),
    path('user/hapus/<int:id_user>', hapus_user, name='hapus_user')
]
