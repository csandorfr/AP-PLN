import sys,os
import data
import logging
import subprocess

# Parameters
f_annot_phen=sys.argv[1]
dir_data=sys.argv[2]
dir_work=sys.argv[3]
exclude=sys.argv[4]
out_suffixe=sys.argv[5]


# define log
logger = logging.getLogger('module1-build phenotypic benchmark')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
#
# Step1: Determine data file used to compute similarity score 
#
logger.info("1) File used to compute phenotypic semantic similarity score between genes pairs")
f_dcas,f_term,f_redund,f_annot=data.get_list_file(dir_data)
logger.debug("disjonct common ancestor file: %s" % f_dcas)
logger.debug("phenotype information (relation with others terms) file: %s " % f_term)
logger.debug("phenotype redundant file: %s" % f_redund)
logger.debug("phenotype annotations of genes file: %s" % f_annot)

#
# Step2: Keep only relevant annotation"
# 
f_annot_subset=dir_work+'/'+"genes_ens_to_phenotype_no_red_"+out_suffixe+".txt"
logger.info("2) Keep only relevant annotation...")
if exclude=='0' or exclude=='1':
	list_arg="python $AP_PLN_HOME/src/scripts_python/reannotation_with_subset/reannotation_with_subset.py %s %s/%s %s/%s %s/%s %s %s" % (f_annot_phen,dir_data,f_term,dir_data,f_redund,dir_data,f_annot,f_annot_subset,exclude)
	proc = subprocess.Popen(list_arg, stdout=subprocess.PIPE, shell=True) 
	(out, err) = proc.communicate()
	[logger.debug(val) for val in out.split("\n")]
	if err is not None: logger.error(err)
else:
	logger.error("error in parameter exclude %s" % exclude)
	exit()
#
# Step3: Compute information content for each term
#
logger.info("3) Compute Information Content of each term...")
f_ic=dir_work+'/'+"ic_"+out_suffixe+".txt"
list_arg="python $AP_PLN_HOME/src/scripts_python/ic/compute_ic.py %s/%s %s %s" % (dir_data,f_term,f_annot_subset,f_ic)
proc = subprocess.Popen(list_arg, stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
[logger.debug(val) for val in out.split("\n")]
if err is not None: logger.error(err)

#
# Step4: Compute similarity between terms
# 
logger.info("4) Compute Similarity between each term pairs by using disjunctive common ancestors (see GRASM paper)")
f_sem_term=dir_work+'/'+"semantic_sim_term_"+out_suffixe+".txt"
list_arg="python $AP_PLN_HOME/src/scripts_python/compute_sim_term/compute_sim_term.py %s/%s %s %s" % (dir_data,f_dcas,f_ic,f_sem_term)
proc = subprocess.Popen(list_arg, stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
[logger.debug(val) for val in out.split("\n")]
if err is not None: logger.error(err)

#
# Step5: Compute similarity score between gene pairs
#
logger.info("5) Compute semantic similarity score between each gene Pairs")
f_sem_sim=dir_work+'/'+"semantic_sim_gene_"+out_suffixe+".txt"
list_arg="python $AP_PLN_HOME/src/scripts_python/compute_sim_score/compute_sim_score.py %s %s %s" % (f_sem_term,f_annot_subset,f_sem_sim)
proc = subprocess.Popen(list_arg, stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
[logger.debug(val) for val in out.split("\n")]
if err is not None: logger.error(err)

#
# Step6: Scale semamtic similarity score
#
logger.info("6) Scale semantic similarity score")
f_sem_sim_scale=dir_work+'/'+"semantic_sim_gene_"+out_suffixe+".scale"
list_arg="python $AP_PLN_HOME/src/scripts_python/scale_dataset/scale_dataset.py %s %s" % (f_sem_sim,f_sem_sim_scale)
proc = subprocess.Popen(list_arg, stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
[logger.debug(val) for val in out.split("\n")]
if err is not None: logger.error(err)


#
# Step7: Remove intermediate file
#
logger.info("7) Remove useless file")
list_arg="rm %s %s %s %s" % (f_annot_subset,f_sem_term,f_ic,f_sem_sim)
proc = subprocess.Popen(list_arg, stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
[logger.debug(val) for val in out.split("\n")]
if err is not None: logger.error(err)
