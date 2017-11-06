import re,os

def get_list_file(dir):
	list_file=os.listdir(dir)
	for file in list_file:
		if re.search('dcas',file):
			f_dcas=file
		elif re.search('own_format.obo',file):
			f_term=file
		elif re.search('redundant.obo',file):
			f_redund=file
		elif re.search('genes_ens_to_phenotype_no_red.txt',file):
			f_annot=file
		else:
			print "file unknown",file
	return f_dcas,f_term,f_redund,f_annot

def test_file_annot(file):
	f=open(file,'r')
	pheno_mem=''
	n=0
	for line in f:
		term=line.rstrip()
		if re.search('MP',term):
			pheno='mgi'
		elif re.search('HP',term):
			pheno='hpo'
		else:
			print "Error: %s is not HPO or MGI annotations" % pheno
		if pheno_mem!=pheno and n > 0:
			print "Error: HPO and MGI annotations in the same file"
		n+=1
		pheno_mem=pheno
	return pheno_mem	
	
