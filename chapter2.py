import pandas as pd

"""Indexing,Selecting & Assigning"""

hotels= pd.read_csv(r"C:\\Users\\ruchi\\Downloads\\hotel_bookings.csv")

# print(hotels.country)

# o/p
# 0         PRT
# 1         PRT
# 2         GBR
# 3         GBR
# 4         GBR
#          ... 
# 119385    BEL
# 119386    FRA
# 119387    DEU
# 119388    GBR
# 119389    DEU
# Name: country, Length: 119390, dtype: object

# print(hotels['country'])

# 0         PRT
# 1         PRT
# 2         GBR
# 3         GBR
# 4         GBR
#          ...
# 119385    BEL
# 119386    FRA
# 119387    DEU
# 119388    GBR
# 119389    DEU
# Name: country, Length: 119390, dtype: object

# print(hotels['country'][0])
# o/p PRT


"""Indexig in pandas"""

"""iloc operator"""
# print(hotels.iloc[0])

# o/p
# hotel                             Resort Hotel
# is_canceled                                  0
# lead_time                                  342
# arrival_date_year                         2015
# arrival_date_month                        July
# arrival_date_week_number                    27
# arrival_date_day_of_month                    1
# stays_in_weekend_nights                      0
# stays_in_week_nights                         0
# adults                                       2
# children                                   0.0
# babies                                       0
# meal                                        BB
# country                                    PRT
# market_segment                          Direct
# distribution_channel                    Direct
# is_repeated_guest                            0
# previous_cancellations                       0
# previous_bookings_not_canceled               0
# reserved_room_type                           C
# assigned_room_type                           C
# booking_changes                              3
# deposit_type                        No Deposit
# agent                                      NaN
# company                                    NaN
# days_in_waiting_list                         0
# customer_type                        Transient
# adr                                        0.0
# required_car_parking_spaces                  0
# total_of_special_requests                    0
# reservation_status                   Check-Out
# reservation_status_date             2015-07-01
# Name: 0, dtype: object



# print(hotels.iloc[:, 0])

# 0         Resort Hotel
# 1         Resort Hotel
# 2         Resort Hotel
# 3         Resort Hotel
# 4         Resort Hotel
#               ...
# 119385      City Hotel
# 119386      City Hotel
# 119387      City Hotel
# 119388      City Hotel
# 119389      City Hotel
# Name: hotel, Length: 119390, dtype: object



# print(hotels.iloc[:3, 0])

# 0    Resort Hotel
# 1    Resort Hotel
# 2    Resort Hotel
# Name: hotel, dtype: object



# print(hotels.iloc[1:3, 0])

# 1    Resort Hotel
# 2    Resort Hotel
# Name: hotel, dtype: object



# print(hotels.iloc[[0, 1, 2], 0])

# 0    Resort Hotel
# 1    Resort Hotel
# 2    Resort Hotel
# Name: hotel, dtype: object



# print(hotels.iloc[-5:])

#              hotel  ...  reservation_status_date
# 119385  City Hotel  ...               2017-09-06
# 119386  City Hotel  ...               2017-09-07
# 119387  City Hotel  ...               2017-09-07
# 119388  City Hotel  ...               2017-09-07
# 119389  City Hotel  ...               2017-09-07

# [5 rows x 32 columns]



"""loc operator"""
#print(hotels.loc[0,'country'])
#PRT




#print(hotels.loc[:,['hotel','country','agent']])

# hotel country  agent
# 0       Resort Hotel     PRT    NaN
# 1       Resort Hotel     PRT    NaN
# 2       Resort Hotel     GBR    NaN
# 3       Resort Hotel     GBR  304.0
# 4       Resort Hotel     GBR  240.0
# ...              ...     ...    ...
# 119385    City Hotel     BEL  394.0
# 119386    City Hotel     FRA    9.0
# 119387    City Hotel     DEU    9.0
# 119388    City Hotel     GBR   89.0
# 119389    City Hotel     DEU    9.0

# [119390 rows x 3 columns]




"""Manipulating the index"""
#print(hotels.set_index("hotel",inplace=True))
#it will change the index of the dataframe to hotel column





# print(hotels.loc[:,'country'])
# 0         PRT
# 1         PRT
# 2         GBR
# 3         GBR
# 4         GBR
#          ...
# 119385    BEL
# 119386    FRA
# 119387    DEU
# 119388    GBR
# 119389    DEU
# Name: country, Length: 119390, dtype: object




"""Conditional selection"""
# print(hotels.country=='GBR')
# 0         False
# 1         False
# 2          True
# 3          True
# 4          True
#           ...
# 119385    False
# 119386    False
# 119387    False
# 119388     True
# 119389    False
# Name: country, Length: 119390, dtype: bool



