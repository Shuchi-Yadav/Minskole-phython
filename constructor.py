#class Person:
    #def __init__(self,fn,ln,age):
        #self.firstName = fn,
        #self.lastName = ln,
        #self.age = age

    #def displayName(self):
       # print(self.firstName + self.lastName)  

#amol = Person("amol", "rao",25)
#print(amol.firstName)
#print(amol.lastName)
#print(amol.age)
#amol.displayName()
class Person:
    # class variable
    country = "IND"
    #constructor to initialise instance variable
    def __init__(self, fn,ln,age,salary):
        #self.fistname is instance variable 
        self.firstName = fn 
        self.lastName = ln
        self.age = age 
        self.salary = salary

    # instance method
        #self refers to the calling object
    def displayName(self): #instance method
        print(self.firstName + self.lastName)
    
    # instance method
    def udapateAge(self,ag):
        self.age = ag

    #
    def updateSalary(self,sl):
        self.salary = sl

radha = Person("radha","deshmukh",23,300000)
sanjay = Person("sanjay","deshpande",24,300000)

#radha.udapateAge() # call instance method

print(radha.country)
print(sanjay.country)

radha.country = "BHA"

print(radha.country)
print(sanjay.country)