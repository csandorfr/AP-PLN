

# package
options(echo=TRUE)
args <- commandArgs(trailingOnly = TRUE)
print(args)

# parameters
dir_data <-args[1]
f_dataset<-args[2]
random_val <- as.numeric(args[3])
f_graphe<-args[4]


# get the list of f_dataset
list_data<-read.table(f_dataset)
class(list_data)
nb_d<-length(list_data$V1)
print(nb_d)


# get info max x and y each dataset
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

# create png
png(filename =f_graphe, width = 480, height = 480,pointsize = 12, bg = "white")

# make graphe
par(mar=c(5.1, 4.1, 4.1, 8.1), xpd=TRUE)
color_val=sample(colours(), nb_d)
vect_name<-c()
vect_pch<-c()
for (i in c(1:nb_d)) {
	file=paste(dir_data,"/",list_data$V1[i],sep="")
	b<-unlist(strsplit(as.character(list_data$V1[i]), "_"))
	vect_name<-c(vect_name,b[1])
	pch_val <- sample(0:25, 1)
	vect_pch<-c(vect_pch,pch_val)
	data<-read.table(file)
	x<-log(data$V1)
	y<-data$V2
	print(file)
	if (i==1) {
		plot(x,y,ylim=c(min_y-0.01,max_y+0.01),xlim=c(min_x,max_x),col=color_val[i],pch=pch_val,ylab='Cumulative phenotypic semantic similarity',xlab='Log 10 of the coverage gene pairs')

	}
		points(x,y,col=color_val[i],pch=pch_val)
}
segments(min_x,random_val,max_x,random_val,col='gray',lty=2,lwd=2)
legend('topright',  inset=c(-0.2,0), vect_name, col=color_val,pch=vect_pch)
dev.off()
