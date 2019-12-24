kontak = {}

def tambah_kontak(nama,nim,tugas,uts,uas):
    akhir=round((float(tugas)*0.3) + (float(uts)*0.3) + (float(uas) * 0.35), 2)
    kontak[nama] = nama,nim,tugas,uts,uas,akhir

def edit_kontak(nama):
    if nama in kontak.keys():
        del kontak[nama]
        print ("\nUBAH DATA MAHASISWA ")
        from View.input_nilai import inputan
        inputan()
    else:
        print("Data {} tidak ada ".format(nama))

def cari(nama):
    if nama in kontak.keys():
        print("\n╔════════════════════════════════════════════════════════════════════╗")
        print("╠═══════════════════ DATA MAHASISWA YANG DICARI ═════════════════════╣")
        print("╠═════════════════╦══════════════════╦═══════╦═══════╦═══════╦═══════╣")
        print("║      NAMA       ║       NIM        ║ TUGAS ║  UTS  ║  UAS  ║ AKHIR ║")
        print("╠═════════════════╬══════════════════╬═══════╬═══════╬═══════╬═══════╣")
        no = 1
        for tabel in kontak.values():
            print("║ {0:15} ║ {1:16} ║ {2:5} ║ {3:5} ║ {4:5} ║ {5:5} ║"
                  .format(nama, kontak[nama][1],kontak[nama][2], kontak[nama][3],kontak[nama][4], kontak[nama][5]))
        print("╚═════════════════╩══════════════════╩═══════╩═══════╩═══════╩═══════╝")
    else:
        print("Data {0} tidak ditemukan".format(nama))

def delet(nama):
    if nama in kontak.keys():
        del kontak[nama]
        return True
    else:
        print("Data {0} tidak ditemukan".format(nama))

    return False