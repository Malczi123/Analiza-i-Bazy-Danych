import numpy as np
import pandas


p1 = np.array(['Kacper','Malczewski',22,'Male']) #tworzenie dowolnych rekordow
p2 = np.array(['Maciej','Morgalla',22,'Male'])
p3 = np.array(['Anna','Nowak',28,'Female'])
p4 = np.array(['Grazyna','Zarko',52,'Female'])
p5 = np.array(['Nicolas','Smith',15,'Male'])

df = pandas.DataFrame(np.array([p1,p2,p3,p4,p5]),columns=['Name','Surname','Age','Sex']) #tworzenie dataframe

print('\nWyswietlanie DataFrame\n')
print(df) #wyswietlanie dataframe
print('\nWyswietlanie DataFrame.info\n')
print(df.info(verbose=False)) #wyswietlenie informacji o danych pandas info
print("\nWyswietlanie DataFrame.describe\n")
print(df.describe())
print('\nWyswietlanie DataFrame.head dla n=3\n')
print(df.head(n=3))