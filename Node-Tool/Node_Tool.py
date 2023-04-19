#import libraies
import igraph as ig

#Import Scripts from directory
from NT_User_Interface.NT_UI import LoadGUI

#global varibles

networkMap = ig.Graph(directed=False)
#Create Initial vertice - Minumum of 1 required
networkMap.add_vertices(1)

#Load Graphical Interface

GUI = LoadGUI(networkMap)

GUI.mainloop()