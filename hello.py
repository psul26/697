import csv
import sys
############################
#Parser

d ={}
inDict ={}
nextStateDict={}
currentStateDict={}
nodeDict={}
DFFDic ={}
visited ={}
truthTable ={}
toBeExplored = {}
inputs = []
DFFS = []

def getNode(node):
	if d[node][0] == "INPUT":
		return int(inDict[node])
	if d[node][0] == "AND":
		return int(getNode(d[node][1])) & int(getNode(d[node][2]))
	if d[node][0] == "NOT":
		return int(not((getNode(d[node][1]))))
	if d[node][0] == "DFF":
		return int(currentStateDict[node])
		
def setInputs(inputString):
		#print (" set ins called ", inputString)
		inputString = str(inputString)
		count = 0
		for i in inputs:
			 inDict[i.name] = inputString[count] 
			 count = count +1
def setStates(inputStr):
	count = 0
	for i in DFFS:
		currentStateDict[i.name] = inputStr[count]
		count = count + 1
def getNewStates():
	newS = ""
	
	for i in DFFS:
		newS = newS + str(getNode(DFFDic[i.name]))
	return newS
	
def clockSignal():
	for i in DFFS:
		currentStateDict[i.name] = getNode(DFFDic[i.name])
	print("did it trasistions" , currentStateDict)
	
def getCurrentStates():
	stNew = ""
	
	for i in DFFS:
		stNew = stNew + currentStateDict[i.name]
	return stNew
		
		  
class Input:	
	
	
	def __init__(self,name,out):
		self.name = name
		self.out = out
	
		
		
class DFF:	
	
	def __init__(self,name,out,in1):
		self.name = name
		self.out = out
		self.in1 = in1
		
class AND:	
	
	def __init__(self,name,out,in1,in2):
		self.name = name
		self.out = out
		self.in1 = in1
		self.in2 = in2
		
class NOT:	
	
	def __init__(self,name,out,in1):
		self.name = name
		self.out = out
		self.in1 = in1
		
#print(me.name,me.i)

reader = open(sys.argv[1],"r")


#	reader = csv.reader(csvfile)

for line in reader.readlines():	
	if not line == '\n':
		line = line.replace("="," ")
		line = line.replace("("," ")
		line = line.replace(")"," ")
		line = line.replace(","," ")
		line = str(line).split()
	
		if line[0] == "INPUT":
			d[line[1]] = line[0],0
			inDict[line[1]] = 0
			inputs.append(Input(line[1],0))
		if line[1] == "AND":
		
			d[line[0]] = line[1],line[2],line[3]
		if line[1] == "NOT":
		
			d[line[0]] = line[1],line[2]
		if line[1] == "DFF":
			DFFS.append(DFF(line[0],line[0],line[2]))
			d[line[0]] = line[1],line[2],0
			currentStateDict[line[0]] = 0
			DFFDic[line[0]] = line[2]
targetState = ""
reader.close()
if len(sys.argv) == 3:
	reader = open(sys.argv[2],"r")
	for line in reader.readlines():
		if not line == '\n':	
			targetState = str(line).strip()
	
reader.close()









for i in xrange(0,2**len(inDict)):
	l = bin(i)[2:]
	while len(l) < len(inDict):
		l = '0'+l
		
	
	truthTable[i] = l


searching = True
nextState = ""
begState =""
s =""
for i in currentStateDict:
	begState = begState+str(currentStateDict[i])

toBeExplored[begState] =True	
visited[begState] = True


while searching:
	curState = str(toBeExplored.keys()[0])
	visited[str(curState)] = True 
	#print ("to be explored keys" ,toBeExplored.keys()[0])
	setStates(toBeExplored.keys()[0])
	del toBeExplored[curState]
	for i in xrange(0,len(truthTable)):
		#print("before i ", truthTable[i])
		setInputs(truthTable[i])
		
		stateString = getNewStates();
		
			
			
		#print("input ", i, "current states ", curState, "next State ", stateString)
		if stateString not in (visited or toBeExplored):
			toBeExplored[(stateString)] = True
	
		
		if targetState in (visited or toBeExplored):
			print ("target state: "+targetState+ " was reached")
			break			

	if len(toBeExplored) == 0:
		searching = False
print visited
if targetState not in (visited or toBeExplored) and (len(sys.argv) == 3):
	print ("Target state ",targetState, " not found" )


		
		
        
