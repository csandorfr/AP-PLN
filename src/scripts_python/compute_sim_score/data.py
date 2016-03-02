import operator

def get_sim_term(file):
	sim_term=dict()
	f=open(file,'r')
	for line in f:
		line=line.rstrip().split('\t')
		term1=line[0]
		term2=line[1]
		pair1=term1+","+term2
		pair2=term2+","+term1
		score=float(line[2])
		sim_term[pair1]=score
		sim_term[pair2]=score
	f.close()
	return sim_term

def get_gene_annotation(file):
	f=open(file,'r')
	annot_gene=dict()
	for line in f:
		line=line.rstrip().split("\t")
		gene=line[0]
		for i in range(1,len(line)):
			annot_gene.setdefault(gene,{})
			annot_gene[gene][line[i]]=1
	f.close()
	return annot_gene

def report_semantic_sim(file,score_pair):
	list_pair=sort_by_val(score_pair)
	f=open(file,'w')
	for pair in list_pair:
		gene = pair.split(":")
		f.write("%s\t%s\t%s\n" % (gene[0],gene[1],score_pair[pair]))
	f.close()

def sort_by_val(score_pair):
	list_pair=[]
	sort_gene = sorted(score_pair.iteritems(), key=operator.itemgetter(1))
	for i in range(0,len(sort_gene)):
		list_pair.append(sort_gene[i][0])
	list_pair.reverse()
	return list_pair
