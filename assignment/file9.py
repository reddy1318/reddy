# def add_employees():
#     java=[]
#     python=[]
#     sap=[]
#     n=int(input("Enter the num_of_employees"))
#     for i in range(n):
#         name=input("Enter the name:")
#         empid=input("Enter the empid:")
#         domain=input("Enter the domain:")
#         email=input("Enter the email:")
#         employee={"name":name,"emplid":empid,"email":email}
#         if domain=="java":   
#             java.append=(employee)
#         elif domain=="python":
#             python.append(employee)
#         elif domain=="sap":
#             sap.append(employee)
#         else:
#             print("invalid domain")
#     print("java employee:")
#     for emp in java:
#         print(emp)
#     print("python employee:")
#     for emp in python:
#         print(emp)
#     print("sap:") 
#     for emp in sap:
#         print(emp)
# add_employees()


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

        employee = {"name": name, "empid": empid, "email": email}
        
        if domain == "java":
            java.append(employee)
        elif domain == "python":
            python.append(employee)
        elif domain == "sap":
            sap.append(employee)
        else:
            print("Invalid domain. Skipping employee.")

    print("\nJava Employees:")
    for emp in java:
        print(emp)
    
    print("\nPython Employees:")
    for emp in python:
        print(emp)
    
    print("\nSAP Employees:")
    for emp in sap:
        print(emp)

add_employees()


