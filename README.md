# Diaphony
The data and plotting script for point sets with a minimized diaphony

This project contains the datapoints for the configuration of N=1 to 20 points with minimal diaphony, in addition to a simple script to view them. The points are contained in the 'Points' folder, with their x, y, and z coordinates in a .csv file with the corresponding filename. 

To view the points simply execute the Run.py script and specify the number of points that one wishes to see in the prompt. A new window will appear in which the points and some predefined distances are animated. Note that for each figure, all lines with identical colours are of equal distance. The figure can be rotated by the user by clicking and dragging the figure. 
The matplotlib window contains two buttons: the 'Pause/Resume' button, which pauses or resumes the animation, and the 'Quit' button, which terminates the window. IMPORTANT, always terminate the window via the 'Quit' button, otherwise a new empty window will simply appear, forcing the user to terminate the program. This is unfortunate side effect simultaneously implementing an animation and manual rotation. A fix may be implemented in the future. 
