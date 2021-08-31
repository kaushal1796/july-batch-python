# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 15:58:59 2021
@author: Admin
"""
#-------------------------Reading & Writing data in Files----------------------

import pandas

# Reading CSV Files with Pandas:
df = pandas.read_csv('D:/work july py work/csv files/User_Data.csv')
print(df)

# Writing CSV Files with Pandas:
df.to_csv('D:/work july py work/csv files/IIT-B.csv')

# Reading Excel Files with Pandas
df1 = pandas.read_excel('D:/work july py work/excel files/User_Data.xlsx')

df1 = pandas.read_excel('D:/work july py work/excel files/User_Data.xlsx')
print(df1)

# Writing Excel Files with Pandas 
df1.to_excel('D:/work july py work/excel files/IIT-B.xlsx')
df2 = pandas.DataFrame(df1)
print (df2)