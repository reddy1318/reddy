# Armstrong number
num=int(input("Enter a number:"))
sum=0
temp=num
n=len(str(num))
while temp>0:
    digit=temp % 10
    sum +=digit ** 3
    temp //=10
if sum==num:
    print(num,"is armstrong number")
else:
    print(num,"is not armstrong number")