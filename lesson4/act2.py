
def recur_factorial(l):
   if l == 1:
       return l
   else:
       return l*recur_factorial(l-1)

num = int(input("Enter a number"))

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))