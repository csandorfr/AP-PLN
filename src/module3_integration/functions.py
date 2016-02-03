import data,os

def evaluate_free_param(f_integration,f_bench,bin_size,median_y_n,f_ens_red):

	# determine the number of free parameter to evaluate
	f=open(f_integration,'r')
	head=f.readline()
	nb_d=len(head.rstrip().split('\t'))-2
	print "number of free parameter",nb_d

	# gene pair in bench
	sem_sim=data.read_sem_sim(f_bench)

	# comparison phenotypic bench vs integrated datase
	for d in range(1,nb_d+1):

		# keep only gene pairs with phenotypic semantic similarity score
		f_out1=f_integration+"_d"+str(d)
		data.report_pair_with_sem_sim(f_integration,f_out1,sem_sim,d)

		# sort gene pair by value
		f_out2=f_integration+"_d"+str(d)+".ord"
		os.system("python ../scripts_python/sort_gene_pairs_by_value/sort_pair_value.py %s %s" % (f_out1,f_out2))
		os.system("rm %s" % f_out1)

		# scale dataset
		f_out3=f_integration+"_d"+str(d)+".ord.scale"
		os.system("python ../scripts_python/scale_dataset/scale_dataset.py %s %s" % (f_out2,f_out3))
		os.system("rm %s" % f_out2)
		
		# gene pair value vs benchmark
		f_out4=f_integration+"_d"+str(d)+"_bench"
		print(os.system("python ../scripts_python/bench_versus_dataset/eval_with_scale.py %s %s %s %s %s %s" % (f_ens_red,f_bench,f_out3,f_out4,bin_size,median_y_n)))
		os.system("python ../scripts_python/bench_versus_dataset/eval_with_scale.py %s %s %s %s %s %s" % (f_ens_red,f_bench,f_out3,f_out4,bin_size,median_y_n))

def get_integration(f_integration,best_d):
	
		# select correct dataset		
		f_out1=f_integration+"_final"
		data.report_pair(f_integration,f_out1,best_d)

		# scale dataset
		f_out2=f_integration+"final.scale"
		os.system("python ../scripts_python/scale_dataset/scale_dataset.py %s %s" % (f_out1,f_out2))
		os.system("rm %s" % f_out1)

		# sort the pairs by value
		f_out3=f_integration+"final.scale.ord"
		os.system("python ../scripts_python/sort_gene_pairs_by_value/sort_pair_value.py %s %s" % (f_out2,f_out3))
		os.system("rm %s" % f_out2)
		os.system("rm %s" % f_integration)
		

	
