# program 1
# x , y   ---- formal arguments 
# 12, 13  ---- actual arguments 

def add(x,y):
    return x + y
el = add(12,4)
print(el)
    
# program 2 "positional argument"

def subA(x,y):
    return x - y
e2 = subA(y=23, x =45)    
print(e2)

# program 3 "default arguments"

def mulA(x=6, y=8):
    return x * y
e3 = mulA()
e4 = mulA(24,2)
print(e3)
print(e4)

# program 4 - variable length arguments

def addAll(*args):
    print(args)
    total = 0
    for i in args:
        total = total + i
    return total    

e5 = addAll(1,2,3,4,5,6,73,4,5,6,6,55,6,7,3,4,5,6,7)
print(e5)

# program 5 

def greet(*args):
    for i in args:
        print("welcome " + i)
greet("vanshika", "nathan", "divya", "inaya")       

# program 6
# g = 10
# h = 12.4
# j = True
# l = [11,22,33]
# f = 12,4
# r = {
#     "firstName":"chinmay"
# }
# g = {1,2,3,4}
# h = "chinmay"

def printInfo(**kwargs):
    print(kwargs)
    for i in kwargs:
        print(i,kwargs[i])

printInfo(first_name = "chinmay",lastName = "deshpande",age = 34 , city = "pune")    

# default arguments

def addA(x =7, y =8):
    print(x+ y)
addA()
addA(7,6)

# positional arguments 

def addC(x,y):
    print(x+y)
c = addC(12,3)
print(c)

def addD(x,y):
    return x + y
d = addD(3,5)
print(d)

def sub(x,y):
    return x - y
f = sub(56,3)
print(f)

def sub(x,y):
    print(x-y)
sub(x=6, y=4)

def addD(*args):
    print(args)
    total = 0
    for x in args:
        total = total + x
    return total
e3 = addD(1,2,33,4,55,6,7,88,9,55,66,77,8,99,44,55)
print(e3)


def addinfo(**kwargs):
    print(kwargs)
    kwargs['city']="pune"
    return kwargs
e4 = addinfo(first_name = "shivani",last_name ="hedau",age= 30)
print(e4)
#{'first_name': 'shivani', 'last_name': 'hedau', 'age': 30}
#{'first_name': 'shivani', 'last_name': 'hedau', 'age': 30, 'city': 'pune'}


def myfunction():
    a = 1
    b = 2
    a = a + 1
    print(a)
    print(b)
    myfunction()   
    print(a)

    a = 1 #global
    def myfunction2():
        b = 5
        a = 6 #local
        a = a + 1
        print(a) # 7
        print(b) # 5

    myfunction2()
    print(a) # 1

    a = 10 # global
    def myfunction3():
        print(a) #global
        print(10)
    myfunction3()
    print(a) # global

    # program 9
h = 10  # global varibale
def myfunction4():
    global h
    h =99 # global variable
    print(h)
    myfunction4()
    print(h)

