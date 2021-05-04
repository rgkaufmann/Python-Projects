import matplotlib.pyplot as plt
import numpy as np


gridSize = input("What size of grid would you like? ")

grid = np.random.randint(0, 2, size=(gridSize, gridSize))

def getLiveNeighbours():

# funcAnimation function, called at each frame
# first argument will be the next value in frames
def getNextGrid(frameNum, *fargs):
