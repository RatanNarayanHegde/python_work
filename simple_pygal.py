from random import randint
import pygal
class Die():
    """This will simulate the Die"""
    def __init__(self,num_sides=6):
        """initializes the dies with default number of sides being 6 """
        self.numsides = num_sides
    
    def roll(self):
        """ Simulate the rolling of die"""
        res = randint(1,self.numsides)
        return res

d6 = Die()
results =[]
for _ in range(100):
    results.append(d6.roll())

frequencies = []
for value in range(1,7):
    frequencies.append(results.count(value))

hist = pygal.Bar()
hist.title = "Result of rolling dies 100 times"
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "Results"
hist.y_title = "frequencies"
hist.add('D6',frequencies)
hist.render_to_file('die_visuals.svg')