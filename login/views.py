from django.shortcuts import render, redirect
from login.form import FormTambahUser
from login.models import user
from django.contrib import messages

def hapus_user(request, id_user):
    User = user.objects.filter(id=id_user)
    User.delete()
    messages.success(request,"Data Berhasil Dihapus")
    return redirect('data')

def ubah_user(request, id_user):
    User = user.objects.get(id=id_user)
    template = 'ubah_data.html'
    if request.POST:
        form = FormTambahUser(request.POST, instance=User)
        if form.is_valid():
            form.save()
            messages.success(request,"Data berhasil diubah")
            return redirect(ubah_user, id_user)             
    else:
        form = FormTambahUser(instance=User)
        konteks = {
            'form' : form,
            'user' : User,
        }
    return render(request,template,konteks)

def login(request):
    return render(request,'index.html')

def tambah_user(request):
    if request.POST:
        form = FormTambahUser(request.POST)
        if form.is_valid():
            form.save()
            form = FormTambahUser()
            pesan = "Data berhasil disimpan"
            konteks = {
                'form' : form,
                'pesan' : pesan
            }
            return render(request, 'tambah-user.html', konteks)
    else:
        form = FormTambahUser()
        konteks = {
            'form' : form,
        }
    return render(request,'tambah-user.html',konteks)

def tampil_user(request):
    users = user.objects.filter()[:10]
    konteks={
        'users' : users,
    }
    return render(request,'data.html',konteks)