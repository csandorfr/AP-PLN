
best_index_polynomial <- function(x,y,i){
	
	model1<-lm(y ~ poly(x,i, raw = TRUE))
	model2<-lm(y ~ poly(x,i+1, raw = TRUE))
	anova_test<-anova(model1,model2)
	p<-anova_test['Pr(>F)'][2,1]
	if (is.na(p)) {
		index<-i
	}
	else{
		if (p > 0.00001){
			index<-i
		}
		else {
			index<-best_index_polynomial(x,y,i+1)
		}
	}
	return(index)
}

intersection <- function(x,y,index_ref,min_x,max_x,ref_val) {
	model_ref<-lm(y ~ poly(x,index_ref, raw = TRUE))
	x_mod<-seq(min_x,max_x, length = length(x))
	y_mod<-predict(model_ref,newdata = data.frame(x_mod))
	y_mod<-rev(y_mod)
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
library('earth')

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

# fit polynomial
index<-best_index_polynomial(x,y,1)
index

# get intercept
intercept<-intersection(x,y,index,min(x),max(x),random_val)
intercept

# get informative
datasub <- subset(data, data$V1 > intercept)
xsub<-datasub$V1
ysub<-datasub$V2

# multivariate adaptive regression splines
model_earth<-earth(xsub,ysub) 

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

model_ref<-lm(y ~ poly(x,index, raw = TRUE))
x_mod<-seq(min(x),max(y), length = length(x))
y_mod<-predict(model_ref,newdata = data.frame(x_mod))
y_mod<-rev(y_mod)

points(x_mod,y_mod,col='red')
abline(h=random_val,col='gray',lty=2,lwd=2)
dev.off()

