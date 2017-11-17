import os,sys
import logging

#
# Parameters
#
f_sem_sim=sys.argv[1]
f_list_data=sys.argv[2]
dir_data=sys.argv[3]
dir_work=sys.argv[4]
out=sys.argv[5]

#
# Define log
#
logger = logging.getLogger('quick start')
logger.setLevel(logging.DEBUG)
ch = logging.FileHandler('%s/qstart_%s.log' % (dir_work,out))
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

logger.info("Parameters:%s" % sys.argv )

#
# Step1: Evaluation of two individual functional dataset
#
logger.info("1) Evalution and of two individual functional dataset")
os.system("python $AP_PLN_HOME/src/module2_evaluation_rescore/pipeline_evaluation_rescore.py %s %s %s %s 500 0 %s" % (f_sem_sim,f_list_data,dir_data,dir_work,out))

#
# Step2: Integration to build PLN
#
logger.info("2) Integration to build PLN")
list_file_rescore=dir_work+"/list_file_rescore."+out
os.system("python $AP_PLN_HOME/src/module3_integration/pipeline_integration.py %s %s %s %s 500 0 %s" % (f_sem_sim,list_file_rescore,dir_work,dir_work,out))
#
# Step3: Comparison of accuracy and gene pairs coverage for different individual dataset and for PLN
#
logger.info("3) Comparison of two functional dataset interm of gene pairs coverage and accuracy")
list_file_rescore_final=dir_work+"/list_file_rescore_wl."+out
os.system("python $AP_PLN_HOME/src/additional_tools/comparison_dataset/pipeline_evaluation.py %s %s %s %s 2000 0 %s" % (f_sem_sim,list_file_rescore_final,dir_work,dir_work,out))
