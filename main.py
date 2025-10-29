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
for user in users:
    print(f"Twój znajomy {user["name"]} z miejscowości {user["location"]} opublikował {user["posts"]} postów")
