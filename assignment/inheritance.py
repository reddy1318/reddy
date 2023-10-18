#single inheritance
class ATM:
    full_name="Automated Teller Machine"
    website="www.ATM"
    def atm_address(self):
        print("atm_address:Sr nagar hyderabad")
class Atm_process(ATM):
    def __init__(self):
        self.Atm_pin="*************"
        self.Total_balance=100000
    def Atm_details(self):
        print("Atm_pin_",self.Atm_pin)
        print("Total_balance_",self.Total_balance)
        print("full_name_",self.full_name)
        print("website_",self.website)
s=Atm_process()
s.Atm_details()
s.atm_address()

#2
class realme:
    company_name="realme"
    website="www.realme"
    def address(self):
        print("realme India")
class realmeC13(realme):
    def __init__(self):
        self.name="RushiReddy"
        self.year=2007 
    def product_details(self):
        print("name:",self.name)
        print("year:",self.year)
        print("company_name:",self.company_name)
        print("website:",self.website)
s=realmeC13()
s.product_details()
s.address()


#multilevel inheritance
class Grandfather1:
    def __init__(self,grandfathername1):
        self.grandfathername1=grandfathername1
class Father1(Grandfather1):
    def __init__(self,fathername1,grandfathername1):
        self.fathername1=fathername1
        Grandfather1.__init__(self,grandfathername1)
class Son1(Father1):
    def __init__(self,sonname1,fathername1,grandfathername1):
        self.sonname1=sonname1
        Father1.__init__(self,fathername1,grandfathername1) 
    def print_name(self):
        print('Grandfather name is:',self.grandfathername1)
        print("Father name is:",self.fathername1)
        print("Son name is:",self.sonname1)
s1=Son1('reddy','Rushi reddy','vemireddy rushireddy')  
print(s1.grandfathername1)
s1.print_name()        
    
           
#multiple inheritance
class Fruit:
    fruitname=""
    def fruit(self):
        print(self.fruitname)
class Fruittree:
    fruittreename=""
    def fruittree(self):
        print(self.fruittree)
class Fruitetreename(Fruit,Fruittree):
    def Seed(self):
        print("Fruitree name is:",self.fruittreename)
        print("Fruit name is:",self.fruitname)
s1=Fruitetreename()
s1.fruittreename="Mango tree"
s1.fruitname="Apple"
s1.Seed()


#hierarchical inheritance
class SlipersBrands:
    def m1(self):
        print("this is a slipersbrands")
class Slipersname_1(SlipersBrands):
    def m2(self):
        print("this is a slipersname_1 class")
class Slipersname_2(SlipersBrands):
    def m3(self):
        print("this is a slipersname_2 class")
s1=Slipersname_1()
s1.m1()
s1.m2()
s2=Slipersname_2()
s2.m1()
s2.m3()

#hybrid inheritance
class Brand:
    def m1(self):
       print("brand class")
class Amazon(Brand):
    def m2(self):
        print("this is Amazon class")
class Ajio(Amazon,Brand):
    def m3(self):
        print("this is Ajio class")
ajio_instance=Ajio()
ajio_instance.m1()
ajio_instance.m2()
ajio_instance.m3()


