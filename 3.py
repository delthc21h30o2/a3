x=[]
y=[]

for i in range(5):
   
   m =int(input("enter number: "))

   x.append(m)
   y.append(m)

y.sort()
if y==x:
    print("✅")

else:
    print("⛔")
