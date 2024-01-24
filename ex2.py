# Write a function that prints all factors of the given parameter x
def print_factor(x):
# your code here
   factors=[]
   for i in range(x+1):
      if i!=0 and x%(i)==0:
         factors.append(i)
   print(factors)
          
if __name__=='__main__':
   print_factor(52633)