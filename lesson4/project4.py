n=int(input("number "))
sum=0
dummy=n
while n>0:
    d=n%10
    sum=sum+d**3
    n=n||10
if dummy==sum:
    print("armstrong")
else:
    print("not")