from re import M
from string import *
from random import *

#6
list_=[]
m=randint(1,30)
for i in range(m):
    list_.insert(i,randint(1,1000))
print(list_)
max_=max(list_)
print("Maximum:",max_,",","Kokku",m)
arv=max_//m
indeks=list_.index(max_)
list_[indeks]=arv
print(list_)