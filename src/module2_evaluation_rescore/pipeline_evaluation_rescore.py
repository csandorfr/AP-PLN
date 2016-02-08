import sys,os
import numpy as np

# parameters
f_bench=sys.argv[1]
f_gene_pair_value=sys.argv[2]
dir_work=sys.argv[3]
bin_size=sys.argv[4]
bin_size=int(bin_size)
median_y_n=sys.argv[5]


# fixed parameters
f_ens_red="../data/others/ensg_63symb_redundancy"

#
# Step1: Compute the phenotypic value associated with random genes
# 
print "The phenotypic semantic similarity associated with random genes:"
semantic_score=np.loadtxt('%s' % f_bench, usecols=[2])
if median_y_n=='1':
	random_value=np.median(semantic_score)
elif median_y_n=='0':
	random_value=np.mean(semantic_score)
else:
	print "error: median must be 0 or 1"
	exit()
print random_value

#
# Step2: Create Bin Genomic Measure Versus Phenotypic Benchmark
#
print "Create bin genomic measure vs phenotypic benchmark..."
file_el=f_gene_pair_value.split('/')
file_ref=file_el[len(file_el)-1]
f_eval=dir_work+"/"+file_ref+".eval"
os.system("python ../scripts_python/bench_versus_dataset/eval_with_scale.py %s %s %s %s %s %s" % (f_ens_red,f_bench,f_gene_pair_value,f_eval,bin_size,median_y_n)) 

#
# Step3: Evaluation of dataset and re-score
#
print "Evaluation and rescore of dataset..."
f_rescore=dir_work+"/"+file_ref+".rescore"
f_graph=dir_work+"/"+file_ref+".eval.png"
os.system("Rscript ../scripts_R/evaluation_rescale.R %s %s %s %s %s" % (f_eval,random_value,f_gene_pair_value,f_rescore,f_graph))
