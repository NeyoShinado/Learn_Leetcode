col1 = NULL
col2 = NULL

lines=readLines("stdin", n=1)

ll = strsplit(lines[1], " ")[[1]]
N = ll[1]
K = ll[2]
lines = lines[-1]
fea = NULL

for(l in lines){
  if(l == ""){
    break;
  }
  ll = as.numeric(strsplit(l, " ")[[1]])
  fea = rbind(fea, ll)
}


sim = sapply(1:n, function(i){
  sapply(1:i, function(j){
    res = rep(0, N)
    for(k in c(2:K)){
      sum = fea[i, 1] + fea[j, 1]
      if((fea[i, k] + fea[j, k]) == sum){
        next;
      }else{
        sim = 0
        return(sim)
        break;
      }
      sim = 1
      return(sim)
    }
  })
})

res = sum(apply(sim, 1, sum))
cat(res);
cat("\n")
