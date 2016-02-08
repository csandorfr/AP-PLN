import os,sys
import shutil
import data
import numpy as np


# parameters
f_bench=sys.argv[1]
f_listfile=sys.argv[2]
dir_data=sys.argv[3]
dir_work=sys.argv[4]
bin_size=sys.argv[5]
bin_size=int(bin_size)
median_y_n=sys.argv[6]
out=sys.argv[7]


# fixed parameters
f_ens_red="../../data/others/ensg_63symb_redundancy"

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
# Step2: get the list of file to integrate
#
print "Get the list of file to integrate..."
list_file=data.get_list_file(f_listfile)
print "Number of file",len(list_file)
nb_dataset=len(list_file)

#
# Step3: for each re-scored dataset: compute for bin of gene pairs sorted in ascending order the cumulative semantic similarity
#
f_list_cum=dir_work+"/list_cum_"+out
if nb_dataset >1:
	f=open(f_list_cum,'w')	
	for i in range(0,nb_dataset):
		# gene pair value vs benchmark
		f_in=dir_data+"/"+list_file[i]
		f_out=dir_work+"/"+list_file[i]+".benchcum"
		#os.system("python ../scripts_python/benchcum_versus_dataset/eval_with_scale_cum.py %s %s %s %s %s %s" % (f_ens_red,f_bench,f_in,f_out,bin_size,median_y_n))
		f.write("%s\n" % list_file[i]+".benchcum")
	f.close()
else:
	print "There is not dataset"
	exit()

#
# Step4: make graphe
#
f_graph=dir_work+"/comparison_"+out+".png" 
os.system("Rscript ../scripts_R/comparison_dataset.R %s %s  %s %s" % (dir_work,f_list_cum,str(random_value),f_graph))


