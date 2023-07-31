#check given number is positive or negative
#1
n=5
if n>=0:
 print("it is a positive number",n)  
else:
 print("it is a negative number",n)

#2
num=float(input("enter a number:"))
if num>0:
 print("positive number")
elif num==0:
 print("zero")
else:
 print("negative number")

#3
n=6
if n==0:
 print("it is a negative number",n)  
else:
 print("it is a positive number",n)

#4
n=-3
if n<0:
 print("it is a negative number",n)  
else:
 print("it is a positive number",n)

#5
n=0
if n<0:
 print("it is a negative number",n)  
else:
 print("it is a positive number",n)

#6
number=float(input("enter a number:"))
if number>0:
 print("the number is positive.")
elif number<0:
 print("the number is negative")
else:
 print("the number is zero")


# take two numbers check which one is greatest among them
#1
a=4
b=2
if a>b:
 print("a is greaterthan b")
else:
 print("b is greaterthan a") 

#2
num1=10
num2=20
if num1>num2:
 print("num1 is greater")
else:
 print("number2 is greater")

#3
 num1=7
 num2=7
if num1>num2:
  print("num1 is greater")
elif num2>num1:
 print("num2 is greater")
else:
 print("both number are equal")

#4
a=1
b=6
if a<b:
 print("b is greaterthan a")
else:
 print("ais greaterthan b") 

#5
 a=3
 b=6
if a>b:
  print("a is graterthan b")
else:
 print("b is graterthan a")

#6
 a=-7
 b=-4
if a>b:
  print("a is graterthan b")
else:
 print("b is graterthan a")


#take a string write program to repeat it 5 times

#1
n=int(input("enter a string"))
print(n*5)

#2
string="hello"
repeated_string=string*5
print(repeated_string)

#3
string="reddy"
repeated_string=string*5
print(repeated_string)

#4
string="pyton"
repeated_string=""
for _ in range(5):
 repeated_string+=string
 print(repeated_string)

#5
 string="Amma"
 repeated_string=""
for  _ in range(5):
 repeated_string+=string
 print(repeated_string)

#take a input from user and u have to check student is pass or fail 
#1
print('enter marks obtained in 3 subjects')
s1=int(input())
s2=int(input())
s3=int(input())
avg=(s1+s2+s3)/3
if s1>40 and s2>40:
 print('pass')
elif s2>40 and s3>40:
 print('pass')
elif s3>40 and s1>40:
 print('pass')
elif avg>40:
 print('pass')
else:
 print('fail')

#2
marks=float(input("enter the marks:"))
if marks>=50:
 print("pass")
else:
 print("fail")

#3
 marks=float(input("enter the marks:"))
if marks>=80:
 print("pass")
else:
 print("fail")

#4
 marks=float(input("enter the marks:"))
if marks<50:
  print("fail")
else:
 print("pass")
    
#take from user then print all even number,add all odd
#1
a=8
if a%2==0:
 print(" this is even number")
else:
 print("this is a odd number")

#2
test_list=[345,896,777,886,33]
print("the orginal list is :"+ str(test_list))
odd_sum=0
even_sum=0
for sub in test_list:
 for ele in str(sub):
  if int(ele)%2==0:
   even_sum+=int(ele)
else:
  odd_sum+int(ele)
print("odd digit sum:"+ str(odd_sum))
print("even digit sum:"+ str(even_sum))

#3
a=2
if a%2==0:
 print(" this is even number")
else:
 print("this is a odd number")

#4
numbers=input("enter a list of numbers separate by space:").split()
even_numbers=[]
odd_sum=0
for num in numbers:
 num=int(num)
if num%2==0:
 even_numbers.append(num)
else:
 odd_sum+=num
 print("even numbers:",even_numbers)
 print("sum of the numbers:",odd_sum)

#take two inputs on is length and breadth print this is a square
#1
a=3
b=6
if a==b:
 print(" it is a square")
else:
 print("it is not a square")

#2
a=3
b=3
if a==b:
 print(" it is a square")
else:
 print("it is not a square")

#3
a=4
if a>=18:
 print("it is a eligible for vote")
else:
 print("it is a not eligible for vote")
 
#take input which age and check he is eligible for vote or not
#1
a=18
if a>=18:
 print("it is a eligible for vote")
else:
 print("it is a not eligible for vote")

#2
a=20
if a>=18:
 print("it is a eligible for vote")
else:
 print("it is a not eligible for vote")

#3
 a=7
if a>=18:
  print(" it is a eligible for vote")
else:
 print("it is a not eligible for vote")

#take a string print half of the string
#1
def print_half_string(input_string):
  length=len(input_string)
  half_length=length//2
  half_string=input_string[:half_length]
  print("the first half of the string is:",half_string)
user_input=input("Enter a string:")
print_half_string(user_input)

#2
string="hello world"
half_length=len(string)//2
half_string=string[:half_length]
print(half_string)

#3
string="Python  Programming"
half_length=len(string)//2
half_string=string[:half_length]
print(half_string)

#4
string="Rushi Reddy"
haif_length=len(string)//2
half_string=string[:half_length]
print(half_string)

#5
string="anu,rushi"
half_length=len(string)//2
half_string=string[:half_length]
print(half_string)



#print a pattern with different shapes in python
#1
n=5
for i in range(0,n):
  for j in range(0,i+1):
   print("* ",end="")
  print()

#2
n=2
for i in range(0,n):
  for j in range(0,i+1):
   print("* ",end="")
  print()

#3
  n=11
for i in range(0,n):
  for j in range(0,i+1):
   print("* ",end="")
  print()

#4
  n=10
for i in range(0,n):
  for j in range(0,i+1):
   print("* ",end="")
  print()

#5
  n=6
for i in range(0,n):
  for j in range(0,i+1):
   print("* ",end="")
  print()


