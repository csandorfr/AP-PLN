import random
import operator

def ScoreGeneTot(Score):
        ScoreGene={}
        for Gene1 in Score.iterkeys():
                for Gene2 in Score[Gene1].iterkeys():
                        ScoreGene.setdefault(Gene1,0)
                        ScoreGene[Gene1]+=Score[Gene1][Gene2]
                        ScoreGene.setdefault(Gene2,0)
                        ScoreGene[Gene2]+=Score[Gene1][Gene2]
        return ScoreGene

def SortScore(Score):

	sorted_x = sorted(Score.iteritems(), key=operator.itemgetter(1))
	ListGene=[]
	for i in range(0,len(sorted_x)):
		ListGene.append(sorted_x[i][0])
	return ListGene

def NormVect(Score):
	ScoreNew=dict()
	ListScore=Score.values()
	minScore=min(ListScore)
	varScore=max(ListScore)-min(ListScore)
	for Gene in Score.iterkeys():
		ScoreNew[Gene]=(Score[Gene]-minScore)/varScore
	return ScoreNew

def Match(ScoreGene,NbGene,SizeGene,ListGene):


        MatchGene={}
	
	# normalizatopm two score between zero and one
        SizeGeneNorm=NormVect(SizeGene)
	ScoreGeneNorm=NormVect(ScoreGene)
	
	
	for Gene1 in ScoreGene.iterkeys():
                        if not Gene1 in ListGene: continue
			if not SizeGene.has_key(Gene1): continue

                        MatchGene.setdefault(Gene1,[])

                        # Create a dict with as attributs different of Size,Score,...
                        ListAttribut=[]
                        for Gene2 in ScoreGene.iterkeys():
                                        if Gene1 == Gene2: continue
					if not SizeGene.has_key(Gene1) or not SizeGene.has_key(Gene2): continue
					SizeNorm=abs(SizeGeneNorm[Gene2]-SizeGeneNorm[Gene1])
					ScoreNorm=abs(ScoreGeneNorm[Gene1]-ScoreGeneNorm[Gene2])
					Score_Final=SizeNorm+ScoreNorm
                                        ListAttribut.append({'Gene':Gene2,'Score_Final':Score_Final})
                        # Sort dict
                        SortedListAttribut = sorted(ListAttribut , key=lambda elem:     elem['Score_Final'])

                        if NbGene  > len(SortedListAttribut):
                                NbGeneTemp=len(SortedListAttribut)
                        else:
                                NbGeneTemp=NbGene
                        for i in range(0,NbGeneTemp):
                                        Gene=SortedListAttribut[i]['Gene']
                                        MatchGene[Gene1].append(Gene)

        return MatchGene


def Filter(ListGene,Match):
	ListGeneNew={}
	for Gene in ListGene.iterkeys():
		if Match.has_key(Gene):
			ListGeneNew[Gene]=1
	return ListGeneNew



def Compute_SumLinks(ListGene,ScorePair):
	Sum=0
	for Gene1 in ListGene.iterkeys():
		for Gene2 in ListGene.iterkeys():
			if ScorePair.has_key(Gene1) and ScorePair[Gene1].has_key(Gene2):
				Sum+=ScorePair[Gene1][Gene2]
	return Sum



def RandomGen(Match):
	ListGene=Match
	ListGeneNew={}
	for Gene in ListGene.iterkeys():
		GeneRandom=SelectGene(ListGeneNew,Match[Gene])
		
		ListGeneNew[GeneRandom]=1
	return ListGeneNew

def SelectGene(ListGene,Match):
	GeneRandom=random.choice(Match)
	if ListGene.has_key(GeneRandom):
		GeneRandom=SelectGene(ListGene,Match)

	return GeneRandom





