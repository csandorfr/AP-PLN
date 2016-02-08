import functions

def get_info_term(file):
	info_term,list_term={},[]
	f=open(file,'r')
	for line in f:
		line=line.rstrip().split('\t')
		generation=int(line[0])
		term=line[1]
		name=line[2]
		ancestor=[]
		for i in range(3,len(line)):
			parent=line[i]
			ancestor.append(parent)
		info_term.setdefault(term,dict())
		info_term[term].setdefault('ancestor',[])
		info_term[term]['ancestor'].extend(ancestor)
		info_term[term]['name']=name
		info_term[term]['generation']=generation
		list_term.append(term)

	return info_term,list_term

def report_dcas_pairs(file,list_term,info_term):

	f=open(file,'w')
	for i in range(0,len(list_term)-1):
		if not i % 100:
			print "\t%s" % i
		for j in range(i+1,len(list_term)):
			term1=list_term[i]
			term2=list_term[j]
			dcas=dict()
			for list1 in info_term[term1]['way']:
				for list2 in info_term[term2]['way']:
					A=functions.dcas_list(list1,list2)
					dcas[A]=1


			f.write("%s\t%s" % (term1,term2))
			for ancestor in dcas.iterkeys():
				f.write("\t%s" % (ancestor))
			f.write("\n")

	f.close()
