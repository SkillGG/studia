Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import math
def policz():
    x = input("X: ")
    y = input("Y: ")
    return 2 * pow(x,4) + math.sqrt(y)/x
SyntaxError: multiple statements found while compiling a single statement
import math
def policz():
    x = input("X: ")
    y = input("Y: ")
    return 2 * pow(x,4) + math.sqrt(y)/x
policz()
SyntaxError: invalid syntax
def policz():
    x = input("X: ")
    y = input("Y: ")
    return 2 * pow(x,4) + math.sqrt(y)/x

policz()
X: 12
Y: 5
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    policz()
  File "<pyshell#7>", line 4, in policz
    return 2 * pow(x,4) + math.sqrt(y)/x
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
def policz():
    x = int(input("X: "))
    y = int(input("Y: "))
    return 2 * pow(x,4) + math.sqrt(y)/x

policz()
X: 12
Y: 5
41472.18633899812
policz()
X: 5
Y: 12
1250.6928203230275
## zad 2
def haslo():
    passw = "jajko"
    while(input("Podaj hasło: ") != passw):
        pass
    print("Doskonale!")

    
haslo()
Podaj hasło: asd
Podaj hasło: asdwdw
Podaj hasło: jajko
Doskonale!
# zadanie 3
def f3():
    for i in range(3):
        x = input("Liczba: ")
        print(f"{math.sqrt(x):.3f}")

        
f3()
Liczba: 12
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    f3()
  File "<pyshell#25>", line 4, in f3
    print(f"{math.sqrt(x):.3f}")
TypeError: must be real number, not str
def f3():
    for i in range(3):
        x = int(input("Liczba: "))
        print(f"{math.sqrt(x):.3f}")

        
f3()
Liczba: 12
3.464
Liczba: 32
5.657
Liczba: 5
2.236

# zadanie 4
def f4():
    print("Dzis jest %s, godzina %s", input("Podaj dzien: "), input("Podaj godzine: "))

f4()
Podaj dzien: Wtorek
Podaj godzine: 12:23
Dzis jest %s, godzina %s Wtorek 12:23
def f4():
    print("Dzis jest %s, godzina %s" % (input("Podaj dzien: "), input("Podaj godzine: ")))

    
f4()
Podaj dzien: Czwartek
Podaj godzine: 12:25
Dzis jest Czwartek, godzina 12:25

#zadanie 5
imiona = ["Ala","Alan","Ada","Adam"]
for e,i in enumerate(imiona):
...     print(f"{i} => {e}")
... 
...     
Ala => 0
Alan => 1
Ada => 2
Adam => 3
>>> 
>>> #zad 6
>>> 
>>> def f6():
...     t = input("Tekst: ")
...     l = int(input("Liczba: "))
...     x = 0
...     for i in t:
...         if i == "a":
...             x++
...             
SyntaxError: invalid syntax
>>> def f6():
...     t = input("Tekst: ")
...     l = int(input("Liczba: "))
...     x = 0
...     for i in t:
...         if i == "a":
...             x+=1
...     if x == l:
...         print("Spełnia")
...     else: print("Nie spełnia")
... 
...     
>>> f6()
Tekst: aaa
Liczba: 3
Spełnia
>>> f6()
Tekst: abcd
Liczba: 2
Nie spełnia
