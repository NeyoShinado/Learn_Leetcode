#1 
# input
con <- file("stdin", "r")
title = readLines(con, n=1)
title = strsplit(title, split=" ")[[1]]
n = as.numeric(title[1])
m = as.numeric(title[2])


#data = matrix(0, nrow = n, ncol = m)
data = t(sapply(1:n, function(i){
  line = readLines(con, n=1)
  line = strsplit(line, split=" ")[[1]]
  #data[i, ] = as.numeric(line)
  return(as.numeric(line))
}))


sub_max = sapply(1:m, function(i){
  sub = rep(max(data[, i]), n)
  return(sub)
})


candid = data - sub_max
acc = sapply(1:n, function(i){
  res = any(as.logical(!candid[i, ]))
  return(res)
})
ans = sum(acc)

cat(ans)
cat("\n")
close(con)
