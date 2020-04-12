import matplotlib.pyplot as plt
from rwmodule import RandomWalk
#simulating the random walk then plotting the graph
while True:
    ch = input("Do you want another one[y/n]")
    if ch == 'n':
        break
    rw = RandomWalk()
    rw.walk()
    ptnumber = list(range(5001))
    plt.scatter(rw.x_position,rw.y_position,s=5,c=ptnumber,cmap=plt.cm.Blues)
    plt.scatter(0,0,s=10,c='green')
    plt.scatter(rw.x_position[-1],rw.y_position[-1],s=10,c='red')
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
