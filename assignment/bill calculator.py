class calculator:
    def __init__(self):
        pass
    def add(self,a,b):
        return a+b
    def subtract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        if b==0:
            return ("cannot divide by zero.")
        return a/b
calculator=calculator()
result=calculator.add(12,4)
print("12+4=",result)
result=calculator.subtract(20,4)
print("20-4=",result)
result=calculator.multiply(17,3)
print("17*3=",result)
result=calculator.divide(23,4)
print("23/4=",result)