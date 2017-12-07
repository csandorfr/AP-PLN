import sys
import data

# parameters
f_subnetwork=sys.argv[1]
f_listdata=sys.argv[2]
f_dir=sys.argv[3]
f_out=sys.argv[4]

# get the list of datasets
list_data_dict=data.list_dataset(f_listdata)
print "number of list of datasets",len(list_data_dict.keys())
list_data=list_data_dict.keys()

# get subnetwork
subnet=data.get_links(f_subnetwork,1000000000,len(list_data)+1)

# get info from individual datasets
n=1
for data_set in list_data:
        file=f_dir+"/"+list_data_dict[data_set]
        print file
        data.get_value_links(file,n,subnet)
        n+=1

# report
data.report(f_out,subnet,list_data)

