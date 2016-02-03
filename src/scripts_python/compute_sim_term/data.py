import functions

def get_ic(file):
	ic=dict()
	f=open(file,'r')
	for line in f:
		line = line.rstrip().split('\t')
		if line[2]=='NaN': continue
		term = line[0]
		val= float(line[2])
		ic[term]=val
	f.close()
	return ic

def compute_score_sem_sim(file1,file2,ic):	
	f1=open(file1,'r')
	f2=open(file2,'w')
	# between each different ter,
	for line in f1:
		line=line.rstrip().split('\t')
		term1=line[0]
		term2=line[1]
		score=functions.comparison_term(line[2:len(line)],ic)
		if score=='NaN': continue
		f2.write("%s\t%s\t%s\n" % (term1,term2,score))
	# between each term
	for term in ic.iterkeys():
		f2.write("%s\t%s\t%s\n" % (term,term,ic[term]))
	f1.close()
