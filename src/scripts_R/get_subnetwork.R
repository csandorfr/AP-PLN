# package
library(biomaRt)

options(echo=TRUE)
args <- commandArgs(trailingOnly = TRUE)
print(args)


# parameters
f_gene <-args[1]
f_net<-args[2]
f_output=args[3]

# get list of genes
gene<-read.table(f_gene,header=FALSE)

# convert gene symbol to ensembl gene
ensembl = useEnsembl(biomart="ensembl", dataset="hsapiens_gene_ensembl")
query_ensembl<-getBM(attributes=c('ensembl_gene_id','hgnc_symbol'), filters ='hgnc_symbol', values =gene$V1, mart = ensembl)

# get network
net<-read.table(f_net,header=FALSE,sep="\t",nrows=1000000)

# get sub network
index_net<-which(net$V1 %in% query_ensembl$ensembl_gene_id & net$V2 %in% query_ensembl$ensembl_gene_id)
sub_net<-net[index_net,]
list_gene_net<-unique(c(as.character(sub_net$V1),as.character(sub_net$V2)))
write.table(sub_net,f_output,quote=F,sep="\t",row.names=F,col.names=F)
