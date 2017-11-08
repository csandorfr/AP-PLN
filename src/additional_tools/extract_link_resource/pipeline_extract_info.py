import os,sys
import data          
import shutil
import numpy as np

# parameters
f_gene=sys.argv[1]
f_net=sys.argv[2]
f_list=sys.argv[3]
f_dir=sys.argv[4]

f_out_subnet=f_net+"_subnetwork"

#get a subnetwork from input gene list and network
os.system("Rscript $AP_PLN_HOME/src/additional_tools/extract_link_resource/get_subnetwork.R %s %s %s" % (f_gene,f_net,f_out_subnet))

f_out_infoLinks=f_out_subnet+"_infoLinks"

#extract information for each link in the subnetwork
os.system("python $AP_PLN_HOME/src/additional_tools/extract_link_resource/get_info_network.py %s %s %s %s" % (f_out_subnet,f_list,f_dir,f_out_infoLinks))

#plot the subnetwork 
os.system("Rscript $AP_PLN_HOME/src/additional_tools/extract_link_resource/make_network.R %s %s" % (f_out_infoLinks,f_dir))
