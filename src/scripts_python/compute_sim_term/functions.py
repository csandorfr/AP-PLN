import numpy as np

def comparison_term(list_dcas,ic):
	list_ic,score=[],'NaN'
	for term in list_dcas:
		try:
			list_ic.append(ic[term])
		except:
			continue
	if len(list_ic) !=0:
		score=np.mean(list_ic)
	return score
