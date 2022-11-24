#내장함수
abs(5)
abs(-2.234)
all([2,56,23])
all([])
all([1,3,5,7,0])
any([1,3,4,0])
any([])

chr(97)

divmod(10,3)
eval('1+2')
eval("'hi'+'a'")
eval('divmod(10,3)')
a=[1,2,3,4,5,6,7]
def even(x):
    if x%2==0:
        return True
    else:
        return False

print(list(filter(even,a)))
b=a
id(b)
a is b
c=4
a is c
id(c)
input()
int('3')
str(4)
class Apple:pass
d=Apple()
Apple is d
type(d)
isinstance(d,Apple)
list(map(lambda x:x*3,[1,2,3,4]))
>>> max([1,2,3,4,5])
5
>>> max('mountain')
'u'
>>> min([1,2,3,4,5])
1
>>> pow(2,2)
4
>>> list(range(1,3))
[1, 2]
>>> list(range(0,10,2))
[0, 2, 4, 6, 8]
>>> list(range(30,10,-2))
[30, 28, 26, 24, 22, 20, 18, 16, 14, 12]
>>> round(10.2)
10
>>> round(10.7)
11
>>> round(3.14254,3)
3.143
>>> round(3.14254,2)
3.14
>>> sorted('mountain')
['a', 'i', 'm', 'n', 'n', 'o', 't', 'u']
>>> sorted((23,42,22))
[22, 23, 42]
>>> sum([1,2,3])
6
>>> tuple('abc')
('a', 'b', 'c')
>>> tuple([1,3,5,6,8])
(1, 3, 5, 6, 8)
>>> list(zip([1,2,3,4],[5,6,7,8]))
[(1, 5), (2, 6), (3, 7), (4, 8)]
>>> list(zip([1,2,3,4],[6,7,8]))
list(zip('myhome','telephone'))