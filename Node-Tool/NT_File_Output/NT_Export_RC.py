#import libraies
import io
#Import Scripts from directory
from NT_Graph_Generation.NT_GraphGen import GenerateGraph
from NT_RC_Generation.NT_RcGen import GenerateRC

#Write to file
def WriteToFile(RCFile,nodeName):

    output=""
    for line in RCFile:
        output += (line+"\n")
    with io.open(('host'+nodeName+'.rc'), 'w', newline='\n') as f:
        f.write(output)

#User input
def SaveInput(nodeName):
    names = [""]
    ipAddresses = [""]


    names[0] = str(entry1.get())
    ipAddresses[0] = str(entry2.get())

    RCFile = GenerateRC(names[0],ipAddresses[0])

    WriteToFile(RCFile,names[0])
