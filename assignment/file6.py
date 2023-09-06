
#recursive function
#1
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
n=int(input("enter the n-value:"))
res=factorial(n)
print(res)


# #2
def sum_of_digits(n):
    if n<20:
        return n
    else:
        return n%20+sum_of_digits

#3


def recursive_fibonacci(n):
    if n<=1:
        return n
    else:
        return(recursive_fibonacci(n-1)+recursive_fibonacci(n-2)) 
n_terms=10
if n_terms <=0:
   print("Invalid input! please input a positive value ")
else:
    print("Fibonacci series:")
for i in range(n_terms):
    print(recursive_fibonacci(i))



# Lambda function
#1
finding_smallest_value=lambda a,b:a if a<b else b
print(finding_smallest_value(30,40))

#2
numbers=[1,2,3,4,5,6,7,8,9,10]
even_numbers=list(filter(lambda x:x%2==0,numbers))
print(even_numbers)

# #3
def myfunc(n):
    return lambda a:a*n
mydoubler=myfunc(2)
print(mydoubler(11))


# filter() function
#
def check_odd(a):
    if a%2==0:
        return False
    else:
        return True
l=[1,2,3,4,5,6,7,8,9,10]
l1=list(filter(check_odd,l))
print(l1)

#
nums=[5,6,7,87,88,93,54,10,0,-13,-14,6,-33]
odd=filter(lambda p:p%2 !=0,nums)
even=filter(lambda p:p%2==0,nums)
print("The list odd numbers is:",list(odd))
print("The list even numbers is:",list(even))

# 
numbers=[-3,-4,-1,0,1,2,3]
positive_numbers=list(filter(lambda x:x>0,numbers))
print(positive_numbers)


  