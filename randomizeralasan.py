"""Judul: Randomizer Procrastination
Bahasa: Python 3.7
Tanggal: 28 Mei 2019

Ini program untuk mengecek alasan apa yang akan kamu munculkan 
secara acak ketika sedang procras. Dibuat dengan penuh cinta dan 
kasih sayang oleh seluruh anggota divisi story Genshiken ITB 2018-2019.
66 alasan asli yang ditulis dalam program ini dikumpulkan dalam
rentang waktu hampir 2 bulan oleh anggota divisi story secara kolektif.
Apabila kamu menemukan alasan yang agak konyol, aneh, atau sulit
dimengerti, coba tanyakan langsung di grup Line story. Mungkin ada yang
tahu. Mungkin loh ya.
"""

import random
import time

alasanmu = ["Nanggung masih di kampung", "Nunggu lailatul qadar", 
            "THR lom turun", "Lagi fokus itikaf", "Lagi fokus puasa",
            "Di kampung susah sinyal", "lagi dijodohin sama osanana",
            "Lagi masak opor", "Disuruh bikin kue kering",
            "Disuruh jagain adiknya sepupunya anaknya paman",
            "Lagi ngedanus gorengan di jalan", "Diajakin bukber TK",
            "Deadline mepet bikin kreatif", "Disuruh lulus kuliah dulu", 
            "Buntu", "Mau tawuran pas SOTR", "Main PES19 buat nunggu buka",
            "Lanjutin gamejam", "Ngedit foto Syafrul", "Keasyikan nguli regex",
            "Bikin TA", "Ngoreksi laprak bocah", "Ngejahit celana",
            "Ngerjain tubes", "Menunggu season 2 yang tak kunjung keluar",
            "Masih ijab kabul", "Cucian belum kering", "TTKI",
            "Perang sarung pas tarawih", "Udah mati", 
            "Lagi marathon kamen rider", "Masih mencari bola naga ke-7",
            "Belum dapet final form", "Belum mandi wajib",
            "Lagi di trisakti tanggal 12 Mei",
            "Belum mengembalikan kekaisaran Cina", 
            "Belum menikah dengan macan", "Lho, ada writchal toh. Oooooo~", 
            "Lagi ngitung koefisien Fourier",
            "Mana saya tahu, saya kan maba", "Cuma dapat BC, ga lulus",
            "Nonton spongebob frame by frame di FB",
            "Masih melihat bayangannya di kamarku",
            "Bahkan baru tau ada writchal dari chat panjang ini",
            "Nonton video detektif pikachu joget", 
            "Simulasi webpage 800 ribu halaman",
            "Sibuk ngajuin budget buat opening dua site sekaligus" 
            "\npadahal CEOnya jarang di kantor °^°",
            "Lagi eksplorasi CM3D", "Mau install CM3D tapi kegedean", 
            "mau install CM3D tapi udah punya cewe", "INGIN REBAHAN YA ALLAH", 
            "Ambruk setelah ngoding", "MATHCO (R)", "Mau balik dulu", 
            "Ngedit video detektif pikachu joget", "Menangisi nilai T",
            "Ngejar level battle pass dota",
            "Kebanyakan procras padahal harusnya udah packing aaaaaa",
            "Gak tau spek writchal", "WA IG FB mati",
            "Lagi ngelunasin utang tidur",
            "Lagi ngebudak GBF... YAOLO MUSUH PUSH LAGI",
            "Persiapan pameran Kaliope, datang ya guys"
            "\ntgl 24 jam 1, tgl 25 dari pagi, di altim",
            "Plis jgn push lagi dong.. tinggal 2 jam nih.. mau tidur", 
            "Gaji belum turun", "Nungguin kalkulasi ansys 1 jam belom kelar,"
            "\njadi sambil dengerin dragonforce pake seruling"
            ]

# Untuk menghitung sudah berapa kali kamu main di program ini.
hitung_alasan = []
for i in range(len(alasanmu)):
    hitung_alasan.append(0)

# Untuk menyimpan fakta apakah kamu masih mau procras atau sudah cukup.
lanjut = True

def main():
    # Bagian utama.
    print("Selamat datang di simulator procras.")
    time.sleep(1)
    print("Karena kamu membuka program ini, artinya kamu sedang procras ya...")
    time.sleep(1)
    print("Mau coba keluarkan kemungkinan alasannya?")
    global lanjut
    while lanjut:
        pilih_alasan()
        pass

def pilih_alasan():
    print("Y/y : Oh, boleh.")
    print("N/n : Tidak deh, mau balik kerja aja.")
    cho = str(input("Pilihanmu : "))
    # Kalau masih lanjut.
    if cho.lower() == 'y':
        pengacak()
    # Kalau sudah berhenti.
    elif cho.lower() == 'n':
        pamit()
    # Kalau kamu kebetulan salah ketik.
    else:
        print("\nKamu mabuk?")
        print("Coba tulis antara Y atau N.\n")

def pengacak():
    # Mari gacha....
    alasan = random.choice(alasanmu)
    print("\nAlasan tebakanku adalah...")
    print(alasan)
    global hitung_alasan
    hitung_alasan[alasanmu.index(alasan)] += 1
    # Untuk menambah alasanmu sendiri (kalau beruntung)
    if alasan.lower() == "buntu":
        tambah_alasan()
    if max(hitung_alasan) >= 10 | len(alasanmu) >= 75:
        kelamaan()
    else:
        print("\nMasih mau lanjut procras?")

def tambah_alasan():
    """Kalau kamu beruntung, kamu bisa menambah alasan procras
    kamu sendiri di program ini. Tapi semua alasan tambahan akan
    hilang setelah program ditutup, maaf.
    """
    global alasanmu
    print("Selamat, kamu bisa menambah alasan sendiri!")
    alasan_baru = input("Apa alasan pribadimu? : ")
    alasanmu.append(alasan_baru)

def pamit():
    # Selamat melanjutkan pekerjaan kamu.
    global lanjut
    lanjut = False
    time.sleep(1)
    print("\nWow, kamu sudah berhenti procras.")
    time.sleep(1) 
    print("Oke, selamat bekerja...")
    time.sleep(1)

def kelamaan():
    """Untuk mengembalikan kamu ke kenyataan setelah terlalu lama
    bermain di program ini. Percayalah, ada hal-hal lain dalam hidup
    ini yang sedang menunggu kamu di luar sana.
    """
    global lanjut
    lanjut = False
    time.sleep(1)
    print("\nHei.")
    time.sleep(1)
    print("Kau sudah terlalu lama main di sini.")
    time.sleep(1)
    print("Istirahatlah. Ada hal-hal menyenangkan di luar sana yang menunggumu.")
    time.sleep(1)

# Mulai dari sini ya.
if __name__ == "__main__":
    t_awal = time.time()
    main()
    t_akhir = time.time()
    lama_main = t_akhir - t_awal
    print("\nKamu sudah membuang {} detik untuk procras di program ini."
          .format(lama_main))
