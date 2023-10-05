Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> zbior = set([200,100,100,100,200,50,12,111,1,1,1])
>>> zbior
{1, 100, 200, 12, 111, 50}
>>> if 100 in zbior:
...     print(100)
... 
...     
100
>>> if 100 not in zbior:
...     print("brak 100")
... 
...     
>>> true
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> true = True
>>> false = False
>>> if d == true
SyntaxError: expected ':'
>>> d = True
>>> if d == true:
...     print("prawda")
... 
...     
prawda
>>> if d:
...     print("prawda")
... 
...     
prawda
>>> type(zbior)
<class 'set'>
>>> a = dict([("1",1),("2",2)])
>>> a
{'1': 1, '2': 2}
>>> a["1"]
1
