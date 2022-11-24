import pandas as pd
import numpy as np
print('aa')
ar=[0,1,2,3,4,5,6,7,8,9,10]
print(ar)
ar1=np.array([0,1,2,3,4,5,6,7,8,9,10])
print(ar1)
print(type(ar))
print(type(ar1))

data=ar
result=[]
for i in data:
    result.append(i*3)
print(result)

data1=np.array(ar1)
print(data1)
print(data1*3)

data2=np.array(ar)
print(data1+data2)
print(2*data1+data2)
print(data1==10)
print((data1>5))
print((data2<8))
print((data1>5)&(data2<8))


d2=np.array([[0,1,2],[3,4,5]])
print(d2)
print(len(d2))
print(len(d2[0]))
print(ar1.ndim,ar1.shape)
print(d2.ndim,d2.shape)

d3=np.array([[[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]],
             [[13,14,15,16],
              [17,18,19,20],
              [21,22,23,24]]    
])

print(d3.ndim,d3.shape)