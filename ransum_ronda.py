#!/usr/bin/env python3

import datetime
from datetime import date
from os import sys
import subprocess as sp
from prettytable import PrettyTable

__author__ = "Darmanex"
__version__ = "0.1"


def clear():
    clr = sp.call('clear', shell=True)


class warna:
    START = '\033[92m'
    END = '\033[0m'


today = date.today()
hour = datetime.datetime.now()

# set tanggal, bulan, dan tahun
tbt = today.strftime("%d-%B-%Y")
hr = hour.strftime("%H:%M")

x = PrettyTable()

x.field_names = ["No.", "Nama", "Alamat"]

x.align["No."] = "l"
x.align["Nama"] = "l"
x.align["Alamat"] = "l"

x.add_row([1, "Pakde Karsono", "Kadipaten"])
x.add_row([2, "Pak Kukuh", "Bugisan"])
x.add_row([3, "Sarwadi", "Kadipaten"])
x.add_row([4, "Andiyanto", "Suryowijayan"])
x.add_row([5, "Dedi Eko", "Pakuningratan"])
x.add_row([6, "Rendi", "Kadipatan"])
x.add_row([7, "Edi S", "Bugisan"])
x.add_row([8, "Baskoro", "Bugisan"])
x.add_row([9, "Taufik", "Jogokaryan"])
x.add_row([10, "Maryanta", "Bugisan"])
x.add_row([11, "Ardi", "Kadipaten"])
x.add_row([12, "Tomi", "Jogokaryan"])
x.add_row([13, "Wiwid", "Kadipaten"])
x.add_row([14, "Bu Endang", "Mantrigawen"])
x.add_row([15, "Darman", "Suryowijayan"])
x.add_row([16, "Pak Pungky", "Suryowijayan"])
x.add_row([17, "Novran", "Bugisan"])
x.add_row([18, "Faad", "Suryowijayan"])

def garis_batas():
    print("="*47)


def title():
    garis_batas()
    print(warna.START + "Script untuk mengecek jatah ransum ronda malam" + warna.END)
    garis_batas()

dataJatah = [("Pakde Karsono", ["27, Juni 2019"]),
            ("Pak Kukuh", ["20, Juni 2019"]),
            ("Sarwadi", ["4, Juli 2019"]),
            ("Andiyanto", ["11, Juni 2019"]),
            ("Dedi Eko", ["18, Juli 2019"])]

isValidInput = True
while isValidInput:
    title()
    print(f"Hari ini: {tbt} | Pukul: {hr}")
    print(x.get_string(title="Tabel Nama-nama warga Griya Kembang Putih"))

    for data in dataJatah:
        if data == [1]:
            print("Jatah hari ini adalah: ", data[1])

        pilih = input(
        "Pilih nomor dari daftar nama-nama diatas untuk mengecek jatah ransum [1-18]\natau ketik q untuk keluar: ")

        if pilih == 1:
            print("Menu 1 has been selected")
            # You can add your code or functions here
        elif pilih == 2:
            print("Menu 2 has been selected")
            # You can add your code or functions here
        elif pilih == 3:
            print("Menu 3 has been selected")
            # You can add your code or functions here
        elif pilih == 4:
            print("Menu 4 has been selected")
            # You can add your code or functions here
        elif pilih == 5:
            print("Menu 5 has been selected")
            # You can add your code or functions here
        elif pilih == "q":
            print("[✔] Good bye!")
            sys.exit(0)
        else:
            input("Salah pilih opsi. Tekan enter untuk memilih kembali.")

        isValidInput = False
        clear()

# daftar nama-nama yang ronda
daftar_nama = {
    'Pakde Karsono': 'Kadipaten 11',
    'Pak Kukuh': 'Bugisan 15',
    'Sarwadi': 'Kadipaten 12',
    'Andiyanto': 'Suryowijayan 10',
    'Dedi Eko': 'Pakuningratan 21',
    'Rendi': 'Kadipatan 18',
    'Edi S': 'Bugisan 9',
    'Baskoro': 'BUgisan 19',
    'Taufik': 'Jogokaryan  15',
    'Maryanta': 'Bugisan 27',
    'Ardi': 'Kadipaten 23',
    'Tomi': 'Jogokaryan 9',
    'Wiwid': 'Kadipaten 17',
    'Bu Endang': 'Mantrigawen 27',
    'Darman': 'Suryowijayan 28',
    'Pak Pungky': 'Suryowijayan 19',
    'Novran': 'Bugisan 22',
    'Faad': 'Suryowijayan 25'
}
#  jadwal grup ronda tiap kamis malam
jadwal_ronda = "kamis"

# tanggalan
tanggal = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30
           )
# tiap bulan berapa masing-masing orang dapat jatah ransum
bulan = ('January', 'February', 'March', 'April', 'May', 'June',
         'July', 'August', 'September', 'October', 'November', 'December')


def pilihTanggal():
    inputan = input(int("Pilih tanggalnya: ", tanggal))
    return inputan


class Progs:

    def __init__(self):
        self.masukkan_nama = ""

    def masukkan_nama(self):
        while 1:
            input_nama = str(
                input('ketikkan bulan untuk mengecek jatah ransumnya: '))
            if input_nama == "":
                print("Ops! Retry")
            else:
                print("Hello ", input_nama)
                break
        self.masukkan_nama = input_nama

print(daftar_nama)
