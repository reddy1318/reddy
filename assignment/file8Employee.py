employee_name=[]
domain=[]
employee_id=[]
email=[]
n=int(input("Enter the no.of rows:"))
for x in range(n):
    a=input("Enter the employee name:")
    employee_name.append(a)
    b=input("Enter the domain:")
    domain.append(b)
    c=input("Enter the employee_id:")
    employee_id.append(c)
    d=input("Enter the email:")
    email.append(d)
print()
print('employee_name','domain','employee_id','email')
for a1,a2,a3,a4 in zip(employee_name,domain,employee_id,email):
    print(a1,a2,a3,a4,sep="\t")
print()


