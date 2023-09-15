#.Write a Python script to add a key to a dictionary.
my_dict={0: 10, 1: 20}
my_dict[2]=30
print(my_dict)
#Write a Python script to check whether a given key already exists in a dictionary.
my_dict={'a':1,'b':2,'c':3}
key_to_check='c'
key_exists=False
for key in my_dict:
    if key==key_to_check:
        key_exists=True
        break
    if key_exists:
        print(f"the key'{key_to_check}' exists in the dioctionary.")
    else:
        print(f"the key'{key_to_check}'  does not exists in the dioctionary.")

#Write a Python program to iterate over dictionaries using for loops
my_dict={0: 10, 1: 20, 2: 30}
print(my_dict)
print("for printing iterating keys")
for a in my_dict.keys():
    print(a)

print("for iterating values")
for b in my_dict.values():
    print(b)
print("printing both keys and values")  
for i,j in my_dict.items():
    print(i,"----",j)
#Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
my_dict={}
for num in range(1,16):
    my_dict[num]=num**2

for key,value in my_dict.items():
    print(f"{key}: {value}")

#Write a Python program to sum all the items in a dictionary.
sample_string="marolix technology"
letters_count={}
for char in sample_string:
    if char !='':
        if char in letters_count:
            letters_count[char]+=1
        else:
            letters_count[char]=1
print(letters_count)

#7.Write a Python program to combine two dictionary by adding values for common keys.
my_dict={0: 10, 1: 20, 2: 30}
total_sum=0
for value in my_dict.values():
    total_sum+=value
print("sum of the items in the dictionary:",total_sum)

#Write a Python program to access dictionary key's element by index.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
combined_dict={}
for key in d1:
    if key in d2:
        combined_dict[key]=d1[key]+d2[key]
    else:
        combined_dict[key]=d1[key]
for key in d2:
    if key not in combined_dict:
        combined_dict[key]=d2[key]   
print(combined_dict) 

#Write a Python program to access dictionary key's element by index.
my_dict={'maths':60,'physics':70,'chemistry':50}
for key in my_dict.keys():
    print(key)
#write a Python program to remove a key from a dictionary.

# my_dict = {'a': 10, 'b': 20, 'c': 30}
# print(my_dict)
# key_to_remove = 'b'
# if key_to_remove in my_dict:
#     new_dict={}
#     for v in my_dict.items():
#         if key != key_to_remove:
#             print(key)
#     my_dict = new_dict
#     print(my_dict)
# else:
#     print("key not found")
# Write a Python script to merge two Python dictionaries.d
d1={'a':100,'b':200}
d2={'b':300,'c':400}
merged_dict={}
for key,value in d1.items():
    merged_dict[key]=value
for key,values in d2.items():
    merged_dict[key]=value
print(merged_dict)
