#First, initialize the slices'number as p and cut times as n
#Then, use the while loop to find the 64 slices needs how many cut times are

#initialize the p and n from 0
#use the while loop with the functional relationship between p and n to find the answer
#print the answer







p = 0
n = 0
while p <= 64:
    n = n + 1
    p = (n**2+n+2)/2
print(p)
print(n)
