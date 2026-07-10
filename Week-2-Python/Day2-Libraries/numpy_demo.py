'''
NumPy (Numerical Python) is a Python library used for scientific computing and numerical operations. 
It provides a powerful N-dimensional array (ndarray) that is faster 
and more memory-efficient than Python lists.
'''
import numpy as np
arr1=np.array([1,2,3,4,5,6])    # 1D array  
arr2=np.array([[1,2],[3,4]])    # 2D array  
arr3=np.array([[[1, 2], [3, 4]],    # 3D array
               [[5, 6], [7, 8]]])

print(arr1)
print(arr2)
print(arr3)

#indexing
print("Fisrt element of array:",arr1[0]) #first element
print("Last element of array:",arr1[-1]) #last element
index=np.array([1,2,3])
print(arr1[index])
x=arr1>2
print("Element greater than 2 in array:",arr1[x])

#slicing
print(arr1[0:4])
print(arr1[:3])

# create a array using numpy functions
a1=np.zeros((3,3)) 
a2=np.ones((2,2))  
arr=np.arange(0,10,2) #range zero to one and jump 2
print("Array of zeroes\n",a1)
print("Array of ones\n",a2)
print("Array between range\n",arr)

#Mathematical operations 
print("Square root of array1: ",np.sqrt(arr1))
print("exp of array1: ",np.exp(arr1))
print("Sum of all elements in array:",np.sum(arr1))
print("Maximum number in array:",np.max(arr1))
print("Minimum number in array",np.min(arr1))


'''Vectorization means performing operations on the entire array at once without writing loops'''
 
arr4=np.array([10,20,30,40,50])
arr5=np.array([2,4,6,8,10])
sum=arr4+2
print(sum)
mul=arr4*2
print(mul)
print("Sum of two array:",arr4+arr5)
print("Difference of two array",arr4-arr5)
print("Multiplication of two array:",arr4*arr5)
print("Division of two array:",arr4/arr5)


'''
Broadcasting is a NumPy feature that allows arrays of different shapes to perform arithmetic operations 
by automatically expanding the smaller array.
'''
a1=np.array([[1,2,3],   # matrix 
             [4,5,6]])

a2=np.array([10,20,30])  # vector
print("Addition of matrix and vector\n",a1+a2)
print("Multiplication of matrix and vector\n",a1*a2)

#column Broadcasting
a3=np.array([[12,14,16],
             [20,22,24]])

a4=np.array([[100],
             [200]])

print("Addition of matrix and vector\n",a3+a4)