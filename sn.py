x=int(input())



s=[]



for i in range(0,x):


    s.append("*")



for b in range(1,x,2):


    s[b]="#"

for i in range(x):


    print(s[i],end='')