import os,sys
import logging

#
# Parameters
#
fGene=sys.argv[1]
fNet=sys.argv[2]
dir_work=sys.argv[3]
out=sys.argv[4]
NbSim=sys.argv[5]
NbSim=int(NbSim)

#
# Fixed parameters
#
fSize="$AP_PLN_HOME/data/others/hs_68_cds_max_mean_length"
NbGene=100
nbLinks=1000000

#
# Define log
#
logger = logging.getLogger('additional-tools clustering test ')
logger.setLevel(logging.DEBUG)
ch = logging.FileHandler('%s/clustering_%s.log' % (dir_work,out))
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.info("Parameters:%s" % sys.argv)

# convert gene symbol to ensembl id
logger.info("1) convert gene symbol to ensembl id...")
f_gene_ens=dir_work+"/list_gene_ens"+out
os.system("Rscript $AP_PLN_HOME/src/scripts_R/convert_gene_symbol_ens.R %s %s > /dev/null" % (fGene,f_gene_ens))


# match gene
logger.info("2) Generate background...")
fMatch=dir_work+"/mach_"+out
os.system("python $AP_PLN_HOME/src/additional_tools/clustering_test/generate_random_gene.py %s %s %s %s %s %s > /dev/null" % (fNet,nbLinks,f_gene_ens,NbGene,fSize,fMatch))

# clustering test
logger.info("3) Clustering test...")
fOut=dir_work+'/sim_'+out
os.system("python $AP_PLN_HOME/src/additional_tools/clustering_test/compute_clustering.py %s %s %s %s %s > /dev/null" % (fMatch,fNet,nbLinks,NbSim,fOut))

# plot statistic
logger.info("4) Plot clustering statistic...")
f_pval=fOut+"_pval"
f_score=fOut+"_sum"
os.system("Rscript $AP_PLN_HOME/src/scripts_R/plot_clustering_stat.R %s %s %s %s > /dev/null" % (f_score,f_pval,dir_work,out))
