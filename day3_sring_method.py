# String methods
# function are independent
#method are dependent, requires certian variable/object

name = "ANU"
print(name.lower())

#title() 1st Alphabet of every word in upper case
name1 = "SHUCHI"
print(name1.title())

# casefold() 	Converts complete string into lower case
s = "Its A NICE daY TodaY"

print(s.casefold())

# count()	Returns the number of times a specified value occurs in a string

sentence = "My email ID is rutuja.pune@yahoo.com $"

print(sentence.count("."))
print(sentence.count("o"))


# find()	Searches the string for a specified value and returns the position of where it was found
# position of 1st occurence

print(sentence.find("@"))
#print(sentence.find("Z"))

# index()	Searches the string for a specified value and returns the position of where it was found
#  will throw error if the string is not found

print(sentence.index("o"))

#print(sentence.index("Z"))

# replace()	Returns a string where a specified value is replaced with a specified value

sentence1 = " My email ID is nikhil.pune@yahoo.com $"
print(sentence1.replace("email", "mail-box"))

# strip()	Returns a trimmed version of the string
# trailling and following spaces only

print(sentence1)
print(sentence1.strip())

# split()	Splits the string at the specified separator, and returns a list

print(sentence1.split("@"))
print(type(sentence1.split("@")))


num = "022-26876541"
print(num.split("-"))
ans  = num.split("-")
print(ans[0])

# strip remove left and right spaces from sentence like trim in javascript


s = "                      p        r     "
print(s.strip())

song =  '''Jana gana mana adhinayaka jaya he
Bharata bhagya vidhata
Panjaba Sindha Gujarata Maratha
Dravida Utkala Banga
Vindhya Himachala Yamuna Ganga
Uchchhala jaladhi taranga
Tava subha name jage,
tava subhasisa mage,
gahe tava jaya gatha.
Jana gana mangala dayaka jaya he
Bharata bhagya vidhata.
Jaya he, jaya he,
jaya he,
jaya jaya jaya jaya he'''CV

print(song.count("jaya")) #9
print(song.replace("Bharata", "India"))
print(song.find("Bharata"))
print(song.split(" "))