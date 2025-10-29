users:list = [
    {"name": "Karolina",
     "location": "Kraśnik",
     "posts": "100" },
    {"name": "Tomek",
     "location": "Warszawa",
     "posts": "50" },
    { "name": "Jacek",
      "location": "Londyn",
      "posts": "10" },
]

def user_info(users_data:list)->None:
    for user in users_data:
        print(f"Twój znajomy {user["name"]} z miejscowości {user["location"]} opublikował {user["posts"]} postów")

def add_user(users_data:list)->None:
    name:str = input("Podaj imie nowego znajomego: ")
    location:str = input("Podaj nazwę miejscowości: ")
    posts:int = input("Podaj liczbę postów: ")
    users_data.append({"name":name,"location":location,"posts":posts})

while True:
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
    if tmp_choice==4:
        print("Wybrano funkcję aktualizacji danych znajomego")

