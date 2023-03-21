from django.shortcuts import render, redirect
from .forms import UserPersonal
from userdjanggo.models import User
from django.contrib import messages
# Create your views here.


def hapus_user(request, id_user):
    user = User.objects.filter(id=id_user)
    user.delete()

    return redirect('lihat_user')


# Untuk Mengubah Data User


def ubah_user(request, id_user):
    usered = User.objects.get(id=id_user)
    template = 'ubah-user.html'

    if request.POST:
        form = UserPersonal(request.POST, instance=usered)
        if form.is_valid():
            form.save()
            messages.success(request, "Data User Berhasil Diubah")
            return redirect('ubah_user', id_user=id_user)
    else:
        form = UserPersonal(instance=usered)
        konteks = {
            'form': form,
            'usered': usered
        }
        return render(request, template, konteks)


def user(request):
    return render(request, 'user.html')


def form_tambah_user(request):
    return render(request, 'formUser.html')

# Untuk Menambah Data User


def tambah_user(request):
    if request.POST:
        form = UserPersonal(request.POST)
        if form.is_valid():
            form.save()
            form = UserPersonal()
            pesan = "Data User Berhasil Disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }

            return render(request, 'formUser.html', konteks)
        else:
            form = UserPersonal()

            konteks = {
                'form': form,
            }

            return render(request, 'formUser.html', konteks)

# Untuk Menampilkan Data User Dari Database


def lihat_user(request):
    usered = User.objects.all()

    konteks = {
        'usered': usered,
    }

    return render(request, 'user.html', konteks)
