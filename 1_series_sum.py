"""
#version 1
import math

N, L = map(int, input().split())    #* map

for l in range(L, 102):
    if l <= 100:
        a = ((N - (l**2 - l)/2)/l)    #* ^ is not the power opetator
        if math.ceil(a) == a:
            for j in range(l-1):
                print(int(a + j), end=" ")    #* a is float
            print(int(a + l - 1))
            break
if l == 101:
    print("No")    #* Judging condition for NO pass 
#* python 不用担心溢出问题，因为溢出时会自动拓展数据类型
"""


#version 2
import math

N, L = map(int, input().split())
i = L
while i <= 100:
    a = (2 * N - i*(i - 1)) / (2 * i)
    if math.ceil(a) == a:
        for j in range(i- 1):
            print(int(a), end=" ")
            a += 1
        print(int(a))
        break
    i += 1
if i == 101:
    print("No")