# function 

# int as parameter and int as return

def add(x,y):
    return x + y
e = add(12,45)
print(type(e))

# float as parameter and float as return

def add(k,l):
    return k + l
f = add(45.6,45.8)
print(type(f))

# string as parameter and string as return type 
def greet(word):
    return "hello " + word
q = greet('Nathan')
print(type(q))

# list as parameter and list as return type 
cities = ["pune","mumbai","nagpur"]

def addCity(lst):
    cities.append('wardha')
    return lst
h = addCity(cities)
print(h)

# dict as paramerter and dict as return type

info = {
    "firstName":"chinmay",
    "lastName":"deshpande"
}

def addLang(dictA):
    dictA['language']='hindi'
    return dictA
d = addLang(info)
print(d)

# tuple as parameter and tuple as return type 

a1 = 12,13
a1 = (12,13)

def addElementToTuple(tupA):
    tupA = list(tupA) #covert into list
    print(tupA)
    tupA.append(45)
    print(tupA)
    tupA = tuple(tupA)
    return tupA
l = addElementToTuple(a1)
print(type(l))


# set as a parameter and set as return type

setA = {11,22,33}
def addEtoS(x):
    setA.add(x)
    return(setA)
C = addEtoS(34)
print(C)

#lambda

def add(x,y):
    return x+y
a= add(4,5)
print(a)


addB = lambda x,y:x+y
e2 = addB(34,5)
print(e2)  #39

e = lambda x:x*x
e3 = e(3)
print(e3) #9

names = ["amit", "amol", "anand", "akshay"]
def changeName(lst):
    lst[0] = "arjun"
    return lst
e4 = changeName(names)
print(e4) #['arjun', 'amol', 'anand', 'akshay']
print(names)  #['arjun', 'amol', 'anand', 'akshay']


lstA = [1,2,3,4,5]
n = []
for i in lstA:
    n.append(i*5)
print(n) #[5, 10, 15, 20, 25]

# list comprehension -- o/p - list
#[expression:loop:condition]

e4 = [i*5 for i in lstA]
print(e4) #[5, 10, 15, 20, 25]

listB = [1,2,3,4,5,6,7,8,9,10]
e5 = [i*i for i in listB]
print(e5) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

lstC = [44,55,66,77,33,44,55,66,77,11,22,33,7,8,9]
listD = []
for x in lstC:
    if x % 2 == 0:
        listD.append(x)
print(listD) #[44, 66, 44, 66, 22, 8]

#[expression:loop:condition]
e6 =  [x for x in lstC if x % 2 == 0]
print(e6)

#table of 2

x = [1,2,3,4,5,6,7,8,9,10]
w = [i*2 for i in x]
print(w)

#  even no 

x = [1,2,3,4,5,6,7,8,9,10]
w1 = [i for i in x if i % 2 == 0 ]
print(w1)

# odd no

w2 = [i for i in x if i % 2 != 0]
print(w2)

# make every character to upper()
names = ["chinmay","sarika","poorva","tanmay"]
w3 = [i.upper() for i in names]
print(w3)#['CHINMAY', 'SARIKA', 'POORVA', 'TANMAY']

names = ["chinmay","sarika","poorva","tanmay"]
w4 = [i.upper() for i in names if i.endswith('y')]
print(w4) #['CHINMAY', 'TANMAY']

names = ["chinmay","sarika","poorva","tanmay"]
x5 = [i[0] for i in names]
print(x5)#['c', 's', 'p', 't']

x6 = [
    {
        "firstName":"chinmay",
        "lastName":"deshpande",
        "age":19,
        "vehicle":True
    },
    {
        "firstName":"sarika",
        "lastName":"pansare",
        "age":4,
        "vehicle":True
    },
    {
        "firstName":"pranali",
        "lastName":"pansare",
        "age":19,
        "vehicle":False

    },

    {
        "firstName":"tavish",
        "lastName":"anade"
    }

]

x7 = [x['firstName'] for x in x6]
print(x7)#['chinmay', 'sarika', 'pranali', 'tavish']


x8 = [11,22,33,44]
#[odd,even,odd,even]

#       ternary operator

x10 = ["even" if x%2 == 0 else "odd" for x in x8]
print(x10)#['odd', 'even', 'odd', 'even']

# students 
students  = [
    {
        "firstName":"chinmay",
        "lastName":"deshpande",
        "age":19,
        "vehicle":True
    },
    {
        "firstName":"sarika",
        "lastName":"pansare",
        "age":4,
        "vehicle":True
    },
    {
        "firstName":"pranali",
        "lastName":"pansare",
        "age":19,
        "vehicle":False

    },

    {
        "firstName":"tavish",
        "lastName":"anade",
        "age":39,
        "vehicle":True
    }

]

q3 = [i['firstName'] for i in students if i['age'] >= 18 and i['vehicle']== True]
print(q3)#['chinmay', 'tavish']

q4 = [ x['firstName'] if x['age'] > 18 and x['vehicle'] else None for x in students]
print(q4) #['chinmay', None, None, 'tavish']


q4 = [x for x in q4 if x != None]
print(q4)#['chinmay', 'tavish']

q5 = [ x['firstName'] if x['age'] > 18 else "cannotdrive" for x in students]
print(q4)


def addA(x,y):
    return x + y
e = addA(25,4)
print(e)

def addition(fn,x,y):
    e = fn(x,y)
    return e
print(e)
add = lambda x,y:x+y
result = addition(add, 3,4)
print(result)

# program 2
# function as a parameter to another function

sub = lambda x,y:x-y

def substraction(fn,a,b):
    # fn =  lambda x,y:x-y
    # a = 12
    # b = 4
    e = fn(a,b) # 8
    return e # 8
result2 = substraction(sub,12,4)
print(result2)

# x = 10 
# print(x)
# print(sub) # function 
# sub(23,3) #  function call

# program 3
# function as a return type 
def multiplication():
    return lambda x,y:x*y

result3 = multiplication()
#result3 = lambda x,y:x*y
e2 = result3(34,5)
print(e2)


    