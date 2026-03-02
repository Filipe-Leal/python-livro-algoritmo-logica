Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a = True
>>> b = False
>>> C = True
>>> a and a
True
>>> b and b
False
>>> not c
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    not c
NameError: name 'c' is not defined. Did you mean: 'C'?
>>> not C
False
>>> not b
True
>>> not a
False
>>> a and b
False
>>> b and c
False
>>> a or C
True
>>> b or C
True
>>> C or a
True
>>> C or b
True
>>> C or C
True
>>> b or b
False
