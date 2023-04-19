def GenerateRC(node1Name,node1IP):
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