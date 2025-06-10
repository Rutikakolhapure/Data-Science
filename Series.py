import pandas as pd

"""Simple series"""
# x=pd.Series([1,2,3,4,5])
# print(x)

# o/p
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64

"""Index"""
# x=pd.Series([30,35,40],index=['2015 Sales','2016 Sales','2017 Sales'], name='Product A')
# print(x)
# o/p
# 2015 Sales    30
# 2016 Sales    35
# 2017 Sales    40
# Name: Product A, dtype: int64


"""real data frames"""
# wine_reviews = pd.read_csv(r"C:\\Users\\ruchi\\Downloads\\hotel_bookings.csv")
# x=wine_reviews.shape
# print(x)
# y=wine_reviews.head()
# print(y)

# o/p
# (119390, 32)

# o/p
# (119390, 32)
#           hotel  ...  reservation_status_date
# 0  Resort Hotel  ...               2015-07-01
# 1  Resort Hotel  ...               2015-07-01
# 2  Resort Hotel  ...               2015-07-02
# 3  Resort Hotel  ...               2015-07-02
# 4  Resort Hotel  ...               2015-07-03

# [5 rows x 32 columns]


# wine_reviews = pd.read_csv(r"C:\\Users\\ruchi\\Downloads\\hotel_bookings.csv", index_col=0)
# x=wine_reviews.head()
# print(x)

#               is_canceled  lead_time  arrival_date_year  ... total_of_special_requests  reservation_status  reservation_status_date
# hotel                                                    ...
# Resort Hotel            0        342               2015  ...                         0           Check-Out               2015-07-01
# Resort Hotel            0        737               2015  ...                         0           Check-Out               2015-07-01
# Resort Hotel            0          7               2015  ...                         0           Check-Out               2015-07-02
# Resort Hotel            0         13               2015  ...                         0           Check-Out               2015-07-02
# Resort Hotel            0         14               2015  ...                         1           Check-Out               2015-07-03

# [5 rows x 31 columns]