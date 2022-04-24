#import matplotlib
#creat a new dictionary to contain the information in two lists
# print the dictionary
# draw the plot 



import matplotlib.pyplot as plt
import numpy as np

parental_age = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
chd = [1.03, 1.07, 1.11, 1.17, 1.23, 1.32, 1.42, 1.55, 1.72, 1.94]
print(parental_age)  # question 1
print(chd)  # question 1
plt.scatter(parental_age, chd, marker='o') # question 2
plt.xlabel("Paternal age")
plt.ylabel("Risk for CHD")
plt.show()  # question 2
n = int(input())
i = 0
while i < 9:
    m = parental_age[i]
    if m == n:
        print(chd[i])
    i = i+1  # question 3
