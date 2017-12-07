import data,sys,functions

# parameters
fLink=sys.argv[1]
nbLinks=sys.argv[2]
nbLinks=int(nbLinks)
fGene=sys.argv[3]
NbGene=sys.argv[4]
NbGene=int(NbGene)
fSize=sys.argv[5]
fOut=sys.argv[6]


# info network
print "1) Read the list of links..."
ScorePair=data.getLinks(fLink,nbLinks)
print "Number of Pairs",len(ScorePair.keys())

# list of genes
print "2) Read the list of genes..."
ListGene=data.getGene(fGene)
print "Number of Gene",len(ListGene)

# get the coding sequence length
print "3) Read Genes Size"
InfoSize=data.getSize(fSize)
print "Number of Genes",len(InfoSize.keys())

# compute the sum of links for each gene in the network
print "4) Compute the sum of links of each gene"
ScoreGene=functions.ScoreGeneTot(ScorePair)
print "Number of Links",len(ScoreGene.keys())

# match genes
print "5) Match Gene one size and network connectivity"
Match=functions.Match(ScoreGene,NbGene,InfoSize,ListGene)
print "Number of Gene",len(Match.keys())

# report genes
print "6) Report Match Gene"
data.reportMatch(fOut,Match)
