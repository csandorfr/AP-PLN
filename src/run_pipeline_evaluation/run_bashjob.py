import os

def run_job_grid(script,dirOut,name,bash_script):
	
	# write bash script	
	f=open(bash_script,'w')
	f.write("%s\n" % (script))
	f.close()
	
	# submit job
	os.system("qsub -q medium_jobs.q -o %s -e %s -N %s %s" % (dirOut,dirOut,name,bash_script))	
