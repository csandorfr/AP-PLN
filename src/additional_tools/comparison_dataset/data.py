import os

def get_list_file(file):
	f=open(file,'r')
	list_file=[]
	for line in f:
		list_file.append(line.rstrip())
	f.close()
	return list_file
