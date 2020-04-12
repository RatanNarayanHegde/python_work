from random import choice

class RandomWalk():
    """A Class that will generate random walks"""
    def __init__(self,numberofwalk=5000):
        """Initialize the number of walks and also set initial position at 0,0"""
        self.num_pts = numberofwalk

        #initial position
        self.x_position = [0]
        self.y_position = [0]
    
    def walk(self):
        """simulate the walk"""
        for _ in range(self.num_pts):
            #choosing random values for next walk
            x_direc = choice([1,-1])
            x_dis = choice([1,2,3,4,5])
            x_pos = x_direc*x_dis

            #chooding values for y of next walk
            y_direc = choice([1,-1])
            y_dis = choice([1,2,3,4,5])
            y_pos = y_direc*y_dis

            self.x_position.append(self.x_position[-1]+x_pos)
            self.y_position.append(self.y_position[-1]+y_pos)

