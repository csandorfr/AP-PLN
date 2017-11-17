import os,sys
import shutil
import data
import numpy as np
import logging

#
# Parameters
#
f_bench=sys.argv[1]
f_listfile=sys.argv[2]
dir_data=sys.argv[3]
dir_work=sys.argv[4]
bin_size=sys.argv[5]
bin_size=int(bin_size)
median_y_n=sys.argv[6]
out=sys.argv[7]

#
# Define log
#
logger = logging.getLogger('additional-tools comparison dataset')
logger.setLevel(logging.DEBUG)
ch = logging.FileHandler('%s/add_eval_%s.log' % (dir_work,out))
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.info("Parameters:%s" % sys.argv )

#
# fixed parameters
#
f_ens_red="$AP_PLN_HOME/data/others/ensg_63symb_redundancy"

#
# Step1: Compute the phenotypic value associated with random genes
#
logger.info("1) Compute the phenotypic semantic similarity associated with random genes:") 
semantic_score=np.loadtxt('%s' % f_bench, usecols=[2])
if median_y_n=='1':
        random_value=np.median(semantic_score)
elif median_y_n=='0':
        random_value=np.mean(semantic_score)
else:   
        print "error: median must be 0 or 1"
	logger.error("error: median must be 0 or 1")

#
# Step2: get the list of file to compare
#
logger.info("2) Get the list of functional dataset to compare")
list_file=data.get_list_file(f_listfile)
logger.info("Number of functional dataset %s" % len(list_file.keys()))
nb_dataset=len(list_file.keys())

#
# Step3: for each re-scored dataset: compute for bin of gene pairs sorted in ascending order the cumulative semantic similarity
#
logger.info("3) For each functional dataset compute the cumulative semantic similarity by bin of x gene pairs")
f_list_cum=dir_work+"/list_cum_"+out
if nb_dataset >1:
	f=open(f_list_cum,'w')	
	for name in list_file.iterkeys():
		# gene pair value vs benchmark
		f_in=dir_data+"/"+list_file[name]
		f_out=dir_work+"/"+list_file[name]+".benchcum"
		os.system("python $AP_PLN_HOME/src/scripts_python/benchcum_versus_dataset/eval_with_scale_cum.py %s %s %s %s %s %s" % (f_ens_red,f_bench,f_in,f_out,bin_size,median_y_n))
		f.write("%s.benchcum\t%s\n" % (list_file[name],name))
	f.close()
else:
	logger.error("There is not dataset")
	exit()

#
# Step4: make graphe
#
logger.info("4) Make plot")
f_graph=dir_work+"/comparison_"+out+".pdf"

print("Rscript $AP_PLN_HOME/src/scripts_R/comparison_dataset.R %s %s  %s %s > /dev/null" % (dir_work,f_list_cum,str(random_value),f_graph))


