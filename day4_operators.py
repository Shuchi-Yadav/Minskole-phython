
# comparison 
# < , > , <= , >= , == , != 

print(4 < 5)
print(4 > 3)
print(4 >= 3)
print(4 != 3)
print(4 == 3)

# logical operator 

# and 
#True  and True   =====> True
#False and True   =====> False
#True  and False  =====> False
#False and False  =====> False

print(22 == 22 and 33 == 33) # T T
print(22 != 22 and 33 == 33)# F T
print(22 == 22 and 33 != 33)# T F 
print(22 != 22 and 33 != 33) # F F

# or 

#True  or True   =====> True
#False or True   =====> True
#True  or False  =====> True
#False or False  =====> False

print(22 == 22 or 33 == 33) # T T 
print(22 != 22 or 33 == 33) #F T
print(22 == 22 or 33 != 33) # T F 
print(22 != 22 or 33 != 33) # F F 

# not
#not True --- False
#not False -- True


print(not(22 == 22 or 33 == 33)) # T T