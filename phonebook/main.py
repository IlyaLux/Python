import readfile

if __name__ == "__main__":
    readfile.main_menu()

    while True:
        choose = int(input("Введите пункт меню: "))
        if choose == 1:
            readfile.show_all()
        if choose == 2:
            readfile.add_contakt()
        if choose == 3:
            readfile.edit_contakt()
        if choose == 4:
            readfile.find_contakt()
        if choose == 5:
            readfile.del_contakt()
        if choose == 6:
            readfile.main_menu()