setwd("C:/Users/liang/Desktop/htseq-cts")
directory <- "C:/Users/liang/Desktop/htseq-cts"
sampleFiles <- list.files(directory)
sampleCondition <- factor(c("air", "air", "air", "csc", "csc", "csc"))
sampleCondition
sampleTable <- data.frame(sampleName = sampleFiles,
                          fileName = sampleFiles,
                          condition = sampleCondition)
sampleTable$condition <- factor(sampleTable$condition)
sampleTable

library("DESeq2")
ddsHTSeq <- DESeqDataSetFromHTSeqCount(sampleTable = sampleTable,
                                       directory = directory,
                                       design= ~ condition)

keep <- rowSums(counts(ddsHTSeq)) >= 10
ddsHTSeq <- ddsHTSeq[keep,]

ddsHTSeq

ddsHTSeq$condition <- relevel(ddsHTSeq$condition, ref = "air")

colData(ddsHTSeq)$condition<-factor(colData(ddsHTSeq)$condition, levels=c('air','csc'))
dds<-DESeq(ddsHTSeq)
res<-results(dds, alpha=0.01)
res<-res[order(res$padj),]
head(res)
res

res <- results(dds, contrast=c("condition","csc","air"))
resOrdered <- res[order(res$pvalue),]
resOrdered
summary(res)

write.csv(resOrdered, "bmefinal-deseq2-res.txt", row.names=TRUE)


