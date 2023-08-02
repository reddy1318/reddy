#accessing string by index method
#1
string="hello, World"
if string[0]=='h':
 print("the first character is 'h'")
else:
 print("the first character is not 'h'")

 #2
string="hello, world"
for i in range(len(string)):
  if string[i]=='o':
   print("the character'o' is found at index{i}")

 #3
string="hello, world"
for i in range(len(string)):
 if i%2==0:
    if string[i].isupper():
     print("the character at index", i,"is  an uppercase letter")
else:
 print("the character at index", i,"is not an uppercase letter")
  
# slicing
#1
string="rushi reddy"
print()

#2
string="rushi, reddy"
for char in string[::2]:
 print(char)

 #3
string ="reddy, rushi"
if string[:5]=="reddy":
  print("the string starts with 'reddy'")
else:
  print("the string does not start with 'reddy'")
   
#concatination 
#1
names=["aruna","babu","cherry","devi"]
concatenated_names=""
for names in names:
 if len(names)>4:
  concatenated_names+=names+""
  print(concatenated_names)

#2
string1="reddy"
string2="rushi"
result=string1+""+string2
print(result)  

#reputation
#1
reputation="great job"
count=0
for char in reputation:
 if char.isupper():
  count+=1
print("number of uppercase letters:", count)

#2
reputation="amazing"
reversed_reputation=""
for char in reputation:
 reversed_reputation=char
 reversed_reputation
 print("reversed reputation:",reversed_reputation) 

#3
reputation_string="hello, world"
if reputation_string.startswith("hello"):
 print("the string starts with 'hello'")
else:
 print("the string does not start with 'hello'")


#reverse index by string
my_string="Amma,Nanna"
for char in my_string:
 if char=="a":
  print("found'a'")

#2
my_string="banny, sunny"
for char in my_string:
 if char=='y':
  print(char)

# len()inbuit function
string="python, development"
length=len(string)
print(length)

#2
number=-4
if number>0:
 print("the number is positive")
elif number<0:
 print("the number is negitive")
else:
 print("the number is zero")
 #3
string=""
if len(string)==0:
  print("the string is empty")
else:
 print("the string is not empty")

#creating string
#1
x=10
if x>4:
 my_string="x is greater than 4"
else:
 my_string="x is less than or equal to 4"
print(my_string)

 #2
numbers=[1,2,3,4,5]
my_string=""
for num in numbers:
 my_string+=str(num)+""
print(my_string)

#membership checking in string
#1
string="python, code"
substring="code"
if substring in string:
  print("substring  found")
else:
  print("substring not found")
#2
string="development string"
substring="string"
if substring in string:
 print("substring  found")
else:
  print("substring not found")

 #3 
fruits=["apple","banana","orange"]
if 'apple' in fruits:
  print("apple is oresent in the list of fruits.")
else:
  print("apple is not present in the list of fruits.")






