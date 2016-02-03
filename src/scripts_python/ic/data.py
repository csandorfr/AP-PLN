
def report_ic(file,info_term,list_term):
	f=open(file,'w')
	for term in list_term:
		f.write("%s\t%s\t%s\n" % (term,info_term[term]['nb_gene'],info_term[term]['ic']))
	f.close()

def get_gene_phen_annot(file):
	f=open(file,'r')
	annot=dict()
	for line in f:
		line=line.rstrip().split("\t")
		gene=line[0]
		
		for i in range(1,len(line)):
			annot.setdefault(line[i],{})
			annot[line[i]][gene]=1
	f.close()
	return annot

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