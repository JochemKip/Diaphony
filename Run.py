import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import pandas as pd
import pathlib

n = int(input('The distribution of how many points would you like to see (between 1 and 20)?\n'))
while not n in [i for i in range(1, 23)]:
    n = int(input('The number of points must be between 1 and 20. Please provide a new number.'))

path = f'{pathlib.Path(__file__).parent.resolve()}/Points/{n}.csv'

#Initialize state for the pause and stop buttons and how many different distances need to be drawn for each set of points
pause = False
stop = False 

# Set which distances are drawn for each set of optimized points
n_dists = {1:0, 2:[1], 3:[1], 4:[1], 5:[1,2], 6:[1], 7:[1,2], 8:[1,2], 9:[1,2,3], 10:[1,2], 11:[1,2,3,4,7], 12:[1], 13:[1,2,3,4,5,6], 14:[1,2,3], 15:[4,9,13], 16:[5,8], 17:[3,4,5,6], 18:[1,2,4,6], 19:[1,2,3,4,5], 20:[1,2]}

#Computes the inner products of all points, ranging from cos(theta) = -1 to 1
def compute_inprods(df):
    inprods = {}
    for i in df.index:
        for j in df.index:
            inprods[(i,j)] = np.matmul(np.array(df.loc[i]), np.array(df.loc[j]))
    return inprods

#Function to switch the Pause variable to True or False on click
def pause_button(event):
    global pause
    pause ^= True

#Function to change the stop variable to False when clicked
def stop_button(event):
    global stop
    stop = True

#Read in the N points from a csv file
y = pd.read_csv(path, header = 0)

#List of the computed inner products
inprods = compute_inprods(y)

#The bins and data needed in order to draw lines of equal length later. The odd number of bins are chosen in order to avoid boundary effects for orthogonal points
data, bins = np.histogram(list(inprods.values()), 49)

#Obtain a list of all the bins which have non-zero entries
nonzero_bins = []
for i, entry in enumerate(data):
    if entry != 0:
        nonzero_bins.append([bins[i], bins[i+1]])

#Initialize the 3D plot and hide the axis
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax._axis3don = False

#Draw the points
ax.scatter(y['x'], y['y'], y['z'], s = 100, c = 'black')

#The various colours used to indicate lines between points of equal length
cmap_i = ['red', 'blue', 'black', 'green', 'pink', 'gray']

#Draw the relevant lengths
for i,j in inprods:
    #avoid double couting
    if i <= j:
        continue
    else:
        #get the length between two points
        ab = inprods[(i,j)]
        for k, bin_edges in enumerate(nonzero_bins[::-1]):
            #Check in which the bin the length falls
            if ab >= bin_edges[0] and ab <= bin_edges[1]:
                #The number of different lengths drawn depends on the number of points; regular figures require fewer different distances
                if k in n_dists[n]:
                    plt.plot([y.loc[i]['x'],y.loc[j]['x']], [y.loc[i]['y'],y.loc[j]['y']], [y.loc[i]['z'],y.loc[j]['z']], c = cmap_i[n_dists[n].index(k)])
                else:
                    continue
            else:
                continue

#Create the pause/resume button
ax_pause = fig.add_axes([0.7, 0.05, 0.18, 0.075])
bpause = Button(ax_pause, 'Pause/Resume')
bpause.on_clicked(pause_button)

#Create the stop button
ax_stop = fig.add_axes([0.5, 0.05, 0.1, 0.075])
bstop = Button(ax_stop, 'Quit')
bstop.on_clicked(stop_button)

#Create the animation to rotate the viewing angle around the figure
ax.view_init(90, 30)
ax.set_aspect('equal')
while not stop:
    if not pause:
        ax.view_init(ax.elev-0.5, ax.azim+1)
        plt.draw()
        plt.pause(.002)
    else:
        ax.view_init(ax.elev, ax.azim)
        plt.draw()
        plt.pause(.002)