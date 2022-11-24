#내장함수
print(abs(5))
print(all([1,3,5,7,0]))
print(any([1,3,4,0]))
print(any([]))
print(chr(97))
print(divmod(10,3))
print(eval('1+2'))
print(eval("'hi'+'a'"))
print(eval('divmod(10,3)'))
a=[1,2,3,4,5,6,7]
def even(x):
    if x%2==0:
        return True
    else:
        return False
print(list(filter(even,a)))

print(hex(345))

print(id(a))
b=a
print(id(b))
print(a is b)

c=4
print(a is c)
print(id(c))
# input()
print(int('3'))
print(str(4))

class Apple:pass
d=Apple()
print(Apple is d)
print(type(d))
print(isinstance(d,Apple))

print(len(a))

print(list(map(lambda x:x*3,[1,2,3,4])))

# print(max[1,2,3,4,5])
# print(max('moubtain'))
# print(min[1,2,3,4,5])
print(pow(2,2))
print(list(range(1,3)))
print(list(range(0,10,2)))
print(list(range(30,10,-2)))
print(round(10.2))
print(round(10.7))
print(round(3.14254,3))
print(round(3.14254,2))
print(sorted('mountain'))
# print(sorted(23,42,22))
# print(sum[1,2,3])
print(tuple('abc'))
print(tuple([1,3,5,6,8]))
print(list(zip([1,2,3,4],[5,6,7,8])))
print(list(zip([1,2,3,4],[5,6,7])))
print(list(zip('myhome','telphone')))


import pickle


