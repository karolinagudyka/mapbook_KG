from mapbook_lib.controller import user_info, add_user, remove_user, update_user, get_map
from mapbook_lib.model import users

def main():
    while True:
        print("============================MENU=================================")
        print("0. Wyjście z programu")
        print("1. Wyświetlanie aktywności znajomych")
        print("2. Dodawanie znajomego")
        print("3. Usuwanie znajomego")
        print("4. Aktualizacja danych znajomych")
        print("5. Generowanie mapy")
        print("=================================================================")
        tmp_choice:int=int(input("Wybierz opcję menu: "))
        if tmp_choice==0:
            break
        if tmp_choice==1:
            print("Wybrano funkcję wyświetlania aktywności znajomych")
            user_info(users)
        if tmp_choice==2:
            print("Wybrano funkcję dodawania znajomego")
            add_user(users)
            print(users)
        if tmp_choice==3:
            print("Wybrano funkcję usuwania znajomego")
            remove_user(users)
            print(users)
        if tmp_choice==4:
            print("Wybrano funkcję aktualizacji danych znajomego")
            update_user(users)
            print(users)
        if tmp_choice==5:
            print("Wybrano funkcję wyświetlania mapy")
            get_map(users)

if __name__ == "__main__":
    main()