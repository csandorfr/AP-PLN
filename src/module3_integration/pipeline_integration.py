import os,sys
import shutil
import data,functions


# parameters
f_bench=sys.argv[1]
f_listfile=sys.argv[2]
dir_data=sys.argv[3]
dir_work=sys.argv[4]
bin_size=sys.argv[5]
bin_size=int(bin_size)
median_y_n=sys.argv[6]
suff_out=sys.argv[7]

# fixed parameters
f_ens_red="../../data/others/ensg_63symb_redundancy"


#
# Step1: get the list of file to integrate
#
print "Get the list of file to integrate..."
list_file=data.get_list_file(f_listfile)
print "Number of file",len(list_file)
nb_dataset=len(list_file)
nb_m=nb_dataset+10

#
# Step2: integration by down-weighting less reliable data by using parameter d representing the degree of dependance between dataset according method devoloped by Marcott et al.

if nb_dataset ==1:
	print "There is just one dataset: no need of integration"
	f_in=dir_data+"/"+list_file[0]
	f_out=dir_work+"/integration_"+suff_out
	shutil.copyfile("%s,%s" % (f_in,f_out))

elif nb_dataset > 1:

	# integration with different free parameters	
	print "integration with different free parameter d used to dow-weighted the less reliable data"
	f_integrated=dir_work+'/wl_'+suff_out
	os.system("python ../scripts_python/sum_weighted_links/sum_weighted_links.py %s %s %s %s" % (f_listfile,dir_data,f_integrated,nb_m))
	
	# create bin integrated dataset for a given free parameter vs phenotypic benchmark" 
	print "Create bin integrated dataset for a given free parameter vs phenotypic benchmark"
	functions.evaluate_free_param(f_integrated,f_bench,bin_size,median_y_n,f_ens_red)
	
	# optimisation of free parameter by usion a linear regression
	f_best_d=dir_work+"/best_parameters_d"
	f_graphe_d=dir_work+"/best_parameters_d.png"
	os.system("Rscript ../scripts_R/optimization_best_d_parameter.R %s %s %s %s %s" % (dir_work,nb_m,f_graphe_d,f_best_d,suff_out))
	best_d=data.get_best_parameter_d(f_best_d)
	print "best parameters d",best_d
	
	# rewrite a clean file with best parameters
	functions.get_integration(f_integrated,best_d)

	# remove non usuful file 
	data.remove_non_usuful_file(dir_data,f_integrated,nb_m)
else:
	print "There is not dataset"
	

