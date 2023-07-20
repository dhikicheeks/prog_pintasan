#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3

import os
import sys
from pintasan_flutter import flutter
from pintasan_laravel import laravel
from pintasan_nodejs import nodejs
from pintasan_reactnative import reactnative


def menu():
    clear()
    print("\n---------------------------")
    print(" MAIN MENU PINTASAN ")
    print("---------------------------")
    print("\nPilih Framework :")
    print("	1. FLUTTER")
    print("	2. LARAVEL")
    print("	3. NODE JS")
    print("	4. REACT NATIVE")
    print("	0. Exit")

    pilih = input("Masukkan pilihan [1-4] : ")

    if pilih == "1":
        clear()
        flutter(menu, tanya, clear)
    elif pilih == "2":
        clear()
        laravel(menu, tanya, clear)
    elif pilih == "3":
        clear()
        nodejs(menu, tanya, clear)
    elif pilih == "4":
        clear()
        reactnative(menu, tanya, clear)
    elif pilih == "0":
        clear()
        print("Terima kasih sudah menggunakan aplikasi ini!")
        sys.exit()
    else:
        clear()
        print("\nPilihan yang anda masukkan salah!")
        menu()


def tanya():
    clear()
    print("\n-----------------------------------------")
    tanya = input(" Ingin mengulang aplikasi lagi? [y/t] : ")
    print("-----------------------------------------")
    if tanya == "y":
        menu()
    elif tanya == "t":
        sys.exit()
    else:
        print("Pilihan yang anda masukan salah!")


def clear():
    os.system('clear')


menu()
