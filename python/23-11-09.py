Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dok = input("Dokad: ")
Dokad: Warsaw
>>> kie = input("Kiedy: ")
Kiedy: Friday
>>> print("You are going to "+dok+" on "+kie)
You are going to Warsaw on Friday
>>> for i in range(0,int(print("Liczba: ")))
SyntaxError: expected ':'
>>> for i in range(0,int(print("Liczba: "))):
...     print(i)
... 
...     
Liczba: 
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    for i in range(0,int(print("Liczba: "))):
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'
>>> for i in range(0,int(print("Liczba: "))):
...     print(i)
... 
...     
Liczba: 
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    for i in range(0,int(print("Liczba: "))):
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'
>>> for i in range(0,int(input("Liczba"))):
...     print(i)
... 
...     
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
>>> for i in range(0,10):
...     print(i**2)
... 
...     
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
>>> for i in range(10,16):
...     print(i*2)
... 
...     
20
22
24
26
28
30
