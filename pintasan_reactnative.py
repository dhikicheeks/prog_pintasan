import os


def reactnative(menu, tanya, clear):
    print("\n---------------------------")
    print(" React Native ")
    print("---------------------------")
    print("\nPilih command :")
    print("	1. Run Expo")
    print("	2. Doctor")
    print("	9. Create Project")
    print("	0. Back")

    pilih = input("Masukkan pilihan [1-2] : ")

    if pilih == "1":
        os.system("npx expo start")
    elif pilih == "2":
        os.system("npx react-native doctor")
    elif pilih == "9":
        name = input("Masukkan Nama Project : ")
        command = "npx create-expo-app {}".format(name)
        os.system(command)
    elif pilih == "0":
        menu()
    else:
        clear()
        print("\nPilihan yang anda masukkan salah!")
        reactnative(menu, tanya, clear)
