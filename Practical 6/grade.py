import matplotlib.pyplot as plt
import numpy as np

marks = [45, 36, 86, 57, 53, 92, 65, 45]

print(sorted(marks))  # question 1
plt.boxplot(marks)  # question2
plt.title("Marks")
plt.show()  # question2

i = 0
sum_marks = 0
length = len(marks)
print(str(length))
while i < length - 1:
    sum_marks += marks[i]
    i=i+1
print("The average mark of Rob is "+str(sum_marks/length))
if sum_marks/length < 60:
    print("he has not passed")  # question3
else:
    print(" he has passed")  # question3
