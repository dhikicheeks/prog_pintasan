import os


def nodejs(menu, tanya, clear):
    print("\n---------------------------")
    print(" NODE JS ")
    print("---------------------------")
    print("\nPilih command :")
    print("	1. Npm Run Dev")
    print("	0. Back")

    pilih = input("Masukkan pilihan [1-2] : ")

    if pilih == "1":
        os.system("npm run dev")
    elif pilih == "0":
        menu()
    else:
        clear()
        print("\nPilihan yang anda masukkan salah!")
        nodejs(menu, tanya, clear)
