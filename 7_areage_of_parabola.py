lines=readLines("stdin")
A = NULL
B = NULL
C = NULL
S = 0

for(l in lines){
  if(l == ""){
    break;
  }
  ll = strsplit(l, " ")[[1]]
  if(length(ll) == 1){
    T = as.numeric(ll[1])
  }else{
    A = c(A, as.numeric(ll[1]))
    B = c(B, as.numeric(ll[2]))
    C = c(C, as.numeric(ll[3]))
  }
}

S = sapply(1:T, function(i){
  a = A[i]
  b = B[i]
  c = C[i]
  
  delta = 1/(b^2) - (2*c)/(a*b)
  if(delta <= 0){
    s = 0
    return(s)
  }else{
    
    integrand <- function(x, a, b, c){
      -(x^2/(2*a) - x/b + c/b)
    }
    
    x1 = a * (1/b - sqrt(delta))
    x2 = a * (1/b + sqrt(delta))
    s = integrate(integrand, lower = x1, upper = x2)$value
    return(s)
  }
  
})
cat(S);
cat("\n")

  
  