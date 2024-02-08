#slicing with jump/step values
#syntax
#variable[start:stop:step] n-1 will be considered

phrase = "the sun is bright and lovely"
print(phrase[0:20])
print(phrase[0:20:2])
print(len(phrase))

print(phrase[:33:3])

#negative indexing
# to print the last element
# to reverse the sttring    

v1 = "Python 3.1"
v2 = "Python 3.2"

print(v1[-1])
print(v2[-1])

#palindrome

name = "NAMAN"
name2 = "RAKESH"

print(name[::-1])
print(name2[::-1])

# use case for slicing witth skip values

numbers = "123456789"
print(numbers[::2]) #odd numbers
print(numbers[1::2]) #even numbers


sentence = " My email ID is nikhil.pune@yahoo.com $"
print(sentence[0])
print(sentence[27])
print(sentence[28:34])
print(sentence[0:39:4])
print(sentence[::-1])
print(len(sentence))

