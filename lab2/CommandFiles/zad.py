import numpy as np
import pandas as pd 
import pathlib
import os
import re

start_dir = r"C:\Users\kmalc\OneDrive\Pulpit\studiasemestrVII\aibd\lab2\OriginalData\weather.txt"
save_dir = r"C:\Users\kmalc\OneDrive\Pulpit\studiasemestrVII\aibd\lab2\AnalysisData"

column_station_ID = []
column_year = []
column_month = []
column_headers = []
_maxsplit=31

with open(start_dir) as file: #stack

    lines = []
    data = file.readlines()

    for line in data:

        line_temp = line.replace('S', '').replace('-9999', '  -9999')
        line_temp = re.sub('O*I[^N]', '', line_temp)
        line_temp = line_temp.replace('D', '').replace('O', '').replace('B', '')
        line_splitted = re.split('\s{2,}', line_temp, maxsplit=_maxsplit)
        lines.append([int(x) for x in line_splitted[1:]])
        column_station_ID.append(line[0:12]) #bierzemy ID z każdej linii ze stringa
        column_year.append(line[11:15]) #jak wyzej
        column_month.append(line[15:17])
        column_headers.append(line[17:21])


dataframe = pd.DataFrame(lines, columns=[str(i) for i in range(1,32)])

dataframe = dataframe.replace(-9999, np.nan) #zamiana wartosci niemożliwych na notanumber

dataframe.insert(0, 'year', column_year)
dataframe.insert(1, 'month', column_month)
dataframe.insert(2, 'type', column_headers)
column_temp_max = dataframe[dataframe['type']=='TMAX']
column_temp_min = dataframe[dataframe['type']=='TMIN']
column_prcp = dataframe[dataframe['type']=='PRCP']

column_prcp_melted = column_prcp.melt(id_vars=['year','month','type'], var_name='day', value_name='PRCP')
column_prcp_melted.dropna(inplace=True)
column_prcp_melted.insert(0, 'date', pd.to_datetime(column_prcp_melted[['year', 'month', 'day']]))
column_prcp_melted.drop(['year', 'month', 'day', 'type'], axis=1, inplace=True)

column_min_melted = column_temp_min.melt(id_vars=['year','month','type'], var_name='day', value_name='TMIN')
column_min_melted.dropna(inplace=True)
column_min_melted.insert(0, 'date', pd.to_datetime(column_min_melted[['year', 'month', 'day']]))
column_min_melted.drop(['year', 'month', 'day', 'type'], axis=1, inplace=True)

column_max_melted = column_temp_max.melt(id_vars=['year','month','type'], var_name='day', value_name='TMAX')
column_max_melted.dropna(inplace=True)
column_max_melted.insert(0, 'date', pd.to_datetime(column_max_melted[['year', 'month', 'day']]))
column_max_melted.drop(['year', 'month', 'day', 'type'], axis=1, inplace=True)


os.chdir(save_dir) #zapis do pliku csv do odpowiedniego folderu
column_prcp_melted.to_csv('DailyPRCP.csv')
column_min_melted.to_csv('DailyTempMIN.csv')
column_max_melted.to_csv('DailyTempMAX.csv')


