# Write a program that be able to find all factors of the numbers in the list l
l = [52633, 8137, 1024, 999]
# your code here
def print_factor(x):
    factor=[]
    for i in range(x+1):
      if i!=0 and x%(i)==0:
            factor.append(i)
    print(factor)
            

if __name__ == '__main__':
    for num in l:
        print_factor(num)