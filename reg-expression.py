import re

#program 1 search

#/w - A-Z , a-z , 0-9# program 2 # findall


str = 'cat main sun mpo run mat mm9 sun'
e = re.search(r'm\w\w',str)
f= re.search(r'\wun', str)
print(e)
print(f)


#e # None---- python ---- false value
if e:
    print(e.group())
else:
    print("match not found !")


if f:
    print(f.group())
else:
    print("match not found")

# program 2 # findall
strB  = "man sun mop run mat fat cat sat"
q = re.search(r'\w\wt',strB)
print(q)

q2 = re.findall(r'm\w\w',strB)
q3 = re.findall(r'\wat',strB)

print(q2)
#['man', 'mop', 'mat']
print(q3)
#['mat', 'fat', 'cat', 'sat']

# program 3 match
# match
strC = "mon tue wed thu fri sat"
q4 = re.match(r'm\w\w',strC)
print(q4)
if q4:
    print(q4.group())
else:
    print("match not found")

# program 4 split
#\w - [A-Z a-z 0-9]
#\W - non alphanumreic    
strD = "This; is the 'core' python's book"   
q5 = re.split(r'\W+',strD)
print(q5)

info = 'chinmay:7709192441'
print(re.split(r'\W+',info))


#program 5 sub

strE = "I am learning javascript"
q6 = re.sub(r'javascript','python',strE)
print(q6)


# [A-Z , a-z , 0-9] // alphanumric  // " ", %%%
# [/W] --- " " and special symbol
# [/w]* zero or more repetitions
# \d  -- represents only digits
# \b -- only blank space

str6 = "an apple a day keeps doctor away"
e2 = re.findall(r'\ba[\w]*',str6)
print(e2)

# program 7
str7 = "The meeting will be conducted on 1st and 21st of each month"
e3 = re.findall(r'\d[\w]*',str7)
print(e3)

# program 8
str8 = "one two three four five six seven 8 9 10"
e4 = re.findall(r'\b\w\w\w\w\w',str8)
print(e4)

# program 9
str9 = "one two three four five six seven nineteen 8 9 10"
e5 = re.findall(r'\b\w{4,}',str9)
print(e5)


#program 11

str6 = "one two three four five six seven nineteen 8 9 10"

e6 = re.findall(r'\b\d{1,}\b', str6)
e7 = re.findall(r'\b\d+\b', str6)

print(e6)
print(e7)

#program12
# a regular expression to find last word starting with 's'
# a regular expression to find last word starting with 'o'

str6 = "o one two three four five six seven seventeen two"
# '\Z' 0 end of string
# '\A' start of string

e8 = re.findall(r'\bs[\w]*\Z',str6)
e9 = re.findall(r'\A\bo[\w]*',str6)

print(e8)
print(e9)


#program 1

str = "chinmay deshpande:7709192441"
print(str)
e = re.search(r'\d+', str)
print(e.group())

#  '\w'  --> [A-Z a-z  0-9]
#   '\W' --> Non alphanumeric
#   '\d' --> digit 
#   '\D' --> non-digit

h = re.search(r'\D+',str)
print(h.group())

i = re.search(r'[\w]* [\w]*', str)
if i:
    print(i.group())
else:
    print("pattern not match")    


# program 2
str1 = "anil akhil ajay arun arti ankur arundhati abhijeet"    
g = re.findall(r'\ba[nkr][\w]*',str1)
print(g) #['anil', 'akhil', 'arun', 'arti', 'ankur', 'arundhati']


# program 3
str2 = 'chinmay 07-11-1989 amol 19-09-1990 mayuri 21-01-1989'
j = re.findall(r'\d{2}-\d{2}-\d{4}', str2)
print(j) #['07-11-1989', '19-09-1990', '21-01-1989']


# program 4
str3 = 'chinmay 7-11-1989 amol 19-09-1990 mayuri 21-01-1989'
i = re.findall(r'\d{1,2}-\d{2}-\d{4}', str3)
print(i) #['7-11-1989', '19-09-1990', '21-01-1989']

# program 5
str4  = "hello world"
k = re.search(r'^he',str4)
print(k.group()) #he

# program 6
str  = "hello world"
g = re.search(r'world$',str)
print(g.group()) #world

#program 7
str  = "hello World"
g = re.search(r'world$',str,re.IGNORECASE)
print(g.group()) #World

# program 8 
students = "I got 80 marks I got 100 marks"
print(re.findall(r'\d{2,3}',students)) #['80', '100']

students = "Amol got 80 marks Mayuri got 100 marks"
f = re.findall(r'[A-Z][a-z]*',students)
print(f) #['Amol', 'Mayuri']

#program 9

str = 'The morning meeting will be scheduled at 8am or 9am , evening at 8pm or 9pm'
k = re.findall(r'\d[\w]*',str)
print(k)
#[8am,9am,8pm,9pm]