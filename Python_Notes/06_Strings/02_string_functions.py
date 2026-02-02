# Strings are immutable that means they do not change the existing string they return a new string to the user

story = "once there was a farmer who was sowing hemp seeds in a field. The farmer was an honest man"

# STRING FUNCTIONS
print(len(story))  # 90
# returns the length of the string i.e number of characters in the string.

# ENDSWITH FUNCTION
print(story.endswith("field"))  # False
print(story.endswith("man"))    # True
# returns true if sentence ends with the word written in ().
# else returns false if the given word doesn't match the word in the string.
# we can also check for a value-in-between the string by providing the start and end index positions. Eg:-
str2 = "Welcome to the Console!!!"
print(str2.endswith("to",4,10))  # True

# COUNT FUNCTION
print(story.count("a"))  # 9
print(story.count("farmer"))  # 2
# counts the total occurence of a particular character in a string here 'a'appears 9 times in the given sentence or given string. 
# it also tells about the occurance of a word.

# CAPITALIZE FUNCTION
print(story.capitalize())  # Once there was a farmer who was sowing hemp seeds in a field. the farmer was an honest man
# it converts the first character in the string in capital form.
''' The capitalize() method turns only the first character of the string to uppercase and the rest other 
characters of the string are turned to lowercase.'''
# Eg:-
blogHeading = "introduction tO JS"
print(blogHeading.capitalize())  # Introduction to js

# FIND FUNCTION
print(story.find("farmer"))  # 17
# finds a word in the given string. returns the index of the character.
# if a word comes twice in the string then it tells the index of word that comes first in the string
print(story.find("they"))  # -1
# if the given word is not present in the string then it returns -1. for this see the above example

# REPLACE FUNCTION
print(story.replace("farmer","goldsmith"))  # once there was a goldsmith who was sowing hemp seeds in a field. The goldsmith was an honest man
# it replaces the existing word with the new word in the entire string

# UPPER FUNCTION
print(story.upper())  # ONCE THERE WAS A FARMER WHO WAS SOWING HEMP SEEDS IN A FIELD. THE FARMER WAS AN HONEST MAN
# upper function capitalize the entire sentence to upper case

friends = "HELLO, MY NAME IS ABC AND I HAVE MANY FRIENDS."
# LOWER FUNCTION
print(friends.lower())  # hello, my name is abc and i have many friends.
# it converts upper case to lower case for a full senctence or word

greeting = "Hey there!!!"
# RSTRIP FUNCTION
print(greeting.rstrip("!"))  # Hey there
# 1. it removes the trailing characters.
# 2. it only removes the trailing characters i.e characters that come after the word not before.Eg:
greeting1 = "!!! Hey there !!!"
print(greeting1.rstrip("!"))  # !!! Hey there

# SPLIT FUNCTION
friends1 = "hello, my name is abc and i have many friends"
print(friends1.split(" "))  # ['hello,', 'my', 'name', 'is', 'abc', 'and', 'i', 'have', 'many', 'friends']
# split() function splits the given string at the specified instance and returns the separated strings as list items
# Eg 2:-
friends2 = "hello,my,name,is,abc,and,i,have,many,friends," 
print(friends2.split(","))  # ['hello,', 'my', 'name', 'is', 'abc', 'and', 'i', 'have', 'many', 'friends','']

# CENTRE FUNCTION
str1 = "Welcome to the Console!!!"
print(str1.center(50))
print(len(str1))  # 25
print(len(str1.center(50)))  # 50
# the centre() method aligns the string to the centre as per the parameters given by the user.

# ISTITLE FUNCTION
''' The istitle() returns True only if the first letter of each word of the string is capitalized, else it returns False'''
# Eg 1:-
str2 = "World Health Organization"
print(str2.istitle())  # True
# Eg 2:-
str2 = "To kill a Mocking bird"
print(str2.istitle())  # False

# SWAPCASE FUNCTION
''' The swapcase() method changes the character casing of the string. Uppercase are converted to lowercase and
lowercase are converted to uppercase.'''
str3 = "Python is a Interpreted Language"
print(str3.swapcase())  # pYTHON IS A iNTERPRETED lANGUAGE

# TITLE FUNCTION
# The title() method capitalizes each letter of the word within the string
str4 = "His name is Dan. Dan is a honest man"
print(str4.title())  # His Name Is Dan. Dan Is A Honest Man

# JOIN FUNCTION
''' join() function joins the string with the given string'''
str5 = " ".join(["apple", "banana", "orange"])
print(str5)  # apple banana orange


