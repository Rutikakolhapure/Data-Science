import numpy as np

"""general example"""
# prices=np.array([100,200,300,400,500])
# discount=10
# new_prices=prices-(prices*(discount/100))
# print(new_prices)

# o/p [ 90. 180. 270. 360. 450.]



"""Rule 2"""
# arr=np.array([100,200,300])
# result=arr*2
# print(result)

# o/p [200 400 600]


"""1D to 2D"""
# matrix=np.array([[1,2,3],[4,5,6]]) #2x3 matrix
# vector=np.array([10,20,30]) # 1D array

# result =matrix + vector
# print(result)

# o/p [[11 22 33]
#  [14 25 36]]


"""Rule 3"""
# arr1=np.array([1,2,3],[4,5,6]) #shape(2,3)
# arr2=np.array([1,2]) #shape(2)

# result = arr1 + arr2

# print(result)

# error
# Traceback (most recent call last):
#   File "c:\Users\ruchi\Videos\Data_Science\Numpy\broadcasting.py", line 33, in <module>
#     arr1=np.array([1,2,3],[4,5,6])
# TypeError: Field elements must be 2- or 3-tuples, got '4'
#solution is use .reshape property and reshape the array

