import random
import datetime

def all_pairs(lst):
    if len(lst) < 2:
        yield []
        return
    
    a = lst[0]
    for i in range(1,len(lst)):
        pair = (a,lst[i])
        for rest in all_pairs(lst[1:i]+lst[i+1:]):
            yield [pair] + rest
         
y = list(all_pairs(['basira','gaby','iman','hasanat','krushang','rajiv','tamar','xiaona']))   
x = datetime.datetime.now()
random.seed(x.strftime("%j"))
random.shuffle(y)
l = y[0]
print(l)
