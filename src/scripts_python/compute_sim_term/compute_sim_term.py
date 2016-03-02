import sys
import data

# Parameters
f_dcas=sys.argv[1]  # /net/isi-scratch/cynthia/DATA/T2D/HPO/DCAS/dcas
f_ic=sys.argv[2]
f_out=sys.argv[3] # /net/isi-scratch/cynthia/DATA/T2D/HPO/SIMTERM/semantic_sim_term_hpo_t2d.txt

# get information for each term
print "1) Get information content for each term"
ic=data. get_ic(f_ic)
print "Number of term with ic",len(ic.keys())

# compute sematic similaritu between each term pairs
print "2) Compute semantic similarity between each pair terms"
data.compute_score_sem_sim(f_dcas,f_out,ic)
