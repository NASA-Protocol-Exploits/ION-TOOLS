import io
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import igraph as ig

#global varibles
input_text = ''

nodeName = ""

#Stuff for generating Graph

def GenerateGraph(names):

    g = ig.Graph(directed=False)

    # Add 5 vertices
    g.add_vertices(5)

    # Add ids and labels to vertices
    for i in range(len(g.vs)):
        g.vs[i]["id"]= i
        g.vs[i]["label"]= str(names[0])  #str(i)

    # Add edges
    g.add_edges([(0,2),(0,1),(0,3),(1,2),(1,3),(2,4),(3,4),(1,4)])

    # Add weights and edge labels
    weights = [8,6,3,5,6,4,9]
    g.es['weight'] = weights
    g.es['label'] = weights

    visual_style = {}

    # Set bbox and margin
    visual_style["bbox"] = (400,400)
    visual_style["margin"] = 27

    # Set vertex colours
    visual_style["vertex_color"] = 'white'

    # Set vertex size
    visual_style["vertex_size"] = 45

    # Set vertex lable size
    visual_style["vertex_label_size"] = 22

    # Don't curve the edges
    visual_style["edge_curved"] = True

    # Set the layout
    my_layout = g.layout_lgl()
    visual_style["layout"] = my_layout

    layout = g.layout(layout='auto')
    fig, ax = plt.subplots()
    ig.plot(g, target=ax)
    
    return fig

#Write to file

def writeToFile(RCFile,nodeName):

    output=""
    for line in RCFile:
        output += (line+"\n")
    with io.open(('host'+nodeName+'.rc'), 'w', newline='\n') as f:
        f.write(output)


def generateRC(node1Name,node1IP):
    RCFile = []
    #Each new Append is a new line
    #Ion Secadmin Segment
    RCFile.append("## begin ionsecadmin")
    RCFile.append("1")
    RCFile.append("## begin ionsecadmin")
    RCFile.append("")
    #Ionadmin Segment
    RCFile.append("## begin ionadmin")
    RCFile.append("1 "+node1Name+ '')
    RCFile.append("s")
    RCFile.append("")
    RCFile.append("m horizon +0")
    RCFile.append("")
    # Series of 1-hour contacts

    # WIll require loop here for all nodes defined by user
    RCFile.append("a contact +0 +3600 "+node1Name+" "+node1Name+" "+"10000000 1")

    # WIll require loop here for all nodes defined by user
    RCFile.append("a range +0 +3600 "+node1Name+" "+node1Name+"1")


    #define limits
    RCFile.append("m production 10000000")
    RCFile.append("m consumption 10000000")

    RCFile.append("## end ionadmin")
    RCFile.append("")

    #ltpadmin Segment
    RCFile.append("## begin ltpadmin")
    RCFile.append("1 32")
    RCFile.append("")

    # LTP span for loopback connection
    RCFile.append("a span "+node1Name+" 32 32 1400 10000 1 'udplso "+node1IP+":1113' 300")
    RCFile.append("")
    RCFile.append("s 'udplsi "+node1IP+":1113'")
    RCFile.append("## end ltpadmin")
    RCFile.append("")


    #Bpadmin Segment
    RCFile.append("## begin bpadmin")
    RCFile.append("1")
    RCFile.append("a scheme ipn 'ipnfw' 'ipnadminep'")
    #Any more than 1 is unnessary but is good practice as they are essentially ports
    RCFile.append("a endpoint ipn:"+node1Name+".0 q")
    RCFile.append("a endpoint ipn:"+node1Name+".1 q")
    RCFile.append("a endpoint ipn:"+node1Name+".2 q")
    RCFile.append("")
    # TCP protocol declaration
    RCFile.append("a protocol tcp 1400 100")
    RCFile.append("")
    # LTP and TCP inducts
    #self Inducts
    RCFile.append("a induct ltp "+node1Name+" ltpcli")
    RCFile.append("a induct tcp "+node1IP+":4556 tcpcli")
    RCFile.append("")
    #self OutDuct
    RCFile.append("a outduct ltp "+node1Name+" ltpclo")
    RCFile.append("")
    #External Outducs
    #eg: a outduct ltp 200 ltpclo

    # TCP outduct to node 100
    #eg: a outduct tcp 192.168.0.98:4556 ''
    RCFile.append("")
    RCFile.append("s")
    RCFile.append("## end bpadmin")
    RCFile.append("")

    #Begin Ipnadmin Segment
    RCFile.append("## begin ipnadmin")
    RCFile.append("a plan "+node1Name+" ltp/"+node1Name)
    RCFile.append("")

    #Begin IPN Plans of additional Nodes
    
    #eg: a plan 100 tcp/192.168.0.98:4556
    
    RCFile.append("")
    RCFile.append("## end ipnadmin")

    return RCFile

#User input

def save_input(nodeName):
    names = [""]
    ipAddresses = [""]


    names[0] = str(entry1.get())
    ipAddresses[0] = str(entry2.get())

    RCFile = generateRC(names[0],ipAddresses[0])

    writeToFile(RCFile,names[0])

    fig = GenerateGraph(names)


    graph = FigureCanvasTkAgg(fig, window)
    graph.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)


#Tkinter GUI

window = tk.Tk()

message1 = tk.Label(window, text="Enter Node Name")
message1.pack()


entry1 = tk.Entry(window, width=40)
entry1.pack()

message1 = tk.Label(window, text="Enter Node IP")
message1.pack()

entry2 = tk.Entry(window, width=40)
entry2.pack()


button = tk.Button(window, text="Save Input", command=lambda:save_input(nodeName))
button.pack()


#graph = FigureCanvasTkAgg(fig, window)
#graph.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

nodeName = "100"

window.mainloop()