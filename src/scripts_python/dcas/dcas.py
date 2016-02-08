import sys
import data
import functions

# Parameters
f_info_term=sys.argv[1]
f_dcas=sys.argv[2]

# Get info regarding phenotypic term
print "1) Read info regarding phenotypic term..."
info_term,list_term=data.get_info_term(f_info_term)
print "Number of term",len(info_term.keys()),len(list_term)

# determine full list of all ancestor term
print "2) determine full list of all ancestor term..."
functions.list_ancestor(info_term)
print "done"


# report the list of disjunct comman ancestor by term pairs
print "3) determine full list of all ancestor term..."
data.report_dcas_pairs(f_dcas,list_term,info_term)

