# lista = ['wyraz', 3, 5.6, 32, [4, 5, 6]]
# print(lista)
#
# lista.append(5)
# lista.append('12')
# print(lista)
#
# lista.insert(3, 4.75)
# lista.insert(10, 14)
# print(lista)
#
# lista.pop(2)
# print(lista)
#
# lista.remove(32)
# print(lista)
#
# del lista[5]
# print(lista)
#
# lista.extend((2, 2, 'n'))
# print(lista)
#
# lista.reverse()
# print(lista)
#
# nowa_lista = [4, 1.2, 5, 7, 2, 3, 1.78]
# nowa_lista.sort()
# print(nowa_lista)

# slownik = {1: 22, "s": "a", 4.5: 10, 1:23}
# print(slownik)
#
# slownik['6'] = 1.1
# print(slownik)
#
# print(slownik[4.5])
#
# slownik.pop(4.5)
# print(slownik)
#
# print(slownik.keys())
#
# print(slownik.values())
#
# del slownik["s"]
# print(slownik)

# liczba = input("Wprowadz dowolną liczbe: ")
# print(liczba)
# print(type(liczba))
# liczba = int(liczba)
# print(liczba)
# print(type(liczba))

# import sys as system
#
# system.stdout.write("wpisz jaką litere: ")
# napis = system.stdin.readline()
# system.stdout.write(napis)

# Zadanie 1 #
zadanie1= "Zadanie 1"
print(zadanie1)

lista = ["piłka nożna", "koszykówka", "siatkówka"]
lista.insert(3,'hokey')
print(lista)

znakiod = "----------------------------------------------"
print(znakiod)

# Zadanie 2 #

zadanie2= "Zadanie 2"
print(zadanie2)

slownik={'itp.':'i tym podobne','wg.':'wedlug','tzn.':'to znaczy'}

print(slownik)

znakiod = "----------------------------------------------"
print(znakiod)

# Zadanie 3 #

zadanie3= "Zadanie 3"
print(zadanie3)

slownik2={'Call of Duty':'Ghost','World of Warcraft':'MMORPG','Mario':'Klasyk'}
print(slownik2)

znakiod = "----------------------------------------------"
print(znakiod)

# Zadanie 4 #

zadanie4= "Zadanie 4"
print(zadanie4)

zdanie=input('Podaj zdanie: ')
print(zdanie)
print(zdanie.count("a"))

znakiod = "----------------------------------------------"
print(znakiod)

# Zadanie 5 #

zadanie5= "Zadanie 5"
print(zadanie5)

import sys as system

system.stdout.write("Podaj 3 liczby calkowite: ")
zad5_1 = int(system.stdin.readline())
zad5_2 = int(system.stdin.readline())
zad5_3 = int(system.stdin.readline())
print((pow(zad5_1, zad5_2) + zad5_3))

znakiod = "----------------------------------------------"
print(znakiod)

# Zadanie 6 #

zadanie6= "Zadanie 6"
print(zadanie6)

liczba1 = input("Podaj 1 z 3 liczb: ")
liczba2 = input("Podaj 2 z 3 liczb: ")
liczba3 = input("Podaj 3 z 3 liczb: ")

if liczba1 > liczba2:
    if liczba1 > liczba3:
        najwieksza = liczba1
        print(najwieksza)
    else:
        najwieksza = liczba3
        print(najwieksza)
elif liczba2 > liczba3:
    najwieksza = liczba2
    print(najwieksza)
else:
    najwieksza = liczba3
    print(najwieksza)

znakiod = "----------------------------------------------"
print(znakiod)

# Zadanie 7 #

zadanie7= "Zadanie 7"
print(zadanie7)

lista_liczb = [1,2.5,5,4,5]

for x in lista_liczb:
    print(x**2)

znakiod = "----------------------------------------------"
print(znakiod)

# Zadanie 8 #

zadanie8= "Zadanie 8"
print(zadanie8)

lista_zad8 = []

i = 1
while i < 11:
    zad8 = int(input('Podaj liczbe: '))
    i+=1
    if zad8%2==0:
        lista_zad8.append(zad8)
print(lista_zad8)

znakiod = "----------------------------------------------"
print(znakiod)

# Zadanie 9 #

zadanie9= "Zadanie 9"
print(zadanie9)



# Zadanie 10 #

zadanie10= "Zadanie 10"
print(zadanie10)

import math
zad10 = float(input('Podaj liczbe: '))
print(math.sqrt(zad10))


