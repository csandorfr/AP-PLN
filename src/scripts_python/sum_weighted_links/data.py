import functions

def get_list_file(file):
	f=open(file,'r')
	list_file=[]
	for line in f:
		list_file.append(line.rstrip())
	f.close()
	return list_file

def read_pair_score(file,nb_dataset,id_data,score_pair):
	f=open(file,'r')
	for line in f:
		line=line.rstrip().split('\t')
		gene1=line[0]
		gene2=line[1]
		score=float(line[2])
		pair1=gene1+':'+gene2
		pair2=gene2+':'+gene1
		if score_pair.has_key(pair1):
			pair=pair1
		elif score_pair.has_key(pair2):
			pair=pair2
		else:
			pair=pair1
		score_pair.setdefault(pair,['NaN']*nb_dataset)
		score_pair[pair][id_data]=score
	f.close()

def report_integration(file,score_pair,list_d):
	f=open(file,'w')
	for pair in score_pair.iterkeys():
		gene=pair.split(':')
		list_score=[]
		for score in score_pair[pair]:
			if score=='NaN': continue
			list_score.append(score)
		list_score=sorted(list_score)
		list_score.reverse()
		f.write("%s\t%s" % (gene[0],gene[1]))
		for d in list_d:
                        score_final=functions.weighted_sum_marcott(list_score,d)
			f.write("\t%s" % (score_final))
		f.write('\n')
	f.close()
