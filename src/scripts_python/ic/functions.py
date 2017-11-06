from math import log

def list_child(info_term):
	for term in info_term.iterkeys():
		child=[]
		for term_child in info_term.iterkeys():
			if term in info_term[term_child]['ancestor']: child.append(term_child)
		info_term[term].setdefault('child',[])
		info_term[term]['child'].extend(child)

def number_gene_class(list_term,info_term,annot):

	for term in list_term:
		annot_local=dict()
		identify_gene_subclass(term,annot_local,annot,info_term)
		info_term[term]['nb_gene']=len(annot_local.keys())

def identify_gene_subclass(term,annot_local,annot,info_term):

	if annot.has_key(term):
		for gene in annot[term].iterkeys():
			annot_local[gene]=1

	for child in info_term[term]['child']:
		identify_gene_subclass(child,annot_local,annot,info_term)

def compute_ic(info_term):
	dem=max_gene(info_term)
	for term in info_term.iterkeys():
		num=info_term[term]['nb_gene']
		try:
			ic=-log(float(num)/float(dem),2)
		except:
			ic='NaN'
		info_term[term]['ic']=ic

def max_gene(info_term):
	list_numb=[]
	for term in info_term.iterkeys():
		list_numb.append(info_term[term]['nb_gene'])
	return max(list_numb)