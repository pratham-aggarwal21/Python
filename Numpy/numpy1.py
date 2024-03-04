import numpy as np
from numpy import random

##l = eval(input("Enter the list: "))
##print(np.array(l))


##x = random.randint(2,10,size =(3,3))
##print(x)

##arr = np.zeros(10)
##arr[5] = 11
##print(arr)

##x = np.arange(12,39)
##print(x)

##x = np.arange(12,39)
##y = x[::-1]
##print(y)

##x = np.arange(12,39)
##y = x.astype(float)
##print(y)

##arr = np.zeros([10,10])
##arr = arr.astype(int)
##arr[0,:] = 1
##arr[-1,:] = 1
##print(arr)


##arr = np.ones([10,10])
##arr = arr.astype(int)
##arr[0,:] = 0
##arr[-1,:] = 0
##print(arr)

##arr = np.zeros([8,8])
##arr = arr.astype(int)
##arr[0:,::2] = 1
##print(arr)

##l = [1,2,3,4,5]
##np.array(l)
##a = int(input("Enter the value: "))
##l.append(a)
##print(l)

##arr1 = np.empty([8,8])
##print(arr1)
##
##arr2 = np.full([8,8],6)
##print(arr2)

##l = eval(input("Enter the values in C: "))
##arr = np.array(l)
##arr2 = arr - 17.78
##print(arr2)

##l = np.array([1.00000000+0.j,0.70710678+0.70710678j])
##print(l.real)
##print(l.imag)

##arr = np.array([1,2,3,4,5,6])
##print(len(arr))
##print(arr.itemsize)
##print(arr.itemsize * len(arr))

##Array1=np.array([ 0, 10, 20, 40, 60])
##Array2=np.array([0, 40])
##print(np.in1d(Array1,Array2))


##Array1=np.array([ 0, 10, 20, 40, 60])
##Array2=np.array([10,30, 40])
##print(np.intersect1d(Array1,Array2))

##Array1=np.array([10, 10, 20, 20, 0])
##print(np.unique(Array1))

##Array1=np.array([ 0, 10 ,20 ,40 ,60 ,80])
##Array2=np.array([10, 30, 40, 50, 70, 90])
##print(np.setdiff1d(Array1, Array2, assume_unique= True))

##Array1=np.array([ 0, 10 ,20 ,40 ,60 ,80])
##Array2=np.array([10, 30, 40, 50, 70, 90])
##print(np.setxor1d(Array1, Array2, assume_unique= True))


##Array1=np.array([1,1,1,1,1,1,1,1,1,1])
##Array2=np.array([1,1,1,1,1,1,0])
##print(np.any(Array1))
##print(np.all(Array2))


##Array1=np.array([ 0, 10 ,20 ,40 ,60 ,80])
##print(np.tile(Array1, 2))

##Array1 = np.array([1,2,3,4])
##print(np.repeat(Array1, 2))


##array1 =np.array([0,10,20,60,80])
##print(np.max(array1))
##print(np.min(array1))


##array1 = np.array([1,2])
##array2 = np.array([4,5])
##print(array1>array2)
##print(array1>=array2)
##print(array1<array2)
##print(array1<=array2)

##arr = np.array([[2,5],[4,4]])
##print(np.sort(arr, axis =1))
##print(np.sort(arr, axis =0))

##arr1 = np.array(['Margery','Betsey', 'Shelley', 'Lanell', 'Genesis'])
##arr2 = np.array(['Woolum','Battle', 'Brien', 'Plotner', 'Stahl'])
##print(np.lexsort((arr1,arr2)))


##Array1=np.array([ 0, 10 ,20 ,40 ,60 ,80])
##filter_arr = Array1>10
##print(np.nonzero(Array1>10))
##newarr = Array1[filter_arr]
##print(filter_arr)
##print(newarr)

## 32

##arr1 = np.array([0,10,20,30,40,50,60,70])
##newarr = arr1.reshape(4,2)
##print(newarr)

##arr1 = np.array([[0,10,20,30],[40,50,60,70]])
##arr = arr1.reshape(1,8)
##print(arr)

##arr1 = np.array([[0,10,20,30],[40,50,60,70]])
##newarr = arr1.astype('f')
##print(newarr)


##arr2 = np.full([3,5],6)
##print(arr2)

##arr = np.full([1,10], 10)
##print(arr)

##arr = np.eye(3)
##print(arr)

##arr = np.diagflat([2,4,6,8])
##print(arr)

##arr = np.arange(50)
##print(arr)
##arr1 = np.arange(10,50)
##print(arr1)

##arr = np.linspace(2.5,6.5,30)
##print(arr)

##arr1 = np.array([[0,10,20,30],[40,50,60,70],[90,100,200,300]])
##arr = arr1.reshape(1,12)
##print(arr)

##arr1 = np.array([[0,10,20,30],[40,50,60,70],[90,100,200,300]])
##arr = arr1.reshape(12)
##print(arr)
##print(arr[3])

##arr = np.arange(2,14).reshape(4,3)
##print(np.triu(arr,-1))
