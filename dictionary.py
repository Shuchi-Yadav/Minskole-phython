student = {
    "first_name" : "Shuchi",
    "lasr_name" : "Yadav",
    "age" : 40,
    "roll_no" : 47
}

#retrieve

print(student["first_name"])

#update

student["first_name"] = "shivani"
print(student)

#add

student["city"]="pune"
print(student)

#delete

student.pop("city")
print(student)

student.popitem()
print(student)

info = {
     "first_name" : "Shuchi",
    "lasr_name" : "Yadav",
    "age" : 40,
    "roll_no" : 47
}

#get()

#q11 = info["Age"]
#print(q11)

q1 = info.get('Age')
print(q1)
print('hello')

#loop

vehicle = {
    "color" : "red",
    "type" : "sedane",
    "regNo" : 123
}

print(vehicle['color'])

for item in vehicle:
    print(item, vehicle[item])

for x in vehicle.keys():
    print(x)

for y in vehicle.values():
    print(y)

for k,v in vehicle.items():
    print(k, v)    


e = dict.fromkeys(["amol", "chinmay", "rose"])    
print(e)

info3 = {
    "admin": "chinmay",
    "customer" : "ssmeee",
    "support" : "raj"
}

info3.setdefault('manager', 'kalpana')
print(info3)