def get_redundant_term(file):
	convert=dict()
	f=open(file,'r')
	for line in f:
		line=line.rstrip().split("\t")
		term=line[0]
		for i in range(1,len(line)):
			alt_term=line[i]
			convert[alt_term]=term
	f.close()
	return convert

def get_list_term(file,convert):
	f=open(file,'r')
	list_term=dict()
	for line in f:
		line=line.rstrip()
		try:
			list_term[convert[line]]=1
		except:
			list_term[line]=1
	f.close()
	return list_term

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

def take_subset_annot_gene(file1,file2,child):
	f1=open(file1,'r')
	f2=open(file2,'w')
	for line in f1:
		line=line.rstrip().split("\t")
		gene=line[0]
		list_annot=[]
		for i in range(1,len(line)):
			annot=line[i]
			if child.has_key(annot):
				list_annot.append(annot)
		if len(list_annot) > 0:
			f2.write('%s\t%s\n' % (gene,"\t".join(list_annot)))
	f1.close()
	f2.close()
