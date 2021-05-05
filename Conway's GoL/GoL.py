# Conway's Game of Life with a Random Seed
# Julia Hill, Samantha Cibere, Alex Hardjono, Gaurav Tenkila, Ryan Kaufmann

# Import statements
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import cProfile, pstats, io

# Creation of profiler to analyze time of methodology
pr = cProfile.Profile()
pr.enable()

# Introduce constants.
IFPS = 150            # Time between frames in ms
NUMFRAMES = 50      # Number of frames created

# Ask user for a the size of the square grid and generate the random seed.
while True:
    try:
        GridSize = int(input("What size of grid would you like? "))
        break
    except ValueError:
        print('The input value is not an integer.\n')
Grid = np.random.choice([0, 1], size=(GridSize, GridSize), p=[0.8, 0.2])

# Uses np.roll to count up all the neighbours of the grid points and returns the
# values as an array.
def getNumAliveNeighbours(grid):
    axis = (1, 0)
    liveneighbours = np.roll(grid, (1, 1), axis) + np.roll(grid, (1, 0), axis) \
    + np.roll(grid, (1, -1), axis) + np.roll(grid, (0, 1), axis) + \
    np.roll(grid, (0, -1), axis) + np.roll(grid, (-1, 1), axis) + \
    np.roll(grid, (-1, 0), axis) + np.roll(grid, (-1, -1), axis)
    return liveneighbours


# Imposes the conditions of Conway's Game of Life as follows:
# If a square is alive:
# - and has 2 or 3 neighbours, it stays alive , oh oh oh
# - otherwise, it dies
# If a square is dead:
# - and has 3 neighbours, it becomes alive
# - otherwise, it stays dead
# Produces the next array in the series and returns it as an array.
def updateGrid(grid):
    liveneighbours = getNumAliveNeighbours(grid)
    conditional = np.logical_or(np.logical_and(liveneighbours == 2, grid == 1),
                                np.logical_and(liveneighbours == 3, grid == 0),
                                np.logical_and(liveneighbours == 3, grid == 1))
    grid = np.where(conditional, 1, 0)
    return grid


# Calls above methods to generate the next array in the series. Uses the array
# to update the plot animation and move the animation forward. Returns the final
# animation in a list.
def getNextGrid(frames):
    global Grid
    gridcopy = np.copy(Grid)
    newgrid = updateGrid(gridcopy)
    AnimateGrid.set_array(newgrid * 255)
    Grid = newgrid
    return [AnimateGrid]


# Use the above functions and constants to generate an animation for Conway's
# Game of Life.
Fig, Ax = plt.subplots()
AnimateGrid = Ax.imshow(Grid * 255, animated=True, cmap = 'inferno')
Animate = ani.FuncAnimation(Fig, getNextGrid, frames=NUMFRAMES, interval=IFPS,
                            blit=True)
plt.show()

# Disable the profiler and export the stats to a .txt file.
pr.disable()
file = open("ProfilerStats.txt", 'w')
s = io.StringIO()
sortby = "tottime"
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
file.write(s.getvalue())
file.close()
