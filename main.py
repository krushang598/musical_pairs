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
         
#y = list(all_pairs(['basira','gaby','iman','hasanat','krushang','rajiv','tamar','xiaona']))   
file_F = open('list.txt','r')
content = file_F.read()
l = content.split("\n")
l[:] = [k for k in l if k]
file_F.close()

x = datetime.datetime.now()
random.seed(x.strftime("%j"))
random.shuffle(l)

print(l.pop(0))

file_F = open('list.txt','w')
for i in l:
    file_F.write(str(i) + "\n")    
file_F.close()
