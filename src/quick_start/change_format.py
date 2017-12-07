import re

def change_format_list_file(f_in,f_out,pln):

	f1=open(f_in,'r')
	f2=open(f_out,'w')
	for line in f1:
		file=line.rstrip()
		if re.search('final',file):
			type_file="PLN"
		else:
			type_file=file[0:7].upper()
		if type_file=='PLN' and pln==0: continue
		f2.write("%s\t%s\n" % (file,type_file))
	f1.close()
	f2.close()
