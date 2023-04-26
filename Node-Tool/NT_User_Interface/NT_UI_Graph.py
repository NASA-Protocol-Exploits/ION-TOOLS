#import libraies
import tkinter as tk
import igraph as ig
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from NT_Graph_Generation.NT_GraphGen import GenerateGraph



networkMap = ig.Graph(directed=False)
#Create Initial vertice - Minumum of 1 required
networkMap.add_vertices(1)


#Define a function to close the window with confirmation window
def DrawGraph(UI,nodes):
    #Create Higher level Window
    graphWindow = tk.Toplevel()
    graphWindow.title('Confirm Exit')
    graphMessage1 = tk.Label(graphWindow, text="Network Map")
    graphMessage1.pack()
    names = [""]
    ipAddresses = [""]
    names[0] = str(100)
    fig = GenerateGraph(networkMap,names)
    graph = FigureCanvasTkAgg(fig, graphWindow)
    graph.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    closeButton = tk.Button(graphWindow, width=20 ,text="Close Graph", command=lambda:graphWindow.destroy())
    closeButton.pack()