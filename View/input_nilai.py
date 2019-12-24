def inputan():
    from Model.daftar_nilai import tambah_kontak
    while (True):
        nama = input ("NAMA       : ")
        if nama == '':
            print('Nama Harus Di isi')
        else:
            break
    while (True):
        try:
            nim = int(input("NIM        : "))
            if nim == '':
                print("Masukkan NIM dengan Angka")
        except ValueError:
            print("Masukkan NIM dengan Angka")
        else:
            break
    while (True):
        try:
            tugas = int(input("TUGAS      : "))
            if tugas == '':
                print("Masukkan TUGAS dengan Angka")
        except ValueError:
            print("Masukkan TUGAS dengan Angka")
        else:
            break
    while (True):
        try:
            uts = int(input("UTS        : "))
            if uts == '':
                print("Masukkan UTS dengan Angka")
        except ValueError:
            print("Masukkan UTS dengan Angka")
        else:
            break
    while (True):
        try:
            uas = int(input("UAS        : "))
            if uas == '':
                print("Masukkan UAS dengan Angka")
        except ValueError:
            print("Masukkan UAS dengan Angka")
        else:
            break
    tambah_kontak(nama, nim, tugas, uts, uas)

def edit():
    from Model.daftar_nilai import edit_kontak
    edit_kontak(nama=input("Masukkan nama yang akan diubah : "))

def delett():
    from Model.daftar_nilai import delet
    delet(nama=input("Masukkan Nama yang akan dihapus : "))

def find():
    from Model.daftar_nilai import cari
    cari(nama=input("Masukkan Nama yang akan dicari : "))