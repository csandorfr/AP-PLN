import sys,operator

def read_data(file):
	score_pair=dict()
	f=open(file,'r')
	for line in f:
		line=line.rstrip().split('\t')
		gene1=line[0]
		gene2=line[1]
		score=float(line[2])
		pair=gene1+":"+gene2
		score_pair[pair]=score
	f.close()
	return score_pair

def sort_report(file,score_pair):

	sorted_score = sorted(score_pair.iteritems(), key=operator.itemgetter(1))
	list_pair=[]
	for i in range(0,len(sorted_score)):
		list_pair.append(sorted_score[i][0])

	list_pair.reverse()

	f=open(file,'w')
	for pair in list_pair:
		gene=pair.split(":")
		f.write("%s\t%s\t%s\n" % (gene[0],gene[1],score_pair[pair]))
	f.close()

f_in=sys.argv[1]
f_out=sys.argv[2]

score_pair=read_data(f_in)
print "Number of pair",len(score_pair.keys())

sort_report(f_out,score_pair)
