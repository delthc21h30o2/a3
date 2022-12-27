n1=int(input("first number: "))


n2=int(input("s number: "))



for i in range(min(n1,n2),0,-1):


    if (n1% i ==0) and (n2% i == 0):

        b=i

        k=n1*n2/b

        print(k)

        break