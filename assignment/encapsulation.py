
class student:

    def __init__(self,name,age ,address):
        self.name=name
        self.age=age
        self.address=age
class name(student):
    def student_information(self):
        print("name:",self.name)
class age(student):      
    def student_information(self):
        print("age:",self.age)
class address(student):
    def student_information(self):
        print("address:",self.address)
n=name("RushiReddy",22,"reddypalem")
n.student_information()
a=age("Munish",22,"kota")
a.student_information()
ad=address("Sandeep","nellore",26)
ad.student_information()

