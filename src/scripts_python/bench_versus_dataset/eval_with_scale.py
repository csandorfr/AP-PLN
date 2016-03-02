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
score_pair=data.read_score(f_dataset,gene_convert,sem_sim)
print "Number of gene pairs",len(score_pair.keys())

# sort pair according to score
print "4) Sort pair according Score..."
list_pair=functions.sort_by_val(score_pair)
print "Number of Pair",len(list_pair)

# Report dataset by bin versus semantic similarity
print "5) read and look at distribution mgi/hpo..."
data.report_data_ben_bin(f_out,score_pair,list_pair,sem_sim,bin_size,median_y_n)

