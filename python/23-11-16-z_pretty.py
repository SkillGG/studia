Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import math
def zad1():
    x = int(input("X: "))
    y = int(input("Y: "))
    return 2 * (x**4) + math.sqrt(y)/x

zad1()
X: 12
Y: 15
41472.32274861218


#zad 2
def zad2():
    passw = "jajko"
    while(input("Podaj hasło: ") != passw):
        pass
    print("Doskonale!")

    
zad2()
Podaj hasło: asd
Podaj hasło: asd
Podaj hasło: jajko
Doskonale!


#zad 3
def zad3():
    for i in range(3):
        x = int(input("Liczba: "))
        print(f"{math.sqrt(x):.3f}")

        
zad3()
Liczba: 12
3.464
Liczba: 4
2.000
Liczba: 23
4.796


# zad 4
def zad4():
    print("Dzis jest %s, godzina %s" % (input("Podaj dzien: "), input("Podaj godzine: ")))

    
>>> zad4()
Podaj dzien: Czwartek
Podaj godzine: 12:30
Dzis jest Czwartek, godzina 12:30
>>> 
>>> 
>>> #zad 5
>>> imiona = ["Ala","Alan","Ada","Adam"]
>>> for i,e in enumerate(imiona):
...     print(f"{i} => {e}")
... 
...     
0 => Ala
1 => Alan
2 => Ada
3 => Adam
>>> 
>>> 
>>> #zad 6
>>> def zad6():
...     text = input("Tekst: ")
...     liczba = int(input("Liczba: "))
...     if text.count("a") >= liczba:
...         print("Spełnia")
...     else: print("Nie spełnia")
... 
...     
>>> zad6()
Tekst: aabc
Liczba: 1
Nie spełnia
>>> zad6()
Tekst: aabc
Liczba: 2
Spełnia
