import sys
import data
import functions

# Parameters
f_sim_term=sys.argv[1] 
f_annot_gene=sys.argv[2]
f_out=sys.argv[3]

# Read semantic similarity between each term pairs
print "1) Read semantic similarity between each term pairs"
sim_term=data.get_sim_term(f_sim_term)
print "Number of term pairs with disjoint common ancestor",len(sim_term.keys())

# Get phenotypic annotation gene
print "2) Get phenotypic annotation gene"
annot_gene=data.get_gene_annotation(f_annot_gene)
print "Number of Gene",len(annot_gene.keys())

# Comparison gene product
print "3) Comparison Gene Product..."
score_pair=functions.comparing_gene_product(annot_gene,sim_term)
print "Number of genes pair with score",len(score_pair.keys())

# report semantic similarity score
print "4) Report of results..."
data.report_semantic_sim(f_out,score_pair)
