import sys
import data,functions

# Parameters
f_list_term=sys.argv[1]
f_info_term=sys.argv[2]
f_redund=sys.argv[3]
f_ann_term=sys.argv[4]
f_out=sys.argv[5]


# Get redundant phenotypic redundant annotation
print "1) Read Redundant Annotation..."
convert=data.get_redundant_term(f_redund)
print "Number of redundant Gene",len(convert.keys())

# Get the list of phenotypic term
print"2) Read Redundant Annotation..."
list_subset_term=data.get_list_term(f_list_term,convert)
print "Number of Term in Subset",len(list_subset_term.keys())

# Get info regarding phenotypic term
print "3) Read info regarding phenotypic term..."
info_term,list_term=data.get_info_term(f_info_term)
print "Number of term",len(info_term.keys()),len(list_term)

for term in list_subset_term.keys():
	print "%s,%s,%s" % (term,info_term[term]['generation'],info_term[term]['name'])

# Identify all child of each ter,
print "4) Identify Child..."
functions.list_child(info_term)

# identify child (propagation) of subset term
print "5) Identify Term Subset..."
child=dict()
for term in list_subset_term.iterkeys():
	child[term]=1
	functions.identify_child(term,info_term,child)
print "Number of term",len(child.keys())

# Consider only gene annotated with relevant phenotypic term
print "6) Keep only gene annoted with relevant term..."
data.take_subset_annot_gene(f_ann_term,f_out,child)
