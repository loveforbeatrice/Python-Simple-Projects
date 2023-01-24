#lfb 113 HW 1.2

#modules
import re

#####################

text = input("Please write your text: ")
char = input("which character do you search? ")
matches = re.findall(char,text )
num = len(matches)
print("We have found","'"+str(num)+"'", "special characters","'"+char+"'" )
