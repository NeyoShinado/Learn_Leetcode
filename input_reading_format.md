##Input format
# R
con <- file("stdin", "r")
a = readlines(con, n=1)
a = strsplit(a, " ")[[1]][n]
while(...){
	cat(...)
	cat("\n")
}
close(con)


# python
# !/usr/bin/env
# coding = utf-8
while(...):
    a = []
    s = input()
    if s != "":
        for x in s.split():
            a.append(int(x))