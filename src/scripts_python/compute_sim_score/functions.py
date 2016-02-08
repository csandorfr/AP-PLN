import numpy as np

def comparing_gene_product(annot_gene,sim_term):
	scor_pair=dict()
	list_gene=annot_gene.keys()
	for i in range(0,len(list_gene)-1):
		for j in range(i+1,len(list_gene)):
			gene1=list_gene[i]
			gene2=list_gene[j]
			pair=gene1+':'+gene2
			c1=compute_sim_gene(annot_gene[gene1],annot_gene[gene2],sim_term)
			c2=compute_sim_gene(annot_gene[gene2],annot_gene[gene1],sim_term)
			score=(c1+c2)/2
			if score==0: continue
			scor_pair[pair]=score
	return scor_pair

def compute_sim_gene(list_term1,list_term2,sim_term):
	list_score_sim=[]
	for term1 in list_term1:
		list_sim=[]
		for term2 in list_term2:
			pair=term1+","+term2
			try:
				list_sim.append(sim_term[pair])
			except:
				continue
		if len(list_sim) > 0:
			list_score_sim.append(max(list_sim))
	if len(list_score_sim) > 0:
		C=np.mean(list_score_sim)
	else:
		C=0
	return C
