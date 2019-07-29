#!/usr/bin/env python3

import datetime
import subprocess as sp

clr = sp.call('clear', shell=True)


class color:
    START = '\033[92m'
    END = '\033[0m'


def title():
    print('='*50)
    print(color.START + "Script untuk mengecek jatah ransum ronda malam" + color.END)
    print('='*50)


hari_ini = datetime.datetime.now()


# daftar nama-nama yang ronda
daftar_nama = {'Pakde Karsono', 'Pak Kukuh', 'Sarwadi', 'Andiyanto', 'Dedi Eko',
               'Rendi', 'Edi S', 'Baskoro', 'Taufik', 'Maryanta', 'Ardi', 'Tomi',
               'Wiwid', 'Bu Endang', 'Darman', 'Pak Pungky', 'Novran', 'Faad'}

#  jadwal grup ronda tiap kamis malam
jadwal_ronda = "kamis"

# tiap bulan berapa masing-masing orang dapat jatah ransum
bulan = ('January', 'February', 'March', 'April', 'May', 'June',
         'July', 'August', 'September', 'October', 'November', 'December')


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
                break  # this will break the loop
            # try:
            #     text = str(input_nama)
            #     print("Terima kasih telah memasukkan namanya gan!", text)
            # except ValueError:
            #     print("Masukkan nama-nama yang telah terdaftar bro!")
        self.masukkan_nama = input_nama


title()

