

intersection <- function(x,y,index_ref,min_x,max_x,ref_val) {
	model_ref<-earth(x,y)
	x_mod<-seq(min_x,max_x, length = length(x))
	y_mod<-predict(model_ref,newdata = data.frame(x_mod))
	intercept<-estimation_intercept(x_mod,y_mod,ref_val)	
	return(intercept)
}

estimation_intercept<-function(x,y,ref_val) {
	intercept<-NA
	for (i in 1:length(x)) {
		if (y[i] > ref_val) {
			intercept <-x[i]
			break
		}
	}
	return(intercept)
}

# package
suppressMessages(library('earth'))


# remove warnings
options(warn=-1)

options(echo=TRUE)
args <- commandArgs(trailingOnly = TRUE)
print(args)


# parameters
f_measure_mgi <-args[1]
random_val <- as.numeric(args[2])
f_pair_gene<-args[3]
f_pair_gene_rescale<-args[4]
f_graphe_report<-args[5]


# read data 
data<-read.table(f_measure_mgi)
x<-data$V1
y<-data$V2



# get intercept
intercept<-intersection(x,y,index,min(x),max(x),random_val)
intercept

# get informative
datasub <- subset(data, data$V1 > intercept)
xsub<-datasub$V1
ysub<-datasub$V2

# multivariate adaptive regression splines
model_earth<-earth(xsub,ysub) 
coefficient<-coef(summary(model_earth))
coefficient
for (i in 2:length(coefficient)){
	if (coefficient[i] < -0.1) {
		model_earth<-earth(xsub,ysub,linpreds=1)
		break
	}
}
summary(model_earth)

# apply this model full data
data_full<-read.table(f_pair_gene)
data_full_sub <- subset(data_full, data_full$V3 > intercept)
ypredict<-predict(model_earth,newdata = data.frame(data_full_sub$V3))
data_new<-data.frame(data_full_sub$V1,data_full_sub$V2,ypredict)
write.table(data_new, file = f_pair_gene_rescale, sep = "\t",quote=FALSE,row.names = FALSE,col.names=FALSE)

# plot rescale
png(filename =f_graphe_report, width = 480, height = 480,pointsize = 12, bg = "white")
plot(x,y,xlab='',ylab='',main='')
x_plot<-seq(intercept,1, length = 200)
y_plot<-predict(model_earth,newdata = data.frame(x_plot))
points(x_plot,y_plot,col='blue')
abline(v=intercept,col='blue')


abline(h=random_val,col='gray',lty=2,lwd=2)
dev.off()

