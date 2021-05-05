# Conway's Game of Life with a Random Seed
# Julia Hill, Samantha Cibere, Alex Hardjono, Gaurav Tenkila, Ryan Kaufmann

# Import statments
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import cProfile, pstats, io

# Creation of profiler to analyze time of methodology
pr = cProfile.Profile()
pr.enable()

# Introduce constants
FPS = 30            # Time between frames in ms
NUMFRAMES = 1000    # Number of frames created

# Ask user for a the size of the square grid and generate the random seed
while True:
    try:
        GridSize = int(input("What size of grid would you like? "))
        break
    except ValueError:
        print('The input value is not an integer.\n')
Grid = np.random.choice([0, 1], size=(GridSize, GridSize), p=[0.6, 0.4])

def getNumAliveNeighbours():
    liveneighbours = np.zeros(size=(Gridsize, Gridsize))
    for i in range(len(Gridsize)):
        for j in range(len(Gridsize)):

# if alive:
# - and has 2 or 3 neighbours: stay alive , oh oh oh
# - else dies
# if dead:
# - and has 3 neighbours: become alive
# - else: stay dead

def updateGrid(grid):
    liveneighbours = getNumAliveNeighbours(grid)


# funcAnimation function, called at each frame
# first argument will be the next value in frames
def getNextGrid(frames):
    gridcopy = np.copy(Grid)
    newgrid = updateGrid(gridcopy)
    AnimateGrid.set_array(newgrid)
    return [AnimateGrid]

# Use the above functions and constants to generate an animation for Conway's
# Game of Life
Fig, Ax = plt.subplots()
AnimateGrid = Ax.imshow(Grid * 255, animated=True)
Animate = ani.FuncAnimation(Fig, getNextGrid, frames=NUMFRAMES, interval=FPS,   # Need to define getNextGrid
                            blit=True)
plt.show()

# Disable the profiler and export the stats to a .txt file
pr.disable()
file = open("ProfilerStats.txt", "w")
s = io.StringIO()
sortby = 'tottime'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
file.write(s.getvalue())
file.close()
