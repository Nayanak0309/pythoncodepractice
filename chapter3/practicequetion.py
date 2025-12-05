#write a python program to display a user entered name followed by good afternoon using input() function
"""name = input("enter the name")
print(f"good afternoon {name}")"""#we can use the f string

#problem2
"""letter = ''' Dear <|Name|>,
             You are selelcted!
             <|Date|>'''
print(letter.replace("<|Name|>","nayana").replace("<|Date|>","02/04/2003"))"""

#write the pg to detect double space in a string
"""name = "enter   the  name  of the boy"
print(name.find("  "))"""#it will find the double space in the sentence by index
 
#replace the double space into single space
'''name = "enter  the  name  of the boy"
print(name.replace("  "," "))'''#it will replace the into single space

#write the pg to format a following using escape sequence
print("Letter  \n\"Dear Nayana, \n\tthis python course is nice. \nThankyou!\"")