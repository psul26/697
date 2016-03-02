import sys
unrolls = int(sys.argv[3])
d = {} #general dictionary of all info if needed
DFF = {} #DFF output cur state indexs to name of input next state
nodeToNumber = {}#node name indexs to gate number
gateNumbers ={} #keeps track of number of gates per type
ands = {} #output name indexs to input1 and input2 names resp
nots = {} #output name indexs to input name
targetState = ""
listDFF = []
def numberOfClauses():
	return (gateNumbers["DFF"]+(3*gateNumbers["AND"]+2*gateNumbers["NOT"])*unrolls+gateNumbers["DFF"]+2*gateNumbers["DFF"]*(unrolls-1))
def numberOfVariables():
	return len(nodeToNumber)*unrolls



reader = open(sys.argv[1],"r")
count = 1
gateNumbers["AND"] = 0
gateNumbers["NOT"] = 0
gateNumbers["DFF"] = 0
gateNumbers["INPUTS"] = 0
for line in reader.readlines():	
	if not line == '\n':
		line = line.replace("="," ")
		line = line.replace("("," ")
		line = line.replace(")"," ")
		line = line.replace(","," ")
		line = str(line).split()
	
		if line[0] == "INPUT":
			d[line[1]] = line[0],0
			nodeToNumber[line[1]] = count
			count = count + 1
			gateNumbers["INPUTS"] = gateNumbers["INPUTS"] + 1
		if line[1] == "AND":
		
			d[line[0]] = line[1],line[2],line[3]
			nodeToNumber[line[0]] = count
			count = count + 1
			ands[line[0]] = line[2],line[3] #output indexs to first then second inputs
			gateNumbers["AND"] = gateNumbers["AND"] + 1
		if line[1] == "NOT":
		
			d[line[0]] = line[1],line[2]
			nodeToNumber[line[0]] = count
			gateNumbers["NOT"] = gateNumbers["NOT"] + 1
			nots[line[0]] = line[2] #output node indexs to input of the not gate
			count = count + 1
		if line[1] == "DFF":
			DFF[line[0]] = line[2]
			d[line[0]] = line[1],line[2],0
			nodeToNumber[line[0]] = count
			gateNumbers["DFF"] = gateNumbers["DFF"] + 1
			listDFF.append(str(line[0]))
			count = count + 1
			
reader.close()
if len(sys.argv) == 4:
	reader = open(sys.argv[2],"r")
	for line in reader.readlines():
		
		if not line == '\n':	
			targetState = str(line).strip()
	
reader.close()

writer = open("out","w")

writing = True
numberOfNodes = len(nodeToNumber)
while writing:
	writer.write("p cnf "+str(numberOfVariables())+" "+str(numberOfClauses())+"\n")
	
	
	writer.write("c initial states start\n")
	for i in DFF:
		writer.write("-"+str(nodeToNumber[i])+" "+"0\n")
	writer.write("c initial states end\n")
	writer.write("c  \n")
	
	for i in xrange(0,unrolls):
		writer.write("c unroll of the transition relation: " +str(i)+"\n")
		writer.write("c \n")
		writer.write("c ands begin for loop\n")
		for x in ands:
			
			writer.write(str(nodeToNumber[ands[x][0]]+(i)*numberOfNodes)+" -"+str(nodeToNumber[x]+(i)*numberOfNodes)+" 0"+"\n")
			writer.write(str(nodeToNumber[ands[x][1]]+(i)*numberOfNodes)+" -"+str(nodeToNumber[x]+(i)*numberOfNodes)+" 0"+"\n")
			writer.write("-"+str(nodeToNumber[ands[x][0]]+(i)*numberOfNodes)+" -"+str(nodeToNumber[ands[x][1]]+(i)*numberOfNodes)+" "+str(nodeToNumber[x]+(i)*numberOfNodes)+" 0"+"\n")
			writer.write("c ANDS for loop done\n")
		writer.write("c nots for loop begin\n")
		writer.write("c \n")
		for m in nots:
			
			writer.write("-"+str(nodeToNumber[nots[m]]+(i)*numberOfNodes)+" -"+str(nodeToNumber[m]+(i)*numberOfNodes)+" 0"+"\n")
			writer.write(str(nodeToNumber[nots[m]]+(i)*numberOfNodes)+" "+str(nodeToNumber[m]+(i)*numberOfNodes)+" 0"+"\n")
		writer.write("c nots for this loop ends\n")
		writer.write("c \n")
		#now time for the linking
		writer.write("c linking begins \n")
		if not i==0:
			for j in listDFF:
				writer.write("-"+str(nodeToNumber[DFF[j]]+(i-1)*numberOfNodes) +" "+ str(nodeToNumber[j]+i*numberOfNodes)+" 0\n")
				writer.write(str(nodeToNumber[DFF[j]]+(i-1)*numberOfNodes) +" -"+ str(nodeToNumber[j]+i*numberOfNodes)+" 0\n")
		writer.write("c linking ends \n")
		writer.write("c loop: "+str(i)+" ends \n")
	writing =False
writer.write("c \n")
writer.write("c begin target states \n")
num = 0

for h in listDFF:
	if targetState[num] == "0":
		writer.write("-"+str(nodeToNumber[DFF[h]]+i*numberOfNodes)+" 0\n")
	if targetState[num] == "1":
		writer.write(str(nodeToNumber[DFF[h]]+i*numberOfNodes)+" 0\n")
	num = num + 1


