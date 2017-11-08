def get_links(file,nb_links,nb_sample):
        f=open(file,'r')
        score=dict()
        n=0
	f.readline()
        for line in f:
                line=line.rstrip().split("\t")
                gene1=line[0]
                gene2=line[1]
                value=float(line[2])
                pair=gene1+":"+gene2
                n+=1
                if n> nb_links: break
                score.setdefault(pair,[0]*nb_sample)
                score[pair][0]=value
        f.close()
        return score

def list_dataset(file):
        list_data=[]
        f=open(file,'r')
        for line in f:
                line=line.rstrip()
                list_data.append(line)
        return list_data

def get_value_links(file,n,score):

        f=open(file,'r')
        for line in f:
                line=line.rstrip().split("\t")
                gene1=line[0]
                gene2=line[1]
                value=float(line[2])
                pair1=gene1+":"+gene2
                pair2=gene2+":"+gene1
                if score.has_key(pair1):
                        pair=pair1
                elif score.has_key(pair2):
                        pair=pair2
                else:
                     	continue
                score[pair][n]=value
        f.close()


def report(file,score,list_data):
        f=open(file,'w')
        for pair in score.iterkeys():
                gene=pair.split(":")
                value=score[pair][0]
                dataset=det_max_dataset(score[pair],list_data)
                f.write("%s\t%s\t%s\t%s\n" % (gene[0],gene[1],value,dataset))
        f.close()


def det_max_dataset(score,list_data):
        mem=list_data[0]
        max_val=0
        for i in range(0,len(list_data)):
                if max_val < score[i+1]:
                        mem=list_data[i]
                        max_val=score[i+1]
        return mem


