import numpy as np
import matplotlib.pyplot as plt

# list manipulation
'''
x = [10,23,41,23,5,3,234]
y = [n/5 for n in x]
print("\nx: {}, y: {}".format(x,y))
a = np.array(x)
b = a/5
print("\na: {}, b: {}".format(a,b))
'''

# plotting sin and cos

'''
x = np.linspace(0, 20, 1000)
y1 = np.sin(x)
y2 = np.cos(x)

zero = np.zeros(1000) 

plt.plot(x , y1, "-g", label="sine")
plt.plot(x , y2, "-b", label="cos")
plt.plot(x , zero, "-r", label="zero")

plt.legend(loc="upper right")

plt.show()
'''

salary = np.fromfile("salaries.txt", sep=",", dtype=int)
names = np.genfromtxt("names.txt", dtype=str, delimiter=",")

x = np.arange(len(names))
plt.bar(x, salary, align="center")
plt.xticks(x, names)
plt.xlabel("Names")
plt.ylabel("Salaries")
plt.title("Salaries of the top 10 richest people in the world")
plt.show()
