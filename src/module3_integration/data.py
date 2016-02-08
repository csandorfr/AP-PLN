import os

def get_list_file(file):
	f=open(file,'r')
	list_file=[]
	for line in f:
		list_file.append(line.rstrip())
	f.close()
	return list_file

def get_best_parameter_d(file):
	f=open(file,'r')
	head=f.readline()
	head=head.rstrip().split()
	return int(head[1])

def remove_non_usuful_file(dir_data,f_integration,nb_d):
	os.system("rm %s/*_bench" % (dir_data))
	for d in range(1,nb_d+1):
		file=f_integration+"_d"+str(d)+".ord.scale"
		os.system("rm %s" % file)

def read_sem_sim(file):
	sem_sim=dict()
	f=open(file,'r')
	for line in f:
		line=line.rstrip().split('\t')
		gene1=line[0]
		gene2=line[1]
		score=float(line[2])
		if score > 0:
			sem_sim.setdefault(gene1,dict())
			sem_sim[gene1][gene2]=score
	f.close()
	return sem_sim

def report_pair_with_sem_sim(f_in,f_out,sem_sim,id_d):
	f1=open(f_in,'r')
	f2=open(f_out,'w')
	for line in f1:
		line=line.rstrip().split('\t')
		gene1=line[0]
		gene2=line[1]
		score=line[id_d+1]
		if sem_sim.has_key(gene1) and sem_sim[gene1].has_key(gene2):
			f2.write("%s\t%s\t%s\n" % (gene1,gene2,score))
		elif sem_sim.has_key(gene2) and sem_sim[gene2].has_key(gene1):
			f2.write("%s\t%s\t%s\n" % (gene2,gene1,score))
		else:
			continue
	f1.close()
	f2.close()

def report_pair(f_in,f_out,id_d):
	f1=open(f_in,'r')
	f2=open(f_out,'w')
	for line in f1:
		line=line.rstrip().split('\t')
		gene1=line[0]
		gene2=line[1]
		score=line[id_d+1]
		f2.write("%s\t%s\t%s\n" % (gene1,gene2,score))
	f1.close()
	f2.close()


