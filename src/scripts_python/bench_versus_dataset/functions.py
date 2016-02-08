import operator

def sort_by_val(score):
	list_pair=[]
        sorted_x = sorted(score.iteritems(), key=operator.itemgetter(1))
        for i in range(0,len(sorted_x)):
                list_pair.append(sorted_x[i][0])
        list_pair.reverse()
        return list_pair

def convert(gene,gene_convert):
        if gene_convert.has_key(gene):
                ref_gene=gene_convert[gene]
        else:
                ref_gene=gene
        return ref_gene
