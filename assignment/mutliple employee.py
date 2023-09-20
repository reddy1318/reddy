def add_employees():
  employee_list={}
  name=[]
  domain=[]
  empid=[]
  email=[]
num_of_employees=int(input("Enter a employees :"))
for i in range(num_of_employees):
    name=input("enter a name:")
    domain=input("enter a domain:")
    empid=input("enter a empid:")
    email=("enter a email:")
    num_of_employees={"name":name,"domain":domain,"empid":empid,"email":email}
    if name=="rushi":
        rushi.append(num_of_employees)
        num_of_employees["reddy"]=rushi
    elif name=="vani":
        vani.append(num_of_employees)
        num_of_employees["vani"]=vani
    elif name=="venu": 
        venu.append(num_of_employees)
        num_of_employees["venu"]=venu  
    elif name=="raju": 
        raju.append(num_of_employees)
        num_of_employees["raju"]=raju
print(num_of_employees)
name=input("enter a name:")
domain=input("enter a domain:")
empid=input("enter a empid:")
email=("enter a email:")  
for i in num_of_employees[add_employees]:
  print(add_employees)
