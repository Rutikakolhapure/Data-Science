#ARRAY ATTRIBUTES OR DATATYPES
import numpy as np


#1.shape property
# arr_2d = np.array([[1,2,3],
#                  [4,5,6] ])
# print(arr_2d.shape)
#o/p (2, 3)



#2.size property
# arr_size = np.array([[1,2,3],
#                  [4,5,6] ])
# print(arr_size.size)
#o/p 6



#3.ndim property
# arr_1d = np.array([1,2,3])
# arr_2d=np.array([[1,2,3],[4,5,6]])
# arr_3d=np.array([[[1,2,3],[4,5,6]]])
# print(arr_1d.ndim)
# print(arr_2d.ndim)
# print(arr_3d.ndim)
# o/p 1
#     2
#     3



#4.dtype property
# arr = np.array([10,20,30.5,40])
# print(arr.dtype)
# o/p float64



# #5.astype()
# arr = np.array([10,20,30.5,40])
# print(arr.dtype)
# int_arr=arr.astype(int)
# print(int_arr)
# print(int_arr.dtype)
# o/p float64
# [10 20 30 40]
# int64


#Basic Oprations
# arr=np.array([10,20,30])
# print(arr+5)
# print(arr*5)
# print(arr**5)

# o/p [15 25 35]
# [ 50 100 150]
# [  100000  3200000 24300000]


#Aggregate Functions
# arr=np.array([10,20,30,40,50])
# print(np.sum(arr))
# print(np.min(arr))
# print(np.max(arr))
# print(np.mean(arr))
# print(np.std(arr))
# print(np.var(arr))

# o/p 150
# 10
# 50
# 30.0
# 14.142135623730951
# 200.0


