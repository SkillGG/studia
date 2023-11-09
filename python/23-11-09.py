Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
dok = input("Dokad: ")
Dokad: Warsaw
kie = input("Kiedy: ")
Kiedy: Friday
print("You are going to "+dok+" on "+kie)
You are going to Warsaw on Friday
for i in range(0,int(print("Liczba: ")))
SyntaxError: expected ':'
for i in range(0,int(print("Liczba: "))):
    print(i)

    
Liczba: 
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    for i in range(0,int(print("Liczba: "))):
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'
for i in range(0,int(print("Liczba: "))):
    print(i)

    
Liczba: 
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    for i in range(0,int(print("Liczba: "))):
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'
for i in range(0,int(input("Liczba"))):
    print(i)

    
Liczba12
0
1
2
3
4
5
6
7
8
9
10
11
for i in range(0,10):
    print(i**2)

    
0
1
4
9
16
25
36
49
64
81
for i in range(10,16):
    print(i*2)

    
20
22
24
26
28
30
def AN():
    name = input("Imie: ")
    print(name)

    
AN()
Imie: Marcin
Marcin
Name: amrcin
amrcin
i
15
Name: adam
Hello adam!
AskName()
Name: adam
Hello adam!
def AskName():
    print("u")

    
AskName()
u
AskName()
Name: adam
Hello adam!
4/3
1.3333333333333333
_
1.3333333333333333
round(_,2)
1.33
def sp():
    l = int(input("L: "))
    if l > 10:
        print(str(i) + " jest > 10")
    elif x < 0:
        print(str(i) + "jest < 0")
    else:
        print(str(i) + "jest z przedzialu <0,10>")

        
sp()
L: 12
15 jest > 10
sp()
L: 12
15 jest > 10
def sp():
    l = int(input("L: "))
    if l > 10:
        print(str(l) + " jest > 10")
    elif l < 0:
        print(str(l) + "jest < 0")
    else:
        print(str(l) + "jest z przedzialu <0,10>")

        
sp()
L: 12
12 jest > 10
sp()
L: 0
0jest z przedzialu <0,10>
sp()
L: -12
-12jest < 0
def sp():
    l = int(input("L: "))
    if l > 10:
        print(str(l) + " jest > 10")
    elif l < 0:
        print(str(l) + " jest < 0")
    else:
        print(str(l) + " jest z przedzialu <0,10>")

        
sp()
L: -12
-12 jest < 0
3
3

def sp2():
    l = int(input("L: "))
    if l > 10:
        print(str(l) + " jest > 10")
    elif l < 0:
        print(str(l) + " jest < 0")
    elif l == 0:
        print("Cya!")
        exit()
    else:
        print(str(l) + " jest z przedzialu <0,10>")

        
sp2()
L: 12
12 jest > 10
sp2()
L: 0
Cya!
def sp2():
    l = int(input("L: "))
    if l > 10:
        print(str(l) + " jest > 10")
    elif l < 0:
        print(str(l) + " jest < 0")
    elif l == 0:
        print("Cya!")
        exit()
    else:
        print(str(l) + " jest z przedzialu (0,10>")

        
sp2()
L: 0.1
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    sp2()
  File "<pyshell#60>", line 2, in sp2
    l = int(input("L: "))
ValueError: invalid literal for int() with base 10: '0.1'
def sp2():
    l = int(input("L: "))
    if l > 10:
        print(str(l) + " jest > 10")
    elif l < 0:
        print(str(l) + " jest < 0")
    elif l == 0:
        print("Cya!")
        exit()
    else:
        print(str(l) + " jest z przedzialu (0,10>")

        
t=""
while t!= "e":
    text = input("T: ")

    
T: a
T: b
T: c
T: d
T: f
T: asdasd
T: e
T: e
T: e
T: e
T: e
T: e
T: e
T: e
T: e
T: e
T: e
T: e
T: e
T: e
T: 
Traceback (most recent call last):
  File "<pyshell#67>", line 2, in <module>
    text = input("T: ")
