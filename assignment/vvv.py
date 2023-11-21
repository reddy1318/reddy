# 1write a program reverse an integer in python
def reverse_integer(number):
    reversed_str=str(number)[::-1]
    reversed_number=int(reversed_str)
    return reversed_number
input_number=123456
result=reverse_integer(input_number)
print(f" {input_number} {result}")

#2 reverse using while loop
num=1234
reversed_num=0
while num!=0:
    digit=num%10
    reversed_num=reversed_num*10+digit
    num//=10
print("reversed number:"+str(reversed_num))

#3reverse string slicing
num=2345
print(str(num)[::-1])