# print(hotels.loc[hotels.country=='PRT'])

#                hotel  ...  reservation_status_date
# 0       Resort Hotel  ...               2015-07-01
# 1       Resort Hotel  ...               2015-07-01
# 6       Resort Hotel  ...               2015-07-03
# 7       Resort Hotel  ...               2015-07-03
# 8       Resort Hotel  ...               2015-05-06
# ...              ...  ...                      ...
# 119317    City Hotel  ...               2017-09-03
# 119340    City Hotel  ...               2017-09-03
# 119357    City Hotel  ...               2017-09-04
# 119366    City Hotel  ...               2017-09-04
# 119367    City Hotel  ...               2017-09-04

# [48590 rows x 32 columns]



# print(hotels.loc[(hotels.country == 'PRT')&(hotels.adults>1)])

# hotel  is_canceled  ...  reservation_status  reservation_status_date
# 0       Resort Hotel            0  ...           Check-Out               2015-07-01     
# 1       Resort Hotel            0  ...           Check-Out               2015-07-01     
# 6       Resort Hotel            0  ...           Check-Out               2015-07-03     
# 7       Resort Hotel            0  ...           Check-Out               2015-07-03     
# 8       Resort Hotel            1  ...            Canceled               2015-05-06     
# ...              ...          ...  ...                 ...                      ...     
# 119237    City Hotel            0  ...           Check-Out               2017-09-01     
# 119317    City Hotel            0  ...           Check-Out               2017-09-03     
# 119340    City Hotel            0  ...           Check-Out               2017-09-03     
# 119366    City Hotel            0  ...           Check-Out               2017-09-04     
# 119367    City Hotel            0  ...           Check-Out               2017-09-04     

# [35998 rows x 32 columns]




# print(hotels.loc[(hotels.country == 'PRT')|(hotels.adults>1)])
# hotel  is_canceled  ...  reservation_status  reservation_status_date
# 0       Resort Hotel            0  ...           Check-Out               2015-07-01     
# 1       Resort Hotel            0  ...           Check-Out               2015-07-01     
# 4       Resort Hotel            0  ...           Check-Out               2015-07-03     
# 5       Resort Hotel            0  ...           Check-Out               2015-07-03     
# 6       Resort Hotel            0  ...           Check-Out               2015-07-03     
# ...              ...          ...  ...                 ...                      ...     
# 119385    City Hotel            0  ...           Check-Out               2017-09-06     
# 119386    City Hotel            0  ...           Check-Out               2017-09-07     
# 119387    City Hotel            0  ...           Check-Out               2017-09-07     
# 119388    City Hotel            0  ...           Check-Out               2017-09-07     
# 119389    City Hotel            0  ...           Check-Out               2017-09-07     

# [108552 rows x 32 columns]


"""Built in functions"""

#print(hotels.loc[hotels.isin(['PRT','GBR'])])
#it is showing error




# print(hotels.loc[hotels.children.notnull()])

# hotel  is_canceled  ...  reservation_status  reservation_status_date
# 0       Resort Hotel            0  ...           Check-Out               2015-07-01
# 1       Resort Hotel            0  ...           Check-Out               2015-07-01
# 2       Resort Hotel            0  ...           Check-Out               2015-07-02     
# 3       Resort Hotel            0  ...           Check-Out               2015-07-02     
# 4       Resort Hotel            0  ...           Check-Out               2015-07-03     
# ...              ...          ...  ...                 ...                      ...     
# 119385    City Hotel            0  ...           Check-Out               2017-09-06     
# 119386    City Hotel            0  ...           Check-Out               2017-09-07     
# 119387    City Hotel            0  ...           Check-Out               2017-09-07     
# 119388    City Hotel            0  ...           Check-Out               2017-09-07     
# 119389    City Hotel            0  ...           Check-Out               2017-09-07     

# [119386 rows x 32 columns]




"""Assigning values"""

# hotels['babies']='cute'
# print(hotels['babies'])

# 0         cute
# 1         cute
# 2         cute
# 3         cute
# 4         cute
#           ... 
# 119385    cute
# 119386    cute
# 119387    cute
# 119388    cute
# 119389    cute
# Name: babies, Length: 119390, dtype: object


# hotels['meal']=range(len(hotels),0,-1)
# print(hotels['meal'])

# 0         119390
# 1         119389
# 2         119388
# 3         119387
# 4         119386
#            ...
# 119385         5
# 119386         4
# 119387         3
# 119388         2
# 119389         1
# Name: meal, Length: 119390, dtype: int64