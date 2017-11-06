import sys,os
import data

# Parameters
f_listfile=sys.argv[1]
dir_data=sys.argv[2]
f_out=sys.argv[3]
nb_m=sys.argv[4]
nb_m=int(nb_m)

# Get the list of file to integrate
print "Get the list of file to integrate..."
list_file=data.get_list_file(f_listfile)
print "Number of file",len(list_file)
nb_dataset=len(list_file)

# Read Score for the different dataset
print "Read Score for the different dataset"
score_pair=dict()
for i in range(0,len(list_file)):
	print "* file",list_file[i]
	data.read_pair_score(dir_data+"/"+list_file[i],nb_dataset,i,score_pair)
print "Number of genes pairs",len(score_pair.keys())

# Integration and report
print "Integration and Report of Pairs"
list_d=range(1,nb_m+1)
data.report_integration(f_out,score_pair,list_d)
