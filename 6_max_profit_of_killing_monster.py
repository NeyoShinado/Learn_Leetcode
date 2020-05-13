#1 不需要按顺序杀怪

# 不需要按顺序杀怪
# input
lines=readLines("stdin")
for(l in lines){
  if(l == ""){
    break;
  }
  ll = strsplit(l, " ")[[1]]
  col1=ll[1];
  col2=ll[2];
}


n = col1[1]
m = col2[1]
c = col1[2:length(col1)]
w = col2[2:length(col2)]
max_gold = 0

sorted_profit = sort(w - round(c/m), 
                     decreasing = TRUE)

if(sorted_profit[1] <= 0){
  return(max_gold)
}else{
  kill_num = which(sorted_profit > 0)
  max_gold = sum(sorted_profit[1:kill_num])
  return(max_gold)
}




