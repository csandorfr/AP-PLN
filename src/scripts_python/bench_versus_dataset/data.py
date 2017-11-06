import functions
import numpy as np


def report_data_ben_bin(f_out,score_pair,list_pair,sem_sim,bin_size,median_y_n):

        f=open(f_out,'w')
        pair=dict()
	sim_link=[]
        nb_gene_bin,sim_y,sum_score=0,0,0
        
	for pair_gene in list_pair:
		
		# pairs
                gene=pair_gene.split(":")
                score=float(score_pair[pair_gene])
		gene1=gene[0]
		gene2=gene[1]

		# doublous
                if (pair.has_key(gene1) and pair[gene1].has_key(gene2)):
			continue
		if (pair.has_key(gene2) and pair[gene2].has_key(gene1)):
			continue
		
		pair.setdefault(gene1,dict())
		pair[gene1][gene2]=1
		pair.setdefault(gene2,dict())
		pair[gene2][gene1]=1

                if nb_gene_bin==bin_size:
                        if median_y_n=="y":
                                sim_y=np.median(sim_link)
                        else:
                                sim_y=np.mean(sim_link)
                        sum_score/=len(sim_link)
                        f.write("%s\t%s\n" % (sum_score,sim_y))

                        sim_link=[]
                        sum_score=0

                        nb_gene_bin=0

                sum_score+=score
                nb_gene_bin+=1
		if (sem_sim.has_key(gene1) and sem_sim[gene1].has_key(gene2)):
                        sim_link.append(sem_sim[gene1][gene2])
                if (sem_sim.has_key(gene2) and sem_sim[gene2].has_key(gene1)):
                        sim_link.append(sem_sim[gene2][gene1])

        f.close()


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

def read_ens_rd(file):
        f=open(file,'r')
        gene_convert=dict()
        for line in f:
                line=line.rstrip().split('\t')
                ref_gene=line[0]
                for gene in range(1,len(line)):
                        gene_convert[gene]=ref_gene
        return gene_convert




def read_score(file,gene_convert,sem_sim):
        score_pair=dict()
        f=open(file,'r')
        for line in f:
                line=line.rstrip().split("\t")
                gene1=functions.convert(line[0],gene_convert)
                gene2=functions.convert(line[1],gene_convert)
                pair=gene1+":"+gene2
		
                score=float(line[2])
                if gene1==gene2: continue
                if sem_sim.has_key(gene1) and sem_sim[gene1].has_key(gene2):
                        score_pair[pair]=score
                if sem_sim.has_key(gene2) and sem_sim[gene2].has_key(gene1):
                        score_pair[pair]=score
        f.close()

        return score_pair
