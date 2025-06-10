import pandas as pd

"""Integer dataframe"""
# x=pd.DataFrame({'Yes':[50,21],'No':[131,2]})
# print(x)

# o/p
#    Yes   No
# 0   50  131
# 1   21    2


"""String dataframe"""
# x=pd.DataFrame({'Bob':['I like it,','It was awful.'],'Sue':['Pretty good.','Bland.' ]})
# print(x)

# o/p
#              Bob           Sue
# 0     I like it,  Pretty good.
# 1  It was awful.        Bland.


"""using our own index."""
# x=pd.DataFrame({'Bob':['I like it,','It was awful.'],
#                 'Sue':['Pretty good.','Bland.' ]}
#                ,index=['A','B'])
# print(x)

# o/p

#              Bob           Sue
# A     I like it,  Pretty good.
# B  It was awful.        Bland.