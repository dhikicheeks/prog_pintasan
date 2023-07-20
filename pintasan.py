#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3

import os
import sys
from pintasan_flutter import flutter
from pintasan_laravel import laravel
from pintasan_nodejs import nodejs
from pintasan_reactnative import reactnative
from sys import platform

def menu():
    cls()
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
        cls()
        flutter(menu, tanya, cls)
    elif pilih == "2":
        cls()
        laravel(menu, tanya, cls)
    elif pilih == "3":
        cls()
        nodejs(menu, tanya, cls)
    elif pilih == "4":
        cls()
        reactnative(menu, tanya, cls)
    elif pilih == "0":
        cls()
        print("Terima kasih sudah menggunakan aplikasi ini!")
        sys.exit()
    else:
        cls()
        print("\nPilihan yang anda masukkan salah!")
        menu()


def tanya():
    cls()
    print("\n-----------------------------------------")
    tanya = input(" Ingin mengulang aplikasi lagi? [y/t] : ")
    print("-----------------------------------------")
    if tanya == "y":
        menu()
    elif tanya == "t":
        sys.exit()
    else:
        print("Pilihan yang anda masukan salah!")


def cls():
    if platform == "darwin":
        os.system('clear')
        # OS X
    elif platform == "win32":
        # Windows...
        os.system('cls')


menu()
