#Lista1

from random import randint

'''
UWAGA! Nie należy zmieniać nazw funkcji, oraz wartości zmiennych podanych w pliku
poza wartościami ze stringiem "PODAJ WYNIK" - w tych zmiennych należy przechowywać wynik
dotyczący poszczególnych zadań w_1, w_2 ... w_6.

Ciało funkcji wpisujemy w kodzie zamiast "pass".

Wyniki z każdego zadania powinny wyświetlać się w jednej linijce.
Nie należy wyświetlań nic poza wynikiem działania kodu z poszczególnych zadań
w kolejności tak jak w pliku.
Plik należy zapisać w postaci: imie_nazwisko_lista1.py
'''

#1. Ile unikatowych elementów znajduje się w liście:
#1 pkt
lista_1 = [0,7,8,3,3,0,7,0,3]
lista_1.sort()
count = 1
for i in range(1, len(lista_1)):
    if lista_1[i-1] != lista_1[i]: count += 1
w_1 = count
print(w_1)

#2. Napisz kod, który podmieni losowy znak ze stringa na '0':
#2 pkt
s_2 = "ala ma kota"
index = randint(0, len(s_2)-1)
temp = list(s_2)
temp[index] = '0'
w_2 = "".join(temp)
print(w_2)


#3. Napisz kod który podmieni z lista_3 język programowania R na JS, następnie wyświetl podmieniony JS.
# Przed JS nadal musi znajdować się python w strukturze takiego samego typu jak w przykladowej lista_3.
# 2pkt
lista_3 = [[{1: 'java', 0: ('python', 'R')},'c++'],['word', 'excel']]
temp = (lista_3[0][0][0][0], 'JS')
lista_3[0][0] = temp
w_3 = lista_3[0][0][1]
print(w_3)


#4. Jakiego typu dane z poniższych nie mogą być kluczami słownika?
#boolean,float,int,string,tuple,list,set. Odpowiedź umieśc w stringu w_4
#1 pkt
w_4 = "list,set"
print(w_4)

#5. Dla stringa wypisz
#ile razy pojawił się dany znak, w kolejności alfabetycznej.
#Użyj słownika - wynik również ma być słownikiem.
#Sprawdzamy tylko te znaki, które występują w podanym stringu.
#2 pkt
s_5 = "ala ma kota imie ma macko"
s_list = list(s_5)
s_list.sort()

s_dict = dict()
for s in s_list:
    if s_dict.get(s) == None: s_dict[s] = 1
    else: s_dict[s] += 1
w_5 = s_dict
print(w_5)

#6. Napisz kod który sprawdzi, czy w poprzednim stringu s_5,
#jakikolwiek znak wystąpił dokładnie 3 razy. Wyświetl Tak jeżeli wystąpił,
#Nie jeżeli nie wystąpił.
#1 pkt
result = 'Nie'
for s in s_dict:
    if s_dict[s] == 3: result = 'Tak'
w_6 = result
print(w_6)

#7. Napisz funkcję sprawdzającą czy podane słowa/zdania są palindromem
#i zwróci True lub False ( jest/ nie jest).
#Pomiń znaki nie będące literami, wielkość liter nie ma znaczenia
#3pkt

def palindrom(s):
    s_alpha = list()
    for c in s:
        if c.isalpha(): s_alpha.append(c.lower())
    
    length = len(s_alpha)
    for i in range(0, (int)((length+1)/2)):
        if s_alpha[i] != s_alpha[length-1-i]: return False
    return True

s_7_1 ="Nowy Targ, góry, Zakopane – na pokazy róg, graty won"
print(palindrom(s_7_1))


#8. Napisz funkcję, która zwróci
#wszystkie liczby od 1 do n w jednym stringu rozdzielone przecinkami, 
#jednak jeżeli liczba jest podzielna przez:
#trzy – zamiast liczby mamy „Fizz”,
#pięć – zamiast liczby mamy „Buzz”,
#trzy i pięć zamiast liczby mamy „FizzBuzz”.
#wszystkie liczby/słowa mają zostać zwróćone w jednej linii, oraz być rozdzielone przecinkiem
#BEZ spacji
#2 pkt

def fizzbuzz(n):
    by_3 = n%3 == 0
    by_5 = n%5 == 0

    if by_3 and by_5: return "FizzBuzz"
    if by_3: return "Fizz"
    if by_5: return "Buzz"

    return ",".join([str(i) for i in range(1, n)])

n_8 = 16
print(fizzbuzz(n_8))

#9. Napisz funkcję zwracającą n-ty element ciągu Fibonacciego
# przy F(0)= 0 i F(1) = 1.
#bez rekurencji:
#3 pkt
n_9 = 6
def fibonacci(n):
    if n < 2: return n

    fib_list = [0, 1]
    for i in range(2, n+1):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    return fib_list[n]
    
print(fibonacci(n_9))

#10. Napisz funkcję, która dla podanej posortowanej listy
#zwróci index wyszukiwanego elementu za pomocą wyszkukiwania binarnego,
#lub zwróci None gdy nie ma elementu w liscie:
#3 pkt
def binary_search(lista, e):
    index = (int)((len(lista)+1)/2)
    
    if lista[index] == e: return index
    if lista[index] > e: return binary_search(lista[:index], e)
    if lista[index] < e: return binary_search(lista[index+1:], e)

l_10 = [0,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768]
print(binary_search(l_10, 2))