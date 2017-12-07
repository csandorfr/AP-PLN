import os,sys
import logging
import change_format

#
# Parameters
#
f_sem_sim=sys.argv[1]
f_list_data=sys.argv[2]
dir_data=sys.argv[3]
dir_work=sys.argv[4]
f_list_gene=sys.argv[5]
out=sys.argv[6]

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
print "Step1: Evaluation on a phenotypic benchmark of functional dataset..."
logger.info("1) Evalution  of two individual functional dataset")
os.system("python $AP_PLN_HOME/src/module2_evaluation_rescore/pipeline_evaluation_rescore.py %s %s %s %s 500 0 %s" % (f_sem_sim,f_list_data,dir_data,dir_work,out))

#
# Step2: Integration to build PLN
#
print "Step2: Integration to build PLN..."
logger.info("2) Integration to build PLN")
list_file_rescore=dir_work+"/list_file_rescore."+out
os.system("python $AP_PLN_HOME/src/module3_integration/pipeline_integration.py %s %s %s %s 500 0 %s" % (f_sem_sim,list_file_rescore,dir_work,dir_work,out))

#
# Step3: Change format of rescored functional dataset
#
print "Step3: Change format of listed functional dataset..."
logger.info("3) Change the format of rescored functional dataset")

# with PLN
list_file_rescore_final=dir_work+"/list_file_rescore_wl."+out
list_file_rescore_type_final=dir_work+"/list_file_rescore_type_wl."+out
change_format.change_format_list_file(list_file_rescore_final,list_file_rescore_type_final,1)
# without PLN
list_file_rescore_type_final_wpln=dir_work+"/list_file_rescore_type_wl_without_pln."+out
change_format.change_format_list_file(list_file_rescore_final,list_file_rescore_type_final_wpln,0)


#
# Step4: Comparison of accuracy and gene pairs coverage for different individual dataset and for PLN
#
print "Comparison of accuracy and gene pairs coverage for different individual dataset and for PLN..."
logger.info("4) Comparison of two functional dataset interm of gene pairs coverage and accuracy")
os.system("python $AP_PLN_HOME/src/additional_tools/comparison_dataset/pipeline_evaluation.py %s %s %s %s 2000 0 %s > /dev/null" % (f_sem_sim,list_file_rescore_type_final,dir_work,dir_work,out))

#
# Step5: Network representation of PLN for a set of genes
#
print "Step5: Network representation of PLN for a set of genes"
logger.info("5) Network representation for a set of genes")
f_net_graph="network_%s" % out
f_net=dir_work+"/wl_"+out+".final.scale.ord"
os.system("python $AP_PLN_HOME/src/additional_tools/make_network/make_network_info.py %s %s %s %s %s %s > /dev/null" % (f_list_gene,f_net,list_file_rescore_type_final_wpln,dir_work,dir_work,f_net_graph))

#
# Step6: Network clustering
#
print "Step6: functional clustering evaluation for a set of genes..."
logger.info("6) Functional clustering for a set of genes")
os.system(" python $AP_PLN_HOME/src/additional_tools/clustering_test/clustering_test.py %s %s %s %s 1000 > /dev/null" % (f_list_gene,f_net,dir_work,out))
