import os

def get_list_file(file):
	f=open(file,'r')
	list_file=dict()
	for line in f:
		line=line.rstrip().split("\t")
		list_file[line[1]]=line[0]
	f.close()
	return list_file
