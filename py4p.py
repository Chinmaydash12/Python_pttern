Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32.....
Type "help", "copyright", "credits" or "license()" for more information.
>>> d={0:24,1:'Hi','a':'Hello'}
>>> d(a)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    d(a)
NameError: name 'a' is not defined
>>> d[0]
24
>>> d[1]
'Hi'
>>> d[a]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    d[a]
NameError: name 'a' is not defined
>>> d['a']
'Hello'
>>> c={'b':1,'c':'Hi'}
>>> c['b']
1
>>> c['c']
'Hi'
>>> c.update({'c':25})
>>> print(c)
{'b': 1, 'c': 25}
>>> c.update({'b':'Hi'})
>>> print(c)
{'b': 'Hi', 'c': 25}
>>> d.popitem()
('a', 'Hello')
>>> print(d)
{0: 24, 1: 'Hi'}
>>> d.popitem()
(1, 'Hi')
>>> print(d)
{0: 24}
>>> d.pop(o)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    d.pop(o)
NameError: name 'o' is not defined
>>> d.pop(0)
24
>>> print(d)
{}
>>> #list
>>> l=[1,2,2.4,'Hi']
>>> c.values()
dict_values(['Hi', 25])
>>> c.items()
dict_items([('b', 'Hi'), ('c', 25)])
>>> c.keys()
dict_keys(['b', 'c'])
>>> c.get('a')
>>> print(c)
{'b': 'Hi', 'c': 25}
>>> c.get('c')
25
>>> c.get('b')
'Hi'
>>> c['c']
25
>>> c['b']
'Hi'
>>> c[0]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    c[0]
KeyError: 0
>>> d[0]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    d[0]
KeyError: 0
>>> c.setdefault('d')
>>> print(c)
{'b': 'Hi', 'c': 25, 'd': None}
>>> print('c')
c
>>> print(c)
{'b': 'Hi', 'c': 25, 'd': None}
>>> c.setdefault('d',56)
>>> print(c)
{'b': 'Hi', 'c': 25, 'd': None}
>>> c.setdefault('d':56)
SyntaxError: invalid syntax
>>> c.setdefault('e',24)
24
>>> print(c)
{'b': 'Hi', 'c': 25, 'd': None, 'e': 24}
>>> c.update({'d':56})
>>> print(c)
{'b': 'Hi', 'c': 25, 'd': 56, 'e': 24}
>>> c.pop('e')
24
>>> print(c)
{'b': 'Hi', 'c': 25, 'd': 56}
>>> c.popitem()
('d', 56)
>>> c.setdefault('d',56)
56
>>> print(c)
{'b': 'Hi', 'c': 25, 'd': 56}
>>> c.update({'d':65})
>>> print(c)
{'b': 'Hi', 'c': 25, 'd': 65}
>>> c.update({'c':52})
>>> print(c)
{'b': 'Hi', 'c': 52, 'd': 65}
>>> c.setdefault('e',32)
32
>>> print(c)
{'b': 'Hi', 'c': 52, 'd': 65, 'e': 32}
>>> c.pop('e')
32
>>> print(c)
{'b': 'Hi', 'c': 52, 'd': 65}
>>> c.update({'e':45})
>>> print(c)
{'b': 'Hi', 'c': 52, 'd': 65, 'e': 45}
>>> c.popitem()
('e', 45)
>>> print(c)
{'b': 'Hi', 'c': 52, 'd': 65}
>>> c.setdefault('m')
>>> print(c)
{'b': 'Hi', 'c': 52, 'd': 65, 'm': None}
>>> c.setdefault('k')
>>> print(c)
{'b': 'Hi', 'c': 52, 'd': 65, 'm': None, 'k': None}
>>> c.pop({'m','k'})
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    c.pop({'m','k'})
TypeError: unhashable type: 'set'
>>> c.pop({'m'})
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    c.pop({'m'})
TypeError: unhashable type: 'set'
>>> c.pop('m','k')
>>> print(c)
{'b': 'Hi', 'c': 52, 'd': 65, 'k': None}
>>> c.popitem()
('k', None)
>>> #Set
>>> s={1,2,3,3,3,3,} #Set
>>> print(s)
{1, 2, 3}
>>> s[1]
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    s[1]
TypeError: 'set' object is not subscriptable
>>> s[0]
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    s[0]
TypeError: 'set' object is not subscriptable
>>> si={2,3,4}
>>> print(si)
{2, 3, 4}
>>> s.union(si)
{1, 2, 3, 4}
>>> s|si
{1, 2, 3, 4}
>>> s.inntersection(si)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    s.inntersection(si)
AttributeError: 'set' object has no attribute 'inntersection'
>>> sii={3,4,5,6}
>>> print(sii)
{3, 4, 5, 6}
>>> s.intersection(sii)
{3}
>>> s.intersection(si)
{2, 3}
>>> s&si
{2, 3}
>>> s&sii
{3}
>>> s.difference(si)
{1}
>>> s-si
{1}
>>> s.intersection(sii)
{3}
>>> s-sii
{1, 2}
>>> s.difference(sii)
{1, 2}
>>> s.symmentric-difference(si)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    s.symmentric-difference(si)
AttributeError: 'set' object has no attribute 'symmentric'
>>> s^si
{1, 4}
>>> s.symmentricdifference(si)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    s.symmentricdifference(si)
AttributeError: 'set' object has no attribute 'symmentricdifference'
>>> s.symmetric_difference(si)
{1, 4}
>>> s.symmetric_difference(sii)
{1, 2, 4, 5, 6}
>>> s^sii
{1, 2, 4, 5, 6}
>>> print(s)
{1, 2, 3}
>>> print(si)
{2, 3, 4}
>>> print(sii)
{3, 4, 5, 6}
>>> si.symmetric_difference(sii)
{2, 5, 6}
>>> sii.symmetric_difference(si)
{2, 5, 6}
>>> 
