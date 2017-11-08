# package
library(biomaRt)
library(igraph)
require(graphics)

options(echo=TRUE)
args <- commandArgs(trailingOnly = TRUE)
print(args)


# parameters
f_subnet<-args[1]
f_dir<-args[2]

# get network
sub_net<-read.table(f_subnet,header=FALSE,sep="\t",nrows=1000000)

# get list of genes
list_gene_net<-unique(c(as.character(sub_net$V1),as.character(sub_net$V2)))

# convert ensembl id to gene symbol
ensembl = useEnsembl(biomart="ensembl", dataset="hsapiens_gene_ensembl")
query_ensembl<-getBM(attributes=c('ensembl_gene_id','hgnc_symbol'), filters ='ensembl_gene_id', values =list_gene_net, mart = ensembl)

map_id<-query_ensembl[query_ensembl$ensembl_gene_id %in% list_gene_net,]
colnames(map_id)[1]<-"ID"
colnames(sub_net)<-"ID"
temp<-merge(sub_net,map_id,by="ID")
colnames(temp)[1]<-"Gene1"
colnames(temp)[2]<-"ID"
temp2<-merge(temp,map_id,by="ID")
sub_net_f<-temp2[,c(6,5,3,4)]
colnames(sub_net_f)<-c("source","target","weight","dataset")
dataset<-unique(as.character(sub_net_f$dataset))
palette(rainbow(n=length(dataset)))
colv<-palette()
Color<-colv[factor(sub_net_f$dataset)]
sub_net_f<-cbind(sub_net_f,Color)

f_out<-paste(f_dir,"network_representation_infoLinks.pdf",sep="/")
# ipgraph object
net_gene<-as.data.frame(unique(c(as.character(sub_net_f[,1]),as.character(sub_net_f[,2]))))
net_links<-sub_net_f
colnames(net_gene)[1]<-"id"
colnames(net_links)[2]<-"to"
colnames(net_links)[1]<-"from"
colnames(net_links)[4]<-"dataset"
net <- graph_from_data_frame(d=net_links, vertices=net_gene, directed=F)
#layout <- layout.reingold.tilford(net, circular=T)
#layout=layout.fruchterman.reingold(net, niter=10000, area=30*vcount(net)^2)
layout=layout_nicely
E(net)$color <- E(net)$Color

#draw plot
pdf(f_out,12,12)
par(mar = c(4, 4, 4, 20))
plot(net, edge.arrow.size=0, vertex.size=8, vertex.frame.color="gray", vertex.label.color="black", vertex.label.cex=0.8, vertex.label.dist=0.1, edge.curved=0,layout=layout) 
legend(x = "right", dataset , col=colv[length(colv):1],fill=colv[length(colv):1], bty='n', cex=1,inset = -.5, xpd = NA)
dev.off()

# save the igraph object
f_out<-paste(f_dir,"net_igraph.Rdata",sep="/")
save(net,file=f_out)


