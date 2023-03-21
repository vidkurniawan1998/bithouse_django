from django.db import models


class User(models.Model):
    nama_lengkap = models.CharField(max_length=200)
    asal_daerah = models.CharField(max_length=200)
    jenis_kelamin = models.CharField(max_length=200)
    alamat = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    class Meta:
        db_table = 'userdjanggo_user'
