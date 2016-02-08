import os
import run_bashjob

dir_data='/net/isi-backup/webber/code/cynthias/disease_specific_network_v4/data/frankdatasetnorm'
f_bench='/net/isi-scratch/cynthia/CW007_SANDOR_Pipeline/network/all/semantic_sim_gene_all_hpo_mgi_sort.txt'
random_value=0.11
dir_work='/net/isi-scratch/cynthia/CW007_SANDOR_Pipeline/network/all'
dir_out='/net/isi-scratch/cynthia/CW007_SANDOR_Pipeline/src/run_pipeline_evaluation'

list_sub=os.listdir(dir_data)
list_file=[]
list_dir=[]
for sub_dir in list_sub:
	list_temp_file=os.listdir("%s/%s" % (dir_data,sub_dir))
	for file in list_temp_file:
		list_file.append(file)
		list_dir.append("%s/%s" % (dir_data,sub_dir))
	
for i in range(0,len(list_file)):	
	content=open('config','r')
	script = content.read()
	script+="\n cd /net/isi-scratch/cynthia/CW007_SANDOR_Pipeline/src/module2_evaluation_rescore"
	script+="\npython pipeline_evaluation_rescore.py %s %s %s %s %s" % (f_bench,list_file[i],list_dir[i],dir_work,random_value)
        name="job_eval_"+str(i)
        bash_script="job_eval_"+str(i)+".sh"
        run_bashjob.run_job_grid(script,dir_out,name,bash_script)
