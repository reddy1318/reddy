class Calculator:
    def __init__(self):
        pass
    def add(self,a,b):
        return a+b
    def subtract(self,a,b):
        return a-b
    def multiplication (self,a,b):
        return a*b
    def devide(self,a,b):
        if b==0:
            return "cannot devide by zero"
        return a/b
Calculator=Calculator()
result=Calculator.add(12,3)
print("12+3=",result)
result=Calculator.subtract(50,30)
print("50-30=",result)
result=Calculator.multiplication(12,4)
print("12*4=",result)
result=Calculator.devide(23,7)
print("12/7=",result)