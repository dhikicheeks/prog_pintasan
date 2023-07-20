import os


def nodejs(menu, tanya, cls):
    print("\n---------------------------")
    print(" NODE JS ")
    print("---------------------------")
    print("\nPilih command :")
    print("	1. Npm Run Dev")
    print("	11. Create Project Node.js")
    print("	0. Back")

    pilih = input("Masukkan pilihan [1-2] : ")

    if pilih == "1":
        os.system("npm run dev")
    elif pilih == "11":
        name = input("Masukkan Nama Project : ")
        
        
        command_change = "cd\  && e: && cd Apps\laragon\www && md {} && cd {} && npm install express-generator -g && express && npm install && code .".format(name, name)
        os.system(command_change)
        
        
        # command = "md {}".format(name)
        # command1 =  "cd {}".format(name)
        # command2 = "npm install express-generator -g"
        # command3 = "express {}".format(name)
        # command4 = "code ."
        # os.system(command)
        # os.system(command1)
        # os.system(command4)
        # os.system(command2)
        # os.system(command3)
    elif pilih == "0":
        menu()
    else:
        cls()
        print("\nPilihan yang anda masukkan salah!")
        nodejs(menu, tanya, cls)
