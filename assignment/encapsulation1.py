class Employee:
    def __init__(self,name,age,salary,id,project):
        self.name=name
        self.age=age
        self.salary=salary
        self.id=id
        self.project=project
    def show(self):
        print("name:",self.name,'age:',self.age,'salary:',self.salary,"id:",self.id)
    def work(self):
        print(self.name,'is working on',self.project)
emp=Employee('reddy',22,15000,12,'banking website')
emp.show()
emp.work()
