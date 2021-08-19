
import numpy as np



class Point:

    def __init__(self, x, y):
        self.coord = np.array([x, y]).astype('int')

    def __repr__(self):
        return '(%d, %d)' % (self.coord[0], self.coord[1])

    
    def __eq__(self, other):
        return np.array_equal(self.coord, other.coord)

    def __ne__(self, other):
        return not self.__eq__(other)


    def __add__(self, other):
        return Point(*(self.coord + other.coord))

    def __hash__(self):
        return hash((self.coord[0], self.coord[1]))

    def copy(self):
        return Point(self.coord[0], self.coord[1])
    
    def get_coord(self):
        return self.coord

    def get_x(self):
        return self.coord[0]

    def get_y(self):
        return self.coord[1]


    

    
if __name__ == '__main__':
    pass


