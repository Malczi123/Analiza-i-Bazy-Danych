import pandas as pd
import numpy as np
import os
import pathlib
import re


start_dir = r"C:\Users\kmalc\OneDrive\Pulpit\studiasemestrVII\aibd\lab2\OriginalData\weather.txt"
save_dir = r"C:\Users\kmalc\OneDrive\Pulpit\studiasemestrVII\aibd\lab2\AnalysisData"


with open(start_dir) as f: #otwieranie pliku i wczytywanie
    lines=f.readlines()

#print(lines[1])
#f.close()

# for elem in lines:
#     print(elem)

#lines = pd.read_csv(r"C:\Users\kmalc\OneDrive\Pulpit\studiasemestrVII\aibd\lab2\OriginalData\weather.txt",sep="  ",header=None)

#print(lines[0])
#df = pd.DataFrame(np.array(lines))

lista = []
for i in range(len(lines)):
    lista.append(lines[i].replace('PRCP','PRCPx'))
    lista[i] = lista[i].replace('MAX','MAXx')
    lista[i] = lista[i].replace('MIN','MINx')

column_ID_station_PRCP = []
column_year_PRCP = []
column_month_PRCP = []
column_day_PRCP = []
column_ID_station_TMAX = []
column_year_TMAX = []
column_month_TMAX = []
column_day_TMAX = []
column_ID_station_TMIN = []
column_year_TMIN = []
column_month_TMIN = []
column_day_TMIN = []
days = [i for i in range(1,32)]


for i in range(len(lines)):
    if lines[i].find('PRCP')!=-1:
        column_ID_station_PRCP.append(lines[i][0:11])
        column_year_PRCP.append(lines[i][11:15])
        column_month_PRCP.append(lines[i][15:17])
    if lines[i].find("TMAX")!=-1:
        column_ID_station_TMAX.append(lines[i][0:11])
        column_year_TMAX.append(lines[i][11:15])
        column_month_TMAX.append(lines[i][15:17])   
    if lines[i].find("TMIN")!=-1:
        column_ID_station_TMIN.append(lines[i][0:11])
        column_year_TMIN.append(lines[i][11:15])
        column_month_TMIN.append(lines[i][15:17])      

print(len(column_year_PRCP))
print(len(column_year_TMAX))
print(len(column_year_TMIN))

x = lines[0].find("TMAX")+5


looking_word = 'I'

li = []

for i in range(len(lines[0])):
    if lines[0].startswith(looking_word,i):
        #print(i)
        space = lines[0][:i].count(" ")
        #hello = space+1
        #print(hello)
        li.append(i)
print(li)

split_strings = []
n = 8
for index in range(x,len(lines[0]),n):
    split_strings.append(lines[index:index+n])
print(split_strings[0][0])





# os.chdir(save_dir)
# textfile = open('weather3.txt','w') #zamykanie pliku
# for elem in lista:
#     textfile.write(elem)

# textfile.close()




#print(df)


# raw_list =pd.read_csv(r"C:\Users\kmalc\OneDrive\Pulpit\studiasemestrVII\aibd\lab2\OriginalData\weather.txt",header=None)
# print(raw_list)


# string = 'lala jasiek necinski lala lol'

# looking_word = 'lala'

# li = []

# for i in range(len(string)):
#     if string.startswith(looking_word,i):
#         #print(i)
#         space = string[:i].count(" ")
#         hello = space+1
#         print(hello)
#         li.append(i)
# print(li)

# while(True):
#     break