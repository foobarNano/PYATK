from random import randint

cities = ['Warszawa','Kraków','Wrocław','Łódź','Poznań','Gdańsk','Szczecin','Bydgoszcz','Lublin','Białystok']

count = randint(2, 6)

for i in range(0, count):
    index = randint(0, len(cities)-1)
    print(cities.pop(index))
