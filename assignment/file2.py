#write a  python program to remove character from string

#1
def remove_character(string,char):
    new_string=""
    for c in string:
     if c !=char:
        new_string+=c
        return new_string
string="apple,orange"
char="p"
new_string=remove_character(string,char)
print(new_string)

#2
def remove_char(string,char):
   return string.replace(char,"")
input_string="amma,nanna"
char_to_remove="a"
output_string=remove_char(input_string,char_to_remove)
print(output_string)


#write a program to check string is palindrome or not 

#1
def is_palindrome(string):
   string=string.replace("","").lower()
   if string==string[::-1]:
      return True
   else:
      return False
strings=["non","madam","amma","nanna","racecar"]
for string in strings:
   if is_palindrome(string):
      print(f"{string} is a palindrome")
   else:
      print(f"{string} is not a palindrome")

#2
def is_palindrome(string):
   string=string.lower()
   reversed_string=string[::-1]
   return string==reversed_string
print(is_palindrome("hello"))
print(is_palindrome("car"))
print(is_palindrome("bujji"))

# write a program program to check given character is vowel or consonant
def check_vowel_or_consonant(char):
 vowels=['a','e','i','o','u']
 if char.lower()in vowels:
    return"vowel"
 else:
    return "constant"
 character=input("enter a character:")
 result=check_vowel_or_consonant(charcater)
 print(f"the character'{character}' is a {result}.")

#write a python program to replace string space with given character in python
 #1
def replace_space(string,character):
  return string.replace('', character)
input_string="reddy rushi"
replacement_character='-'
output_string=replace_space(input_string,replacement_character)
print(output_string)

#2
input_string="python is awesome"
replacement_character='*'
output_string=replace_space(input_string,replacement_character)
print(output_string)
#write a python program to count alphabets,digits,and special characters in the string
#1
def count_characters(string):
 alphabets=digits=special_chars=0
 for char in string:
  if char.isalpha():
   alphabets+=1
  elif char.isdigit():
   digits+=1
  else:
   special_chars+=1
   return alphabets,digits,special_chars
string="hello world 123"
alphabets,digits,special_chars=count_characters(string)
print("Alphabets:",alphabets)
print("Digits:",digits)
print("Special Characters:",special_chars)
string="hello 123@#"
alphabets,digits,special_chars=count_characters(string)
print("Alphabets:",alphabets)
print("Digits:",digits)
print("Special Characters:",special_chars)


#write a python program to remove all the blank spaces in a given string
#1
def remove_spaces(string):
   words=string.split()
   new_string=''.join(words)
   return new_string
input_string="Hello World"
output_string=remove_spaces(input_string)
print(output_string)

#2
input_string="python programming"
output_string=remove_spaces(input_string)
print(output_string)

#write a python program to find sum of integers in the string
#1
stri=input('enter a string')
sum=0
for i in string:
   if i.isdigit():
      sum=sum+int(i)
print("sum=",sum)



#write a python program to remove repeated character from string
#1
def remove_char(string,char):
 return string.replace(char,"")
string="Hello,World"
char="o"
new_string=remove_char(string,char)
print(new_string)

#2
string="python program"
char="p"
new_string=remove_char(string,char)
print(new_string)

# write a python program to counts occurrence of given character in string
#1
string='abcdef'
char=input('enter character')
i=0
count =0
while(i<len(string)):
   if(string[i]==char):
      count = count+1
   i+=1
   print('total number of', char,'is',count)

#2
def countChars(string):
   chars={}
   for char in string:
      if char in chars:
         chars[char]==1
      else:
         chars[char]=1
   return chars
string="program"
chars=countChars(string)
for char,count in countChars("program").items():
   print(f"{char}:{count}")
   

# write a python program to check string is anagrams or not in python
#1
str1=input("Enter the string1")
str2=input("Enter the string2")
if(len(str1)!=len(str2)):
   print("The strings are not anagrams")
else:
   if(sorted(str1)==sorted(str2)):
    print("the strings are anagrams")
   else:
    print("the strings are anagrams")



# write a python program to sort the characters of the string and first alphabet symbols followed by numeric valuse
#1
s=input("enter some alphanumeric string to sort")
alphabets=[]
digits=[]
for ch in s:
   if ch.isalpha():
      alphabets.append(ch)
   else:
      digits.append(ch)
output=''.join(sorted(alphabets)+sorted(digits))
print(output)

#2
s='B4A3T1'
alphabets=[]
digits=[]
for ch in s:
   if ch.isalpha():
     alphabets.append(ch)
   else:
      digits.append(ch)
output=''.join(sorted(alphabets)+sorted(digits))
print(output)
