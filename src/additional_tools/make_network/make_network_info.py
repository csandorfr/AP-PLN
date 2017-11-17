import os,sys
import data          
import shutil
import numpy as np
import logging

# parameters
f_gene=sys.argv[1]
f_net=sys.argv[2]
f_list=sys.argv[3]
f_dir=sys.argv[4]
dir_work=sys.argv[5]
out_suffixe=sys.argv[6]

#
# Define log
#
logger = logging.getLogger('make network info')
logger.setLevel(logging.DEBUG)
ch = logging.FileHandler('%s/network_%s.log' % (dir_work,out_suffixe))
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

logger.info("Parameters:%s" % sys.argv )

# Get a subnetwork from input gene list and network
logger.info("1) Get a subnetwork from input gene list and network")
f_out_subnet=dir_work+"/"+out_suffixe+"_subnetwork"
os.system("Rscript $AP_PLN_HOME/src/scripts_R/get_subnetwork.R %s %s %s > /dev/null" % (f_gene,f_net,f_out_subnet))
f_out_infoLinks=dir_work+"/"+out_suffixe+"_infoLinks"

# Extract information for each link in the subnetwork
logger.info("2) Extract information for each link in the subnetwork")
os.system("python $AP_PLN_HOME/src/additional_tools/extract_link_resource/get_info_network.py %s %s %s %s > /dev/null" % (f_out_subnet,f_list,f_dir,f_out_infoLinks))

# Plot the subnetwork 
logger.info("3) Plot the subnetwork")
os.system("Rscript $AP_PLN_HOME/src/scripts_R/make_network.R %s %s > /dev/null" % (f_out_infoLinks,dir_work))
