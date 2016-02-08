import sys,os
import data

# Parameters
f_annot_phen=sys.argv[1]
dir_data=sys.argv[2]
dir_work=sys.argv[3]
exclude=sys.argv[4]
out_suffixe=sys.argv[5]

#
# Step1: Determine data file used to compute similarity score 
#
print "1) File used to compute phenotypic semantic similarity score between genes pairs"
f_dcas,f_term,f_redund,f_annot=data.get_list_file(dir_data)
print "disjonct common ancestor file",f_dcas
print "phenotype information (relation with others terms) file",f_term
print "phenotype redundant file",f_redund
print "phenotype annotations of genes file",f_annot

#
# Step2: Keep only relevant annotation"
# 
f_annot_subset=dir_work+'/'+"genes_ens_to_phenotype_no_red_"+out_suffixe+".txt"
print "2) Keep only relevant annotation..."
if exclude=='0' or exclude=='1':
	os.system("python ../scripts_python/reannotation_with_subset/reannotation_with_subset.py %s %s %s %s %s %s" % (f_annot_phen,dir_data+"/"+f_term,dir_data+"/"+f_redund,dir_data+"/"+f_annot,f_annot_subset,exclude))
else:
	print "error in parameter exclude",exclude
	exit()
#
# Step3: Compute information content for each term
#
print "3) Compute Information Content of each term..."
f_ic=dir_work+'/'+"ic_"+out_suffixe+".txt"
os.system("python ../scripts_python/ic/compute_ic.py %s %s %s" % (dir_data+"/"+f_term,f_annot_subset,f_ic))

#
# Step4: Compute similarity between terms
# 
print "4) Compute Similarity between each term pairs by using disjunctive common ancestors (see GRASM paper)"
f_sem_term=dir_work+'/'+"semantic_sim_term_"+out_suffixe+".txt"
os.system("python ../scripts_python/compute_sim_term/compute_sim_term.py %s %s %s" % (dir_data+"/"+f_dcas,f_ic,f_sem_term))

#
# Step5: Compute similarity score between gene pairs
#
print "5) Compute semantic similarity score between each gene Pairs"
f_sem_sim=dir_work+'/'+"semantic_sim_gene_"+out_suffixe+".txt"
os.system("python ../scripts_python/compute_sim_score/compute_sim_score.py %s %s %s" % (f_sem_term,f_annot_subset,f_sem_sim))

#
# Step6: Scale semamtic similarity score
#
print "6) Scale semantic similarity score"
f_sem_sim_scale=dir_work+'/'+"semantic_sim_gene_"+out_suffixe+".scale"
os.system("python ../scripts_python/scale_dataset/scale_dataset.py %s %s" % (f_sem_sim,f_sem_sim_scale))
