import os


def flutter(menu, tanya, clear):
    print("\n---------------------------")
    print(" FLUTTER ")
    print("---------------------------")
    print("\nPilih command :")
    print("	1. Pub Get")
    print("	2. Build Runner")
    print("	3. Build AAB")
    print("	4. Build APK")
    print("	5. Build APK Split")
    print("	0. Back")

    pilih = input("Masukkan pilihan [1-3] : ")

    if pilih == "1":
        os.system("flutter pub get")

    elif pilih == "2":
        os.system("flutter pub run build_runner build --delete-conflicting-outputs")

    elif pilih == "3":
        os.system("flutter build appbundle")

    elif pilih == "4":
        os.system("flutter build apk")

    elif pilih == "5":
        os.system("flutter build apk --split-per-abi")

    elif pilih == "0":
        menu()

    else:
        clear()
        print("\nPilihan yang anda masukkan salah!")
        flutter(menu, tanya, clear)
