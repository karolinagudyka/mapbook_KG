import requests
from bs4 import BeautifulSoup

users:list = [
    {"name": "Tomek",
     "location": "Warszawa",
     "posts": "50",
     "coord": [52.23 , 21.0],
     "img_url": ""},
    {"name": "Karolina",
     "location": "Kraśnik",
     "posts": "100",
     "img_url": ""},
    {"name": "Jacek",
     "location": "Wrocław",
     "posts": "10",
     "img_url": ""},
]

def user_info(users_data:list)->None:
    for user in users_data:
        print(f"Twój znajomy {user["name"]} z miejscowości {user["location"]} opublikował {user["posts"]} postów")

def add_user(users_data:list)->None:
    name:str = input("Podaj imie nowego znajomego: ")
    location:str = input("Podaj nazwę miejscowości: ")
    posts:int = input("Podaj liczbę postów: ")
    img_url:str = input("Wprowadź adres zdjęcia: ")
    users_data.append({"name":name,"location":location,"posts":posts, "img_url":img_url})

def remove_user(users_data:list)->None:
    tmp_name:str = input("Podaj imię użytkownika do usunięcia: ")
    for user in users_data:
        if user["name"] == tmp_name:
            users.remove(user)

def update_user(users_data:list)->None:
    tmp_name: str = input("Podaj imię użytkownika do aktualizacji: ")
    for user in users_data:
        if user["name"] == tmp_name:
            user["name"] = input("Podaj nowe imię użytkownika: ")
            user["location"] = input("Podaj nową miejscowość: ")
            user["posts"] = input("Podaj nową liczbę postów: ")

def get_cordinates(cityname:str)->list:
    url:str=f'https://pl.wikipedia.org/wiki/{cityname}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/123.0 Safari/537.36'
    }
    response=requests.get(url, headers=headers)
    # print(response.text)
    response_html = BeautifulSoup(response.text, 'html.parser')
    # print(response_html.prettify())

    latitude = float(response_html.select('.latitude')[1].text.replace(',','.'))
    #print(latitude)
    longitude = float(response_html.select('.longitude')[1].text.replace(',','.'))
    #print(longitude)
    return [latitude,longitude]
#print(get_cordinates("Wrocław"))

def get_map(users_data:list)->None:
    import folium
    m = folium.Map(location=[52.23 , 21.0], zoom_start=6)

    for user in users_data:
        folium.Marker(
            location=get_cordinates(user["location"]),
            tooltip="Click me!",
            popup=f"<h4>user: {user['name']}</h4> {user['location']} {user['posts']}, <img src={user['img_url']} alt='1' />",
            icon = folium.Icon(icon='cloud')

        ).add_to(m)

    m.save("notatnik.html")

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
