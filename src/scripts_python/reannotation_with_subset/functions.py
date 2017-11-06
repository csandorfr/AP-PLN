def identify_child(term,info_term,child):
	for term_child in info_term[term]['child']:
		child[term_child]=1
		identify_child(term_child,info_term,child)

def list_child(info_term):
	for term in info_term.iterkeys():
		child=[]
		for term_child in info_term.iterkeys():
			if term in info_term[term_child]['ancestor']: child.append(term_child)
		info_term[term].setdefault('child',[])
		info_term[term]['child'].extend(child)
