Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
type([1,23,43])
<class 'list'>
[1,2,3,4,"a"][-1]
'a'
[1,2,3,4,"a"][3:-1]
[4]
[1,2,3,4,"a"][3:]
[4, 'a']
[1,2,3,4,"a"][2:-1]
[3, 4]
set1 = {1,1,1,12,2,22,2,2,2,2,"a","b"}
set1
{1, 2, 22, 'b', 12, 'a'}
set[1]
set[1]
set1[1]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    set1[1]
TypeError: 'set' object is not subscriptable
set1.has(1)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    set1.has(1)
AttributeError: 'set' object has no attribute 'has'
set1.includes(1)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    set1.includes(1)
AttributeError: 'set' object has no attribute 'includes'
1 in set1
True
set1 in 1
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    set1 in 1
TypeError: argument of type 'int' is not iterable
"a" in set1
True
if "a" in set1:
    print("OK")
else:
    print("NO")

    
OK
if "c" in set1:
    print("OK")
else:
    print("NO")

    
NO
True
True
False
False
if True:
    print("OK")
else print (set1)
SyntaxError: expected ':'
if True:
    print("OK")
else: print (set1)

OK
if True:
    print("OK")
else: print (set1)

OK
if True:
    print("OK")
else: print(set1)

OK
if True:
    print("OK")


else: print(set1)
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
if True:
    print("OK")
else: print(set1)

OK
if True:
    print("OK")
else:
    print(set1)

OK
dick = dict(a=1, 2=12, 3=True)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
dick = dict(a=>1, 2=>12, 3=>True)
SyntaxError: invalid syntax
dick = dict(a=1, 2=12, 3=True)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
dick = dict(a=1, b=12, c=True)
dick
{'a': 1, 'b': 12, 'c': True}
dick = {"a":1, "b":12, "c": True, 12: 15}
dick
{'a': 1, 'b': 12, 'c': True, 12: 15}
f"Hehe {dick['a']}"
'Hehe 1'
f"Hehe {dick["a"]}"
SyntaxError: f-string: unmatched '['
f"Hehe {dick[\"a\"]}"
SyntaxError: f-string expression part cannot include a backslash
f"Hehe {dick['a']}"
'Hehe 1'
def x()"
SyntaxError: unterminated string literal (detected at line 1)
def x():
    return print("abc")

print(x())
abc
None
"ac %f" % 0.2
'ac 0.200000'
"ac %.3f" % 0.2
'ac 0.200'
f"ac {0.2:3f}"
'ac 0.200000'
f"ac {0.2:#3f}"
'ac 0.200000'
f"ac {0.2:#f}"
'ac 0.200000'
f"ac {0.2}"
'ac 0.2'
f"ac {0.2:f3}"
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    f"ac {0.2:f3}"
ValueError: Invalid format specifier
f"ac {0.2:01.2f}"
'ac 0.20'
f"ac {0.2:01.15f}"
'ac 0.200000000000000'
f"ac {0.2:2.15f}"
'ac 0.200000000000000'
f"ac {0.2:2.1f}"
'ac 0.2'
f"ac {0.2:2.2f}"
'ac 0.20'
f"ac {0.2:22.2f}"
'ac                   0.20'
f"ac {0.2:3.2f}"
'ac 0.20'
f"ac {0.2:4.2f}"
'ac 0.20'
f"ac {0.2:5.2f}"
'ac  0.20'
f"ac {0.2:6.2f}"
'ac   0.20'
f"ac {0.2:0.2f}"
'ac 0.20'
x= "12"
x= "12.552"
f"ac {x!f:0.2f}"
SyntaxError: f-string: invalid conversion character: expected 's', 'r', or 'a'
f"ac {x:0.2f!s}"
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    f"ac {x:0.2f!s}"
ValueError: Invalid format specifier
f"ac {x:0.2f}"
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    f"ac {x:0.2f}"
ValueError: Unknown format code 'f' for object of type 'str'
f"ac {x!s:0.2f}"
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    f"ac {x!s:0.2f}"
ValueError: Unknown format code 'f' for object of type 'str'
f"ac {x!s}"
'ac 12.552'
f"ac {{x!s}:0.1f}"
SyntaxError: f-string: single '}' is not allowed
f"ac {{x!s}:0.1f}}"
SyntaxError: f-string: single '}' is not allowed
f"ac { {x!s} : 0.1f }"
SyntaxError: f-string: invalid syntax
f"ac { f'{x!s}' : 0.1f }"
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    f"ac { f'{x!s}' : 0.1f }"
ValueError: Invalid format specifier
f"ac {f'{x!s}':0.1f}"
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    f"ac {f'{x!s}':0.1f}"
ValueError: Unknown format code 'f' for object of type 'str'
f"ac {str(x):0.1f}"
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    f"ac {str(x):0.1f}"
ValueError: Unknown format code 'f' for object of type 'str'
f"ac {x:0.1f}"
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    f"ac {x:0.1f}"
ValueError: Unknown format code 'f' for object of type 'str'
f"ac {float(x):0.1f}"
'ac 12.6'
for l in "abc": print(l)

a
b
c
>>> for l in "abc": print(l, end="")
... 
abc
>>> for l in "abc": print(l, end="")
... 
abc
>>> l
'c'
>>> for x in range(0,5)
SyntaxError: expected ':'
>>> for x in range(0,5):
...     print(x)
... 
...     
0
1
2
3
4
>>> from functools import reduce
>>> zip(range(0,4))
<zip object at 0x0000021B78B6B840>
>>> repr(zip(range(0,4)))
'<zip object at 0x0000021B78B81F40>'
>>> list(zip(range(0,4)))
[(0,), (1,), (2,), (3,)]
>>> list(zip(range(0,4),range(0,4)))
[(0, 0), (1, 1), (2, 2), (3, 3)]
>>> zip(*range(0,4))
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    zip(*range(0,4))
TypeError: 'int' object is not iterable
>>> x = range(0,4)
>>> list(x)
[0, 1, 2, 3]
