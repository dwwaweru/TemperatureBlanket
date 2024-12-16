#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 16:23:04 2020

@author: D.W.

Populating Row Colors 

Completed Patter for Ann Arbor Temperature Blanket (8/14/2020-8/14/2021)
"""
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors
from collections import Counter
#yarn colors
color = ['Burgundy', 'Cherry', 'Pumpkin', 'Gold', 'Forest', 
          'Deep Forest', 'Teal', 'Blue Moon', 'Smoke', 
          'Blue Haze', 'Navy', 'Lapis', 'Plum', 'White']
#set desired colorway
colorway = 'B'

#bring in data
rawtemp = pd.read_table("/Users/dwwaweru/Desktop/Crochet/aa20.txt")
rowcount = rawtemp.count()
n = rowcount.iloc[0]-1 #number of days in dataset with spaces
trecord = rawtemp.loc[:n,['Day','Temp']] #clean data

#creating list of temps
temp = trecord.loc[:,'Temp']
temp_list = temp.tolist()

#create yarn list
yarn = []

#assign color given daily high temp
if colorway == 'B':
    for i in temp_list:
        if i == 500:
            yarn.append(color.index('White'))
        elif i in range(90,150):
            yarn.append(color.index('Burgundy'))
        elif i in range(83,90):
            yarn.append(color.index('Cherry'))
        elif i in range(76,83):
            yarn.append(color.index('Pumpkin'))
        elif i in range(69,76):
            yarn.append(color.index('Gold'))
        elif i in range(62,69):
            yarn.append(color.index('Forest'))
        elif i in range(55,62):
            yarn.append(color.index('Deep Forest'))
        elif i in range(48,55):
            yarn.append(color.index('Teal'))
        elif i in range(41,48):
            yarn.append(color.index('Blue Moon'))
        elif i in range(34,41):
            yarn.append(color.index('Smoke'))
        elif i in range(27,34):
            yarn.append(color.index('Blue Haze'))
        elif i in range(20,27):
            yarn.append(color.index('Navy'))
        elif i in range(13,20):
            yarn.append(color.index('Lapis'))
        elif i<= 12:
            yarn.append(color.index('Plum'))
        else:
            yarn.append('other')
else:
    for i in temp_list:
        if i == 500:
            yarn.append(color.index('White'))
        elif i in range(95,150):
            yarn.append(color.index('Burgundy'))
        elif i in range(88,95):
            yarn.append(color.index('Cherry'))
        elif i in range(81,88):
            yarn.append(color.index('Pumpkin'))
        elif i in range(74,81):
            yarn.append(color.index('Gold'))
        elif i in range(67,74):
            yarn.append(color.index('Forest'))
        elif i in range(60,67):
            yarn.append(color.index('Deep Forest'))
        elif i in range(53,60):
            yarn.append(color.index('Teal'))
        elif i in range(46,53):
            yarn.append(color.index('Blue Moon'))
        elif i in range(39,46):
            yarn.append(color.index('Smoke'))
        elif i in range(32,39):
            yarn.append(color.index('Blue Haze'))
        elif i in range(25,32):
            yarn.append(color.index('Navy'))
        elif i in range(18,25):
            yarn.append(color.index('Lapis'))
        elif i<= 17:
            yarn.append(color.index('Plum'))
        else:
            yarn.append('other')
    
#print(yarn) 


#creating data table, a list of lists
blanket_grid = []
for i in yarn:
    row = []
    for x in range(1):
        row.append(i)
    blanket_grid.append(row)
#print(blanket_grid)
        

#list of hex codes corresponding to yarn color
yarn_col = ['#7B2233','#BD362C', '#EF6430', '#F5A631',
            '#88864C', '#6D5C4F', '#2E757E','#506985',
            '#CFD5DD', '#ABCFDA', '#012A6E', '#29355C',
            '#866C80', '#FFFFFF']

#making blank grid
data = blanket_grid
cmap = colors.ListedColormap(yarn_col)
#plt.figure(figsize=(6,6))
plt.pcolor(data[::-1],cmap=cmap,edgecolors='none')
#plt.xticks(np.arange(0.5,10.5,step=1))
#plt.yticks(np.arange(0.5,10.5,step=1))
print("Final Blanket: Aug 14 2020 to Aug 14 2021")
print("Colorway:", colorway)
plt.show()


# pattern text
print('PATTERN:\nFor white rows, use a 4.5mm hook. For all other rows, use 5.5mm hook.')
print('Foundation Row: Chain 320 stiches.')
for i in range(len(yarn)):
 if color[yarn[i]] == 'White':
     print('Row',i+1,': HDC with',color[yarn[i]],'(320)')
 else:
     print('Row',i+1,': Moss stitch with',color[yarn[i]],'(320)')
print("\n")

#How much yarn do you need?
a = Counter(yarn)
for i in a:
    if color[i] == 'White':
        print("White:",round((a[i]/17),2),"skeins for",a[i],'rows.')
    else:
        print(color[i],":",round((a[i]/17),2),"skeins for",a[i],'rows.')

tot_colrow = len(temp_list) - a[13]
prj_cost = (((tot_colrow*12)/260)+((a[13]*9.2)/260))*2.99
print("\nApprox. # skeins:",(prj_cost//2.99))
print('\nTotal cost: $',round(prj_cost,2))