KeyboardInterrupt
while t!= "e":
    t = input("T: ")

    
T: a
T: b
T: c
T: d
T: e
while t!= "e":
    t = input("T: ")

    
suma = 0
while suma < 100:
    suma += int(input("Liczba do dodania: "))
    print("Suma: " + str(suma))
else:
    suma = 0

    
Liczba do dodania: 5
Suma: 5
Liczba do dodania: 200
Suma: 205
while suma < 100:
    suma += int(input("Liczba do dodania: "))
    print("Suma: " + str(suma))
else:
    suma = 0

    
Liczba do dodania: 100
Suma: 100
while suma < 100:
    suma += int(input("Liczba do dodania: "))
    print("Suma: " + str(suma))
else:
    suma = 0

    
Liczba do dodania: 15
Suma: 15
Liczba do dodania: 20
Suma: 35
Liczba do dodania: 25
Suma: 60
Liczba do dodania: 30
Suma: 90
Liczba do dodania: 30
Suma: 120
while suma < 100:
    suma += int(input("Liczba do dodania: "))
    print("Suma: ",suma)
else:
    suma = 0

    
Liczba do dodania: 1
Suma:  1
Liczba do dodania: 2
Suma:  3
Liczba do dodania: 3
Suma:  6
Liczba do dodania: 4
Suma:  10
Liczba do dodania: 5
Suma:  15
Liczba do dodania: 6
Suma:  21
Liczba do dodania: 7
Suma:  28
Liczba do dodania: 8
Suma:  36
Liczba do dodania: 9
Suma:  45
Liczba do dodania: 10
Suma:  55
Liczba do dodania: 11
Suma:  66
Liczba do dodania: 12
Suma:  78
Liczba do dodania: 13
Suma:  91
Liczba do dodania: 14
Suma:  105
def dod():
    suma = 0
    x = 1
    while x != 0:
        x = int(input("Liczba: "))
        suma += x
    print("suma: ", suma)

    
dod()
Liczba: 1
Liczba: 2
Liczba: 3
Liczba: 4
Liczba: 5
Liczba: 20
Liczba: 0
suma:  35
def dod():
    suma = 0
    x = 1
    while x != 0:
        x = int(input("Liczba (exit - 0): "))
        suma += x
    print("suma: ", suma)

    
dod()
Liczba (exit - 0): 
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    dod()
  File "<pyshell#95>", line 5, in dod
    x = int(input("Liczba (exit - 0): "))
KeyboardInterrupt
def dod():
    suma = 0
    x = 1
    while x != 0:
        x = int(input("Liczba (exit - 0): "))
        suma += x
        print("Suma: ", suma)

        
dod()
Liczba (exit - 0): 1
Suma:  1
Liczba (exit - 0): 12
Suma:  13
Liczba (exit - 0): 24
Suma:  37
Liczba (exit - 0): 32
Suma:  69
Liczba (exit - 0): 23
Suma:  92
Liczba (exit - 0): 123
Suma:  215
Liczba (exit - 0): 123
Suma:  338
Liczba (exit - 0): 0
Suma:  338
def dod():
    suma = 0
    while x != 0:
        x = int(input("Liczba (exit - 0): "))
        suma += x
        print("Suma: ", suma)

        
dod()
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    dod()
  File "<pyshell#101>", line 3, in dod
    while x != 0:
UnboundLocalError: local variable 'x' referenced before assignment
def dod():
    suma = 0
    while (x := 1) != 0:
        x = int(input("Liczba (exit - 0): "))
        suma += x
        print("Suma: ", suma)

        
dod()
Liczba (exit - 0): 12
Suma:  12
Liczba (exit - 0): 123
Suma:  135
Liczba (exit - 0): 123
Suma:  258
Liczba (exit - 0): 123
Suma:  381
Liczba (exit - 0): 
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    dod()
  File "<pyshell#104>", line 4, in dod
    x = int(input("Liczba (exit - 0): "))
