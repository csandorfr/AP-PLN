# remove warnings
options(warn=-1)

options(echo=TRUE)
args <- commandArgs(trailingOnly = TRUE)
print(args)


# parameters
f_sum<-args[1]
f_pval<-args[2]
f_dir<-args[3]
out_name<-args[4]

# get network
score<-read.table(f_sum,header=FALSE,sep='\t')
p_val<-read.table(f_pval,header=FALSE,sep='\t')

# function to norm score
range01 <- function(x){(x-min(x))/(max(x)-min(x))}

# title
if (p_val$V3==0) {
  title=paste("pval <",(p_val$V1)**-1,sep=' ')
} else {
  title=paste("pval =",(p_val$V3),sep=' ')
}


# make graphe
file<-paste(out_name,"stat_clustering.pdf",sep="_")
f_out<-paste(f_dir,file,sep="/")
pdf(f_out,12,12)
score_norm<-range01(score$V1)
hist(score_norm,xlab='Random distribution of the\n sum of weighted linked within gene network',ylab='Density',main=title,breaks=100)
abline(v=score_norm[1],col='red')
dev.off()

