import numpy as np


""" Insertion"""
"""1D array"""
# arr=np.array([10,20,30])
# print(arr)
# new_arr=np.insert(arr,1,40,0)
# print(new_arr)
# o/p [10 20 30]
# [10 40 20 30]


"""1D array"""
# arr=np.array([[10,20],[30,40]])
# print(arr)
# new_arr=np.insert(arr,1,[50,60],0)
# print(new_arr)
# new_arr=np.insert(arr,1,[50,60],1)
# print(new_arr)
# new_arr=np.insert(arr,1,[50,60],None)
# print(new_arr)

# o/p 
# [[10 20]
#  [30 40]]
# [[10 20]
#  [50 60]
#  [30 40]]
# [[10 50 20]
#  [30 60 40]]
#[10 50 60 20 30 40]



""" Append"""
# arr=np.array([10,20,30])
# new_arr=np.append(arr,[40,50,60])
# print(new_arr)

# o/p [10 20 30 40 50 60]


"""Concatanation"""
#arr1=np.array([1,2,3])
# arr2=np.array([1,2,3])
# arr=np.concatenate((arr1,arr2))
# print(arr)

# o/p [1 2 3 1 2 3]

"""DElete"""
# arr=np.array([10,20,30])
# print(arr)
# arr1=np.delete(arr,1)
# print(arr1)
# o/p [10 20 30]
# [10 30]

"""2D array"""
# arr=np.array([[10,20,30],[10,20,30]])
# print(arr)
# arr1=np.delete(arr,0,axis=0)
# print(arr1)

# [[10 20 30]
#  [10 20 30]]
# [[10 20 30]]

"""Stacking"""
# arr1=np.array([1,2,3])
# arr2=np.array([1,2,3])

# print(np.vstack((arr1,arr2)))
# print(np.hstack((arr1,arr2)))

# o/p
# [[1 2 3]
#  [1 2 3]]
# [1 2 3 1 2 3]


"""Spliting"""
# arr=np.array([1,2,3,4])
# print(np.split(arr,2))
# print(np.hsplit(arr,2))
# o/p [array([1, 2]), array([3, 4])]
# [array([1, 2]), array([3, 4])]
#for vsplit you need a 2D arr