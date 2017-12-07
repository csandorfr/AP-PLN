

def readMatch(file):
	f=open(file,'r')
	Match={}
	for line in f:
		line=line.rstrip().split('\t')
		Gene=line[0]
		Match.setdefault(Gene,[])
		for i in range(1,len(line)):
			Match[Gene].append(line[i])
	f.close()
	return Match

def reportMatch(file,Match):
	f=open(file,'w')
	for Gene in Match.iterkeys():
		f.write("%s" % (Gene))
		for Gene2 in Match[Gene]:
			f.write("\t%s" % (Gene2))
		f.write("\n")
		
	f.close()

def getSize(file):
	f=open(file,'r')
	InfoSize={}
	for line in f:
		line=line.rstrip().split("\t")
		Gene=line[0]
		Size=float(line[1])
		InfoSize[Gene]=Size
	f.close()
	return InfoSize


def reportPvalObs(file,SumLinks):
	f=open(file,'w')
	nbtime,nbtotal=0,0
	for i in range(1,len(SumLinks)):
		if SumLinks[i] >= SumLinks[0]:
			nbtime+=1
		nbtotal+=1
	pval=float(nbtime)/float(nbtotal)
	f.write("%s\t%s\t%s\n" %(len(SumLinks)-1,SumLinks[0],pval))
	f.close()

def reportSim(file,SumLinks):
        f=open(file,'w')
        for Sim in SumLinks:
        	f.write("%s\n" %(Sim))
        f.close()



def getGene(file):
	f=open(file,'r')
	ListGene={}
	for line in f:
		line=line.rstrip()
		ListGene[line]=1
	f.close()
	return ListGene



def getLinks(file,nbLinks):
	f=open(file,'r')
	ScorePair={}
	n=0
	for line in f:
		line=line.rstrip().split("\t")
		Gene1=line[0]
		Gene2=line[1]
		Score=float(line[2])
		Pair=Gene1+":"+Gene2
		n+=1
		if n> nbLinks: break
		ScorePair.setdefault(Gene1,{})
		ScorePair[Gene1][Gene2]=Score
	f.close()
	return ScorePair
	

