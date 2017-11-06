

best_parameter <- function(dir_data,nb_d,suffixe) {
	best_d<-0
	f_value_mem<-0
	for (i in c(1:nb_d)) {
		file=paste(dir_data,"/wl_",suffixe,"_d",i,"_bench",sep="")
		data<-read.table(file)
		x<-data$V1
		y<-data$V2
		linear_model<-lm(formula = y ~ poly(x, 1, raw = TRUE))
		stat<-summary(linear_model)
		f_value<-stat$fstatistic[1]
		if (f_value > f_value_mem) {
			f_value_mem<-f_value
			best_d<-i
		}

	}
	return (best_d)
}

make_graphe  <- function(f_graphe,d,dir_data,nb_d,suffixe) {

	# plot rescale
	png(filename =f_graphe, width = 480, height = 480,pointsize = 12, bg = "white")
	
	for (i in c(1:nb_d)) {
		file=paste(dir_data,"/wl_",suffixe,"_d",i,"_bench",sep="")
		data<-read.table(file)
		x<-data$V1
		y<-data$V2
		if (i==d) {
			color='red'
		}
		else {
			color='black'
		}
		if (i==1) {
			plot(x,y,xlab='',ylab='',main='',col=color)
		}
		else {
			points(x,y,col=color)
		}
	}
		
	dev.off()
}



# package
options(echo=TRUE)
args <- commandArgs(trailingOnly = TRUE)
print(args)

# parameters
dir_data <-args[1]  
nb_d<- as.numeric(args[2]) 
f_graphe<-args[3]
f_out<-args[4]
suffixe<-args[5]


# determine best parameter
d<-best_parameter(dir_data,nb_d,suffixe)
print(d)

# make graphe of different fit
make_graphe(f_graphe,d,dir_data,nb_d,suffixe)

sink(f_out, append=FALSE, split=FALSE)
print(d)
#sink()
