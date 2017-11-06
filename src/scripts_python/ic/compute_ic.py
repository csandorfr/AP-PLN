import sys
import data,functions

# Paramters
f_info_term=sys.argv[1]
f_ann_term=sys.argv[2]
f_out=sys.argv[3]

# Get info regarding phenotypic term
print "1) Read info regarding phenotypic term..."
info_term,list_term=data.get_info_term(f_info_term)
print "Number of term",len(info_term.keys()),len(list_term)

# get list of genes by phenotype annotation
print "2) Get the list of genes by phenotype annotations..."
annot=data.get_gene_phen_annot(f_ann_term)
print "Number of Annotation with at least one gene",len(annot.keys())

# Identify all child of each term
print "3) Identify Child..."
functions.list_child(info_term)

# Compute the number of gene in parent class term and it children
print "4) Compute number of gene in one class and it sub class..."
functions.number_gene_class(list_term,info_term,annot)

# compute information for each term
print "5) Compute IC of each Term..."
functions.compute_ic(info_term)

# report results
print "6) Report Results..."
data.report_ic(f_out,info_term,list_term)