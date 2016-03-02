import sys,os
import numpy as np
import logging
import subprocess

# parameters
f_bench=sys.argv[1]
f_list_file_eval=sys.argv[2]
dir_data=sys.argv[3]
dir_work=sys.argv[4]
bin_size=sys.argv[5]
bin_size=int(bin_size)
median_y_n=sys.argv[6]
suff_out=sys.argv[7]


# fixed parameters
f_ens_red="$AP_PLN_HOME/data/others/ensg_63symb_redundancy"

# define log
logger = logging.getLogger('module2-evaluation_rescore')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

#
# Step1: Compute the phenotypic value associated with random genes
# 
logger.info("1) Compute the phenotypic semantic similarity associated with random genes")
semantic_score=np.loadtxt('%s' % f_bench, usecols=[2])
if median_y_n=='1':
	random_value=np.median(semantic_score)
elif median_y_n=='0':
	random_value=np.mean(semantic_score)
else:	
	logger.error("error: median must be 0 or 1")
	exit()
logger.debug("%s" % random_value)

#
# Step2: Get the list of file to evaluate
#
logger.info("2) Get the list of functional dataset to evaluate")
list_file = [line.strip() for line in open(f_list_file_eval, 'r')]
logger.debug("There are %s to evaluate" % len(list_file))
logger.debug("\n".join(list_file))


#
# Step3: Create Bin Genomic Measure Versus Phenotypic Benchmark
#

logger.info("3) Create bin genomic measure vs phenotypic benchmark for:")
for file_ref in list_file:
	f_eval=dir_work+"/"+file_ref+"."+suff_out+".eval"
	list_arg='''python $AP_PLN_HOME/src/scripts_python/bench_versus_dataset/eval_with_scale.py %s %s %s/%s %s %s %s\n''' % (f_ens_red,f_bench,dir_data,file_ref,f_eval,bin_size,median_y_n)
	proc = subprocess.Popen(list_arg, stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	[logger.debug(val) for val in out.split("\n")]
	if err is not None: logger.error(err)
#
# Step4: Evaluation of dataset and re-score
#
logger.info("4) Evaluation and rescore of dataset...")
for file_ref in list_file:
	f_eval=dir_work+"/"+file_ref+"."+suff_out+".eval"
	f_rescore=dir_work+"/"+file_ref+"."+suff_out+".rescore"
	f_graph=dir_work+"/"+file_ref+"."+suff_out+".eval.png"
	list_arg="Rscript $AP_PLN_HOME/src/scripts_R/evaluation_rescale.R %s %s %s %s %s" % (f_eval,random_value,dir_data+"/"+file_ref,f_rescore,f_graph)
	proc = subprocess.Popen(list_arg, stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	[logger.debug(val) for val in out.split("\n")]
	os.system("rm %s" % (f_eval))

#
# Step5: Report the list of re-scaled file
#
logger.info("5) Report the list of re-scaled file")
list_file_rescore=dir_work+"/list_file_rescore."+suff_out
f=open(list_file_rescore,'w')
list_file_new=[file_ref+"."+suff_out+".rescore" for file_ref in list_file]
f.write("%s" % "\n".join(list_file_new))
