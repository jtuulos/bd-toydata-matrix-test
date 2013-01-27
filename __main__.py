from bitdeli import profiles
from bitdeli.widgets import Widget
import random

for profile in profiles():
    pass

class Matrix(Widget):
    defaults = {'size': [3,3]}

size = 100
data = [[random.random() for x in range(size)] for y in range(size)]
    
Matrix(size=[12,6],
       color=2,
       data=data)
