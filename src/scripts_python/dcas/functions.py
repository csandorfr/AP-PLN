def identify_ancestor(term,info_term,list_term_ancestor):

	if len(info_term[term]['ancestor']) ==0:
		list_term_ancestor.append('')
	else:
		for ancestor in info_term[term]['ancestor']:
			list_term_ancestor.append(ancestor)
			identify_ancestor(ancestor,info_term,list_term_ancestor)

def list_ancestor(info_term):

	for term in info_term.iterkeys():

		list_term_ancestor=[]

		identify_ancestor(term,info_term,list_term_ancestor)
		info_term[term].setdefault('list_ancestor',[])
		info_term[term]['list_ancestor'].extend(list_term_ancestor)

		list_way(info_term,term)

def list_way(info_term,term):
	info_term[term].setdefault('way',[])
	listA=[]
	listA.append(term)
	for A in info_term[term]['list_ancestor']:
		if A=='':
			info_term[term]['way'].append(listA)
			listA=[]
			listA.append(term)
			continue
		listA.append(A)

def dcas_list(list1,list2):
	for a1 in list1:
		for a2 in list2:
			if a1==a2: 
				return a2