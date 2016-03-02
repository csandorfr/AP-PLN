options(echo=TRUE)
args <- commandArgs(trailingOnly = TRUE)
print(args)


# parameters
f_bench <-args[1]

# get value
data<-read.table(f_bench)
y<-data$V3

# random value
mean(y)

