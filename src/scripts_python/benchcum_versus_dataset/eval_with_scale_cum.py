import sys
import  data,functions


# parameters
f_ens_rd=sys.argv[1]
f_sem_sim=sys.argv[2]
f_dataset=sys.argv[3] 
f_out=sys.argv[4] 
bin_size=sys.argv[5]
bin_size=int(bin_size)
median_y_n=sys.argv[6]


# Redundant ens annotation
print "1) Read ens redundant annotations"
gene_convert=data.read_ens_rd(f_ens_rd)
print "Number of gene",len(gene_convert.keys())

# Read semantic similarity score (benchmark, y)
print "2) Read MGI similarity..."
sem_sim=data.read_sem_sim(f_sem_sim)

# Read genomic dataset (x) with gene pair benchmark value (y)
print "3) Read Score for pair with MGI Score..."
score_pair,list_pair=data.read_score(f_dataset,gene_convert)
print "Number of gene pairs",len(score_pair.keys())


# Report dataset by bin versus semantic similarity
print "4) read and look at distribution mgi/hpo..."
data.report_data_ben_bin(f_out,score_pair,list_pair,sem_sim,bin_size,median_y_n)



