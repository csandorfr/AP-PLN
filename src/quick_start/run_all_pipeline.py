import os,sys

# parameters
f_sem_sim=sys.argv[1]
f_list_data=sys.argv[2]
dir_data=sys.argv[3]
dir_work=sys.argv[4]
out=sys.argv[5]

#
# Step1: Evaluation of two individual functional dataset
#
os.system("$AP_PLN_HOME")
#os.system("python $AP_PLN_HOME/src/module2_evaluation_rescore/pipeline_evaluation_rescore.py %s %s %s %s 500 0 %s" % (f_sem_sim,f_list_data,dir_data,dir_work,out))
#
# Step2: Integration to build PLN
#
list_file_rescore=dir_work+"/list_file_rescore."+out
os.system("python $AP_PLN_HOME/src/module3_integration/pipeline_integration.py %s %s %s %s 500 0 %s" % (f_sem_sim,list_file_rescore,dir_work,dir_work,out))
#
# Step3: Comparison of accuracy and gene pairs coverage for different individual dataset and for PLN
#
list_file_rescore_final=dir_work+"/list_file_rescore_wl."+out
print list_file_rescore_final
os.system("python $AP_PLN_HOME/src/module4_comparison_dataset/pipeline_evaluation.py %s %s %s %s 2000 0 %s" % (f_sem_sim,list_file_rescore_final,dir_work,dir_work,out))
