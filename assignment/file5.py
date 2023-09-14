#1.Write a Python function that accepts a string and counts the number of upper and lower case letters
def count_case_characters(input_string):
 upper_count=0
 lower_count=0
 for char in input_string:
     if char.isupper():
        upper_count +=1
     elif char.islower():
        lower_count +=1
 return f" no.of upper case characters: {upper_count}\n no.of lower case characters: {lower_count}"
sample_string='The quick Brow Fox'
result=count_case_characters(sample_string)
print(result)

#2.Write a Python function that takes a list and returns a new list with distinct elements from the first list.
def get_unique_elements(lst):
    return list(set(lst))
sample_list=[1,2,3,3,3,3,4,5]
unique_list=get_unique_elements(sample_list)
print(unique_list)    
#3Write a Python function to check whether a string is a pangram or not.
def is_pangram(string):
    string=string.lower()
    alphabet=set()
    for char in string:
        if char.isalpha():
            alphabet.add(char)
    return len(alphabet)==26
print(is_pangram("The quick brown fox jumps over the lazy dog"))


#4.Write a Python function to create and print a list where the values are the squares of numbers between 1 and 10 (both included).
def create_square_list():
    square_list=[x**1 for x in range(1,11)]
    return square_list
squares=create_square_list()
print(squares)
#5.Write a Python function to sum all the numbers in a list.
def sum_of_list(numbers):
    total=0
    for num in numbers:
        total +=num
    return total
sample_list=[8,2,3,0,7]
result=sum_of_list(sample_list)
print(result)
#6write a function to find sum of given values, pass values has variable number of arguments to function.

def sum_of_values(*args):
    total=0
    for value in args:
        total +=value
    return total
result=sum_of_values(1,2,3,4,5)
print(result)







