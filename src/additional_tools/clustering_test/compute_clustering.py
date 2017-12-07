import data,functions,sys

# parameters
fMatch=sys.argv[1]
fLink=sys.argv[2]
nbLinks=sys.argv[3]
nbLinks=int(nbLinks)
nbsim=sys.argv[4]
nbsim=int(nbsim)
fOut=sys.argv[5]


# info genes
print "1) Read the list of genes..."
Match=data.readMatch(fMatch)
print "Number of Genes",len(Match.keys())


# info network
print "2) Read the list of links..."
ScorePair=data.getLinks(fLink,nbLinks)
print "Number of Pairs",len(ScorePair.keys())


# compute the sum of between the set of genes
print "3) Compute Sum of observations"
SumLinks=[]
SumLinks.append(functions.Compute_SumLinks(Match,ScorePair))

# compute the sum of weighted for random set
print "4) Simulations..."
for sim in range(nbsim):
	ListGeneNew=functions.RandomGen(Match)

	SumLinks.append(functions.Compute_SumLinks(ListGeneNew,ScorePair))

# report results
print "5) Report Results..."
data.reportPvalObs(fOut+"_pval",SumLinks)
data.reportSim(fOut+"_sum",SumLinks)




