#
# Package
#
options(echo=TRUE)
args <- commandArgs(trailingOnly = TRUE)
print(args)

#
# Parameters
#
dir_data <-args[1]
f_dataset<-args[2]
random_val <- as.numeric(args[3])
f_graphe<-args[4]

#
# Get the list of f_dataset
#
list_data<-read.table(f_dataset,header=FALSE,sep="\t")
nb_d<-length(list_data$V1)
list_data$color_val<-rainbow(n=nb_d)
list_data$PCH<-rep(21,nb_d)
list_data$LTY<-rep(1,nb_d)
even_indexes<-seq(1,nb_d,2)
list_data$LTY[even_indexes]<-2

#
# Get info max x and y each dataset
#
max_x=0
max_y=0
min_x=20000
min_y=1
for (i in c(1:nb_d)) {
	file=paste(dir_data,"/",list_data$V1[i],sep="")
	data<-read.table(file)
	x<-log(data$V1)
	y<-data$V2
	if (max(x) > max_x) {
		max_x=max(x)
	}
	if (max(y) > max_y) {
                max_y=max(y)
	if (min(x) < min_x) {
		min_x=min(x)
	}
	if(min(y) < min_y) {
		min_y=min(y)
	}	
        }
}

#
# Make Plot
#

pdf(f_graphe)

par(mar=c(6.1, 4.1, 4.1, 2.1))
for (i in c(1:nb_d)) {
        file=paste(dir_data,"/",list_data$V1[i],sep="")
        data<-read.table(file)
        x<-log(data$V1)
        y<-data$V2
        if (i==1) {
                 plot(x,y,ylim=c(random_val-0.01,max_y+0.01),xlim=c(min_x,max_x),col=list_data$color_val[i],pch=list_data$PCH[i],ylab='Cumulative phenotypic semantic similarity',xlab='Coverage gene-gene links',type="o",xaxt = 'n',lty=list_data$LTY[i])
                axis(1, labels = FALSE)

        }
                points(x,y,col=list_data$color_val[i],pch=list_data$PCH[i],type="o",lty=list_data$LTY[i])
}

# random pairs of genes
segments(min_x,random_val,max_x,random_val,col='gray',lty=2,lwd=2)

# legend 
legend('topright',  inset=-0.01,-0.01,as.character(list_data$V2), col=list_data$color_val,pch=list_data$PCH,lty=list_data$LTY, yjust=0,xjust=0,cex = 1,pt.cex=2,y.intersp=0.8)

# label x axis
axis_x<-seq(round(min_x)+1,round(max_x),2)
axis(1, at=axis_x,labels=FALSE)
x_lab<-sapply(axis_x,function(x) 10**x)
text(x=axis_x, y=par()$usr[3]-0.03*(par()$usr[4]-par()$usr[3]),labels=x_lab, srt=45, adj=1, xpd=TRUE,cex=0.8)


# close graph
dev.off()
