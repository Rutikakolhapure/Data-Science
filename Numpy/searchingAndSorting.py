import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 4, 4])
# x = np.where(arr == 4)
# print(x)

# o/p (array([3, 5, 6]),)


# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# x = np.where(arr%2 == 0)
# print(x)
# o/p (array([1, 3, 5, 7]),)


# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# x = np.where(arr%2 == 1)
# print(x)

# o/p (array([0, 2, 4, 6]),)

"""searchsorted"""
# arr = np.array([6, 7, 8, 9])
# x = np.searchsorted(arr, 7)
# print(x)

# o/p 1


# arr = np.array([6, 7, 8, 9])
# x = np.searchsorted(arr, 7, side='right')
# print(x)
# o/p 2

# arr = np.array([1, 3, 5, 7])
# x = np.searchsorted(arr, [2, 4, 6])
# print(x)
# o/p [1 2 3]


"""Sorting"""
# arr = np.array([3, 2, 0, 1])

# print(np.sort(arr))
# o/p [0 1 2 3]


# arr = np.array(['banana', 'cherry', 'apple'])
# print(np.sort(arr))

# o/p ['apple' 'banana' 'cherry']


# arr = np.array([True, False, True])
# print(np.sort(arr))
# o/p [False  True  True]

# arr = np.array([[3, 2, 4], [5, 0, 1]])
# print(np.sort(arr))
# o/p [[2 3 4]
#  [0 1 5]]