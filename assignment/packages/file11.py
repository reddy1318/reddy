#1.write a program to create a calculator using function (sum,sub,mul,div)variable length arguments
def sum1(*num):
    sum=0
    for x in num:
        sum=sum+x
        print("The sum is:",sum)
if  __name__=="__main__":
    sum1(10)
sum1(10,20)
sum1(10,20,30)  
print()


def sub1(*num):
    sub=1
    for x in num:
        sub=sub-x
        print("The sub is:",sub)
if  __name__=="__main__":
    sub1(10)
sub1(12,7)
sub1(10,4,2)  
print()


def mul1(*num):
    mul=3
    for x in num:
        mul=mul*x
        print("The mul is:",mul)
if  __name__=="__main__":
    sum1(10)
sum1(10,20)
sum1(10,20,30)  
print()


def div1(*num):
    div=4
    for x in num:
        div=div/x
        print("The div is:",div)
if  __name__=="__main__":
    div1(10)
div1(1,22)
div1(10,2,4)  
print()



#2.wite a program to enter employee details and also filter the stored employee details with name and empid and designation and email
def add_employees():
    java = []
    python = []
    sap = []
    n = int(input("Enter the number of employees: "))
    for i in range(n):
        name = input("Enter the name: ")
        empid = input("Enter the empid: ")
        domain = input("Enter the domain: ")
        email = input("Enter the email: ")
        employee = {"name": name,"empid": empid,"domain":domain,"email": email} 
        if domain == "java":
            java.append(employee)
        elif domain == "python":
            python.append(employee)
        elif domain == "sap":
            sap.append(employee)
        else:
            print("Invalid domain.")
    return java,python,sap
def filter_employees(employees,key,value):
    filtered_employees=[emp for emp in employees if emp.get(key)==value]
    return filtered_employees
java_employees, python_employees, sap_employees = add_employees()
name_filter = input("Enter the name to filter: ")
filtered_by_name = filter_employees(java_employees + python_employees + sap_employees, "name", name_filter)
print("Employees filtered by name:", filtered_by_name)

empid_filter = input("Enter the empid to filter: ")
filtered_by_empid = filter_employees(java_employees + python_employees + sap_employees, "empid", empid_filter)
print("Employees filtered by empid:", filtered_by_empid)

domain_filter = input("Enter the domain to filter (java, python, sap): ")
if domain_filter == "java":
    filtered_by_domain = java_employees
elif domain_filter == "python":
    filtered_by_domain = python_employees
elif domain_filter == "sap":
    filtered_by_domain = sap_employees
else:
    filtered_by_domain = []

print("Employees filtered by domain:", filtered_by_domain) 
    
email_filter = input("Enter the email to filter: ")
filtered_by_email= filter_employees(java_employees + python_employees + sap_employees, "email", email_filter)
print("Employees filtered by email:", filtered_by_email)

   