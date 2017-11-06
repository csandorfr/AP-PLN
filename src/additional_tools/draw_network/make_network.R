# package
library(biomaRt)
library(igraph)

options(echo=TRUE)
args <- commandArgs(trailingOnly = TRUE)
print(args)


# parameters
f_gene <-args[1]
f_net<-args[2]

# get list gene
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


# convert ensembl id to gene symbol
map_id<-query_ensembl[query_ensembl$ensembl_gene_id %in% list_gene_net,]
colnames(map_id)[1]<-"ID"
colnames(sub_net)<-"ID"
temp<-merge(sub_net,map_id,by="ID")
colnames(temp)[1]<-"Gene1"
colnames(temp)[2]<-"ID"
temp2<-merge(temp,map_id,by="ID")
sub_net_f<-temp2[,c(5,4,3)]
colnames(sub_net_f)<-c("source","target","weight")

# ipgraph object
pdf("network_representation.pdf")
net_gene<-as.data.frame(unique(c(as.character(sub_net_f[,1]),as.character(sub_net_f[,2]))))
net_links<-sub_net_f
colnames(net_gene)[1]<-"id"
colnames(net_links)[2]<-"to"
colnames(net_links)[1]<-"from"
net <- graph_from_data_frame(d=net_links, vertices=net_gene, directed=T)
#layout <- layout.reingold.tilford(net, circular=T)
layout=layout.fruchterman.reingold(net, niter=10000, area=30*vcount(net)^2)
plot(net, edge.arrow.size=0, vertex.size=8, vertex.frame.color="gray", vertex.label.color="black", vertex.label.cex=0.8, vertex.label.dist=0.1, edge.curved=0.2,layout=layout) 
dev.off()

# save the igraph object
save(net,file="net_igraph.Rdata")


