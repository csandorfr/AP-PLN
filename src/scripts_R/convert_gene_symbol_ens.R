# package
suppressMessages(library(biomaRt))

# remove warnings
options(warn=-1)

options(echo=TRUE)
args <- commandArgs(trailingOnly = TRUE)
print(args)


# parameters
f_gene <-args[1]
f_output=args[2]

# get list of genes
gene<-read.table(f_gene,header=FALSE)

# convert gene symbol to ensembl gene
ensembl = useEnsembl(biomart="ensembl", dataset="hsapiens_gene_ensembl")
query_ensembl<-getBM(attributes=c('ensembl_gene_id','hgnc_symbol'), filters ='hgnc_symbol', values =gene$V1, mart = ensembl)
list_gene_ens<-unique(query_ensembl$ensembl_gene_id)

# report
write.table(list_gene_ens,f_output,quote=F,sep="\t",row.names=F,col.names=F)
