def get_parameters_scale(file):
	
	list_val=[]
	f=open(file,'r')
	for line in f:
		line=line.rstrip().split('\t')
		list_val.append(float(line[2]))
	return min(list_val),max(list_val)

def rescale(f_in,f_out,min_val,max_val):
	f1=open(f_in,'r')
	f2=open(f_out,'w')
	for line in f1:
		line=line.rstrip().split("\t")
		gene1=line[0]
		gene2=line[1]
		val=float(line[2])
		score=(val-min_val)/(max_val-min_val)
		f2.write("%s\t%s\t%s\n" % (gene1,gene2,score))
	f1.close()
	f2.close()
	
