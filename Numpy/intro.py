# import numpy as np
# tempretures = np.array([32.5,31.8,33.0,35.2,36.6])
# average = np.mean(tempretures)
# print(average)



# ARRAYS IN NUMPY

# py_list=[1,2,3,4,5]
# print(py_list)

# import numpy as np
# numpy_arr=np.array([1,2,3,4,5])
# print(numpy_arr)

# o/p [1, 2, 3, 4, 5]
# [1 2 3 4 5]



#1D array
# import numpy as np
# oneD_array=np.array([1,2,3,4,5])
# print(oneD_array)


#2D array
# import numpy as np
# twoD_array=np.array([[1,2,3],
#                      [4,5,6],
#                      [7,8,9]])
# print(twoD_array)




#creation of numpy using default values
#syntax:np.zeros(shape) {where shape=size of array}
# import numpy as np
# zeroes_array = np.zeros(3)
# print(zeroes_array)
# o/p [0. 0. 0.]
#for elements as 1 then replace zeroes_array by ones_array


#for any other value use
# import numpy as np
# filled_Array = np.full((2,2),7)
# print(filled_Array)
# o/p [[7 7]
#     [7 7]]




#Creating sequence of a numbers in numpy
# import numpy as np
# arr = np.arange(1,10,2)
# print(arr)



#identity matrices
# import numpy as np
# identity_matrix = np.eye(4)
# print(identity_matrix)
# o/p[[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]