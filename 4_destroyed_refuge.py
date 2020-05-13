#3 refuge
con <- file("stdin", "r")
title = readLines(con, n=1)
title = strsplit(title, split = " ")[[1]]
n = as.numeric(title[1])
m = as.numeric(title[2])


mask = matrix(0, 2, n)
#row.names(mask) = c("situation", "next")
#colnames(mask) = 1:n


mask[1, ] = 1
mask[2, ] = c(2:n, -1)

for(i in 1:m){
  event = readLines(con, n=1)
  event = strsplit(event, split=" ")[[1]]
  op = as.numeric(event[1])
  pos = as.numeric(event[2])
  
  if(op == 1){
    mask[1, pos] = 0
    if(pos == n){
      next = -1
    }else{
      next = mask[2, pos]
    }
  
    id = pos
    while(!mask[1, id] && id > 0){
      mask[2, id] = next
      id = id - 1
    }
  }
  
  if(op == 2){
    if(mask[1, pos]){
      cat(pos)
      cat("\n")
    }else{
      cat(mask[2, pos])
      cat("\n")
    }
  }
  
  return()
}

close(con)