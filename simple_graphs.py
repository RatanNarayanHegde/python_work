import matplotlib.pyplot as plt

numbers = list(range(0,101))
squares = [x**2 for x in numbers]

plt.scatter(numbers,squares,s=5,c=squares,cmap=plt.cm.Reds)
plt.title("Square Numbers",fontsize=14)
plt.xlabel("Numbers",fontsize=12)
plt.ylabel("Square Numbers",fontsize=12)
plt.tick_params(axis='both',labelsize=10)
plt.axis([0,110,0,11000])
plt.show()