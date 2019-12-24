from View.input_nilai import inputan, edit, delett
from View.view_nilai import kosong, ccetak, ccari

while True:
    print("╔═════════════════════════════════════════════════════════════════════════╗")
    print("╠═════════════════   PROGRAM DAFTAR NILAI MAHASISWA   ════════════════════╣")
    print("╠═══════════╦════════════╦════════════╦═════════════╦══════════╦══════════╣")
    print("║ T)ambah   ║   (E)dit   ║  H)apus    ║    C)ari    ║  L)ihat  ║ K)eluar  ║")
    print("╚═══════════╩════════════╩════════════╩═════════════╩══════════╩══════════╝")
    c=input('Pilih menu yang tersedia dengah huruf depan : ')

    #Keluar
    if c.lower() == 'k':
        break

    # Lihat data
    elif c.lower() == 'l':
        ccetak()

    # Menambah Data
    elif c.lower() == 't':
        inputan()

    # Edit Data
    elif c.lower() == 'e':
        edit()

    # Cari Data
    elif c.lower() == 'c':
        ccari()

    # Hapus Data
    elif c.lower() == 'h':
        delett()

    else:
        kosong()
