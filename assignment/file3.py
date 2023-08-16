#write a program to merge two lists
#1
list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
merged_list=list1.copy()
for item in list2:
  if item not in merged_list:
    merged_list.append(item)
    print(merged_list)

list1=[1,2,3,4,5]
list2=[3,4,5,6,7]
merged_list=list1.copy()
for item in list2:
    merged_list.append(item)
    print(merged_list)

#2 how to find sum of list
numbers=[1,2,3,4,5] 
sum=0
for num in numbers:
    if num%2==0:
        sum+=num
print("sum of even numbers:",sum)

# print even numbers from list
numbers=[1,2,3,4,5,6,7,8,9,10]
print("even numbers:")
for num in numbers:
    if num%2==0:
        print(num)


#print odd numbers from list     
numbers=[1,2,3,4,5,6,7]
print("odd numbers:")
for num in numbers:
    if num%2!=0:
        print(num)

#delete element of given index
numbers=[10,20,30,40,50]
index_to_delete=3
if index_to_delete<len(numbers):
    del numbers[index_to_delete]
    print(numbers)

# delete element
my_list=[10,20,40,50,70,6]
del my_list[2]
print(my_list)
        
#2
my_list=[1,2,3,4,5,7,9]
my_list.remove(5)
print(my_list)

#3
my_list=[1,2,3,4,5]
del my_list[1:2]
print(my_list)

#insert a element at a given location
my_list=[1,2,3,4,5]
my_list.insert(2,6)
print(my_list)


fruits=['apple','bananna','orange']
my_list.insert
print(fruits)

#insert a element at end
my_list=[10,20,30,40]
my_list.append(50)
print(my_list)

#check the size of two list are same or not
#1
list1=[10,20,30,40]
list2=[40,50,60,70,80]
if len(list1)==len(list2):
    print("the size of both lists is the same.")
else:
    print("the size of both lists is different.")
