import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("Practical7")
covid_data = pd.read_csv("full_data.csv")
covid_data.head(5)
covid_data.info()
print(covid_data.describe())
print(covid_data.iloc[0, 1])
print(covid_data.iloc[2, 0:5])
print(covid_data.iloc[0:2, :])
print(covid_data.iloc[0:10:2, 0:5])
print(covid_data.iloc[0:3, [0, 1, 3]])
my_columns = [True, True, False, True, False, False]
print(covid_data.iloc[0:3, my_columns])
print(covid_data.loc[2:4, "date"])
print(covid_data.loc[0:81, "total_cases"])
a = []
for location in covid_data.loc[:, 'location']:
    a.append(location == 'Afghanistan')
print(covid_data.loc[a, "total_cases"])
b = []
for location in covid_data.loc[:, 'location']:
    b.append(location == 'China')
c = covid_data.iloc[b, [0, 2, 3]]
d = np.mean(c.loc[:, "new_cases"])
print(d)
e = np.mean(c.loc[:,"new_deaths"])
print(e)
print(e/d) #the the proportion of new cases that kill the infected person
case = c.loc[:,"new_cases"]
death = c.loc[:,"new_deaths"]
date = c.loc[:,"date"]
plt.boxplot((case,death),labels=('case','death'))
plt.show()
plt.plot(date,case,"bo")
plt.show()
"""plt.xticks(date.iloc[0:len(date):4],rotation=-90)"""
f = []
for location in covid_data.loc[:, 'location']:
    f.append(location == 'Spain')
g = covid_data.iloc[f, [0, 2, 4]]
newcase = g.loc[:,"new_cases"]
allcase = g.loc[:,"total_cases"]
plt.plot(newcase,allcase,"b+")
plt.show()
