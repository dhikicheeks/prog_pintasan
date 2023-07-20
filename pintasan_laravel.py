import os


def laravel(menu, tanya, cls):
    print("\n---------------------------")
    print(" LARAVEL ")
    print("---------------------------")
    print("\nPilih command :")
    print("	1. Serve")
    print("	2. Redis")
    print("	3. Config cls")
    print("	0. Back")

    pilih = input("Masukkan pilihan [1-3] : ")

    if pilih == "1":
        host = input("Masukkan HOST (127.0.0.1) : ")
        port = input("Masukkan PORT (8000) : ")
        command = ""
        if host != "" and port != "":
            command = "php artisan serve --host={} --port={}".format(
                host, port)
        else:
            if host != "" and port == "":
                command = "php artisan serve --host={host}".format(host)
            elif host == "" and port != "":
                command = "php artisan serve --port={port}".format(port)
            else:
                command = "php artisan serve"

        os.system(command)

    elif pilih == "2":
        os.system("redis-server")
    elif pilih == "3":
        os.system("php artisan config:cls")
    elif pilih == "0":
        menu()
    else:
        cls()
        print("\nPilihan yang anda masukkan salah!")
        laravel(menu, tanya, cls)
