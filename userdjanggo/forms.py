from django import forms
from .models import User


class UserPersonal(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        error_messages = {
            'nama_lengkap': {
                'required': 'Anda Harus Mengisi Form Nama Lengkap'
            },
            'asal_daerah': {
                'required': 'Anda Harus Mengisi Form Asal Daerah'
            },
            'jenis_kelamin': {
                'required': 'Anda Harus Mengisi Form Jenis Kelamin'
            },
            'alamat': {
                'required': 'Anda Harus Mengisi Form Alamat'
            },
            'username': {
                'required': 'Anda Harus Mengisi Form Username'
            },
            'password': {
                'required': 'Anda Harus Mengisi Form Password'
            }
        }
