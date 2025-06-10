import numpy as np

"""np.isnan()"""
# arr = np.array([1,2,np.nan,4,np.nan,6])
# print(np.isnan(arr))

# o/p [False False  True False  True False]


"""np.nan_to_num()"""
# arr = np.array([1,2,np.nan,4,np.nan,6])

# cleaned_arr = np.nan_to_num(arr)
# print(cleaned_arr)

# cleaned_arr = np.nan_to_num(arr,nan=100)
# print(cleaned_arr)

# o/p [1. 2. 0. 4. 0. 6.]

# o/p [  1.   2. 100.   4. 100.   6.]



"""np.isinf()"""
# arr = np.array([1,2,np.inf,3,-np.inf,4])
# print(np.isinf(arr))

# o/p [False False  True False  True False]

"""np.nan_to_num"""
# arr = np.array([1,2,np.inf,3,-np.inf,4])
# cleaned_arr=np.nan_to_num(arr,posinf=1000,neginf=-1000)
# print(cleaned_arr)

# o/p [    1.     2.  1000.     3. -1000.     4.]