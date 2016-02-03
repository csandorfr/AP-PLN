import sys
import data

# parameters
f_in=sys.argv[1]
f_out=sys.argv[2]

# get parameters scale
min_val,max_val=data.get_parameters_scale(f_in)
print "minimal value",min_val
print "maximal value",max_val

# scale the dataset
data.rescale(f_in,f_out,min_val,max_val)

