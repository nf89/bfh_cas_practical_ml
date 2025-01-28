# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 16:10:45 2021

@author: I0325971
"""

#SIB course - 01 Python basics

#theory
# boolean (resulting from comparisons) can be combined using 'and' or 'or'
a = 5
print("'and' requires both elements to be True:", True and (1 + 1 != 2 ))
print("'or' requires at least element to be True:", (a * 2 > 10) or (a > 0))

#strings
#Triple quotes can be used to define multi-line strings.
long_string = """Let me tell you something, my lad. 
When you’re walking home tonight and some great 
homicidal maniac comes after you with a bunch 
of loganberries, don’t come crying to me!\n"""
print(long_string)

#We also commonly use special characters, such as:
print('a\tb')  # \t : tabulation
print('a\nb')  # \n : newline

#lists and tuples
#Lists are declared by surrounding a comma separated list of objects with [].
#Tuples are declared similarly, but using ().
myList = [1, 2, 3, 5, 5.2, 6.99]
myTuple = ('a', 4.2, 5) # a list/tuple is not limited to a single type

#A tuple is immutable : its length is fixed and its elements cannot be changed.
#By comparison, a list is mutable : it can be extended, reduced, and its elements can be changed.

#Changing an element in a list or tuple
myList[3] = "Spam"
print(myList[3])

myTuple[3] = "Spam" #error

#create a list that contains each word of the string, then join it again to a string
myString = "Drop your panties Sir William, I cannot wait till lunchtime."
myWords = myString.split()
print(myWords)
myString_new = " ".join(myWords) 
print(myString_new)


#Dictionnaries
#Dictionnaries, or dict, are containers that associate a key to a value, just like a real world dictionnary associates a word to its definition.
    #Dictionaries are instantiated with the {key:value} or dict() syntax.
    #keys must be unique in the dictionnary.
    #values can appear as many time as desired in the dictionnary.
    #the [] operator is used to select objects from the dictionnary, but using their key instead of their index.
    #Unlike Lists or Tuples, Dict are unordered collections: they do not record element position or order of insertion. Therefore values cannot be retrieved by index position.
    
student_age = dict()                          # this is one way to initiate a dictionnary
student_age = { 'Anne' : 26 , 'Viktor' : 31 } # this is another way to initiate a dictionnary, directly with data in

# Adding key:value pairs to an existing dictionary is as easy as:
student_age['Eleonore'] = 5
print('dictionnary:', student_age)

# Modifying the value associated to a key is equally easy:
student_age['Eleonore'] = 25
print('dictionnary:',student_age)

# We are not restricted to a particular type for keys, nor for values. We can e.g. make dict of lists or dict of dict.
student_age[0] = 'zero' 
student_age['group_1'] = [23, 25, 28] 
student_age['group_2'] = {'bob':26, 'alice':27}
print('dictionnary:',student_age)

# Removing objects from the dictionnary is done with the pop() method, look at the help for more details.
student_age.pop('Anne') 
print('dictionnary:',student_age)