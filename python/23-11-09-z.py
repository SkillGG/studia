Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
wt=""
>>> i = int(input("Liczba: "))
Liczba: 5
>>> text = input("Text: ")
Text: Marmolada
>>> for x in range(i):
...     wt+=text
... 
...     
>>> for x in range(i):
...     print(text,end="")
... 
...     
MarmoladaMarmoladaMarmoladaMarmoladaMarmolada
>>> if(len(wt) >= 30):
...     print("BRAWO!")
... else print("Try again")
SyntaxError: expected ':'
>>> if(len(wt) >= 30):
...     print("BRAWO!")
... else: print("Try again")
... 
BRAWO!
>>> mt = [[x*y for x in range(1,10)] for y in range(1,10)]
>>> 
>>> for c in mt:
...     for x in c:
...         print(f" {x}" if x < 10 else f"{x}", end=" ")
...     print()
... 
...     
 1  2  3  4  5  6  7  8  9 
 2  4  6  8 10 12 14 16 18 
 3  6  9 12 15 18 21 24 27 
 4  8 12 16 20 24 28 32 36 
 5 10 15 20 25 30 35 40 45 
 6 12 18 24 30 36 42 48 54 
 7 14 21 28 35 42 49 56 63 
 8 16 24 32 40 48 56 64 72 
 9 18 27 36 45 54 63 72 81 
