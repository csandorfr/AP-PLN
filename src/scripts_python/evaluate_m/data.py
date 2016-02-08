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