ValueError: invalid literal for int() with base 10: ''
def sp3():
    while (l:=1) != 0:
        l = int(input("L: "))
        if l > 10:
            print(str(l) + " jest > 10")
        elif l < 0:
            print(str(l) + " jest < 0")
        elif l == 0:
            print("Cya!")
            exit()
        else:
            print(str(l) + " jest z przedzialu (0,10>")

            
sp3()
L: 1
1 jest z przedzialu (0,10>
L: -1
-1 jest < 0
L: 12
12 jest > 10
L: 
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    sp3()
  File "<pyshell#107>", line 3, in sp3
    l = int(input("L: "))
ValueError: invalid literal for int() with base 10: ''
sp3()
                     
L: 1
1 jest z przedzialu (0,10>
L: -1
-1 jest < 0
L: 12
12 jest > 10
L: 0
Cya!
def sp3():
    while (l:=1) != 0:
        l = int(input("L: "))
        if l > 10:
            print(str(l) + " jest > 10")
        elif l < 0:
            print(str(l) + " jest < 0")
        else:
            print(str(l) + " jest z przedzialu (0,10>")

            
def sp3():
    while (l:=1) != 0:
        l = int(input("L: "))
        if l > 10:
            print(str(l) + " jest > 10")
        elif l < 0:
            print(str(l) + " jest < 0")
        else:
            print(str(l) + " jest z przedzialu (0,10>")
    print("Cya")

    
sp3()
L: 12
12 jest > 10
L: 32
32 jest > 10
L: -1
-1 jest < 0
L: 0
0 jest z przedzialu (0,10>
L: 0
0 jest z przedzialu (0,10>
L: 
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    sp3()
  File "<pyshell#114>", line 3, in sp3
    l = int(input("L: "))
KeyboardInterrupt
def sp3():
    while (l:=1) != 0:
        l = int(input("L: "))
        if l > 10:
            print(str(l) + " jest > 10")
        elif l < 0:
            print(str(l) + " jest < 0")
        elif l == 0:
            break
        else:
            print(str(l) + " jest z przedzialu (0,10>")
    print("Cya")

    
sp3()
L: 1
1 jest z przedzialu (0,10>
L: 2
2 jest z przedzialu (0,10>
L: 3
3 jest z przedzialu (0,10>
L: 4122
4122 jest > 10
L: -1
-1 jest < 0
L: 0
Cya
def sp3():
    while True:
        l = int(input("L: "))
        if l > 10:
            print(str(l) + " jest > 10")
        elif l < 0:
            print(str(l) + " jest < 0")
...         elif l == 0:
...             break
...         else:
...             print(str(l) + " jest z przedzialu (0,10>")
...     print("Cya")
... 
...     
>>> def sp3():
...     while 1:
...         l = int(input("L: "))
...         if l > 10:
...             print(str(l) + " jest > 10")
...         elif l < 0:
...             print(str(l) + " jest < 0")
...         elif l == 0:
...             break
...         else:
...             print(str(l) + " jest z przedzialu (0,10>")
...     print("Cya")
... 
...     
>>> sp3()
L: 1
1 jest z przedzialu (0,10>
L: 2
2 jest z przedzialu (0,10>
L: 3
3 jest z przedzialu (0,10>
L: 4
4 jest z przedzialu (0,10>
L: 2
2 jest z przedzialu (0,10>
L: 12
12 jest > 10
L: 123
123 jest > 10
L: 123
123 jest > 10
L: -1
-1 jest < 0
L: 0
Cya
>>> def sprcl():
...     x = input("L: ")
...     print(x.isdigit())
... 
...     
>>> sprcl()
L: 4
True
>>> sprcl()
L: 43
True
>>> sprcl()
L: 43a
False
>>> sprcl()
L: 5.12
False
>>> 5.12
5.12
>>> sprcl()
L: a2
False
>>> def sprcl():
...     x = input("L: ")
...     return (x.isdigit())
... 
>>> sprcl()
L: 12
True
>>> sprcl()
L: a2
False
