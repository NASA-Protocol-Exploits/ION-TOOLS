#import libraies
from re import L
from tkinter import ttk
import tkinter as tk
from xml.dom.minicompat import NodeList
import igraph as ig
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from NT_Graph_Generation.NT_GraphGen import GenerateGraph


#Define a function to close the window with confirmation window
def DrawGraph(UI,networkMap):
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