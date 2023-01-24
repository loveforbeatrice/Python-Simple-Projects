# lfb 113 HW
# USERNAME/PASSWORD LOG IN PROGRAM

#modules
import string


#########

rule1 = "Username must begin with letter 'e'\n"
rule2 = "Username must be a minimum of 6 characters and a maximum of 12 characters\n"
rule3 = "Username should not contain any characters other than alphanumeric characters\n"
rule4 = "Password must be at least 8 characters\n"
rules = rule1+rule2+rule3+rule4

print(rules)
#############################################################################################
control = 1

while control == 1:
    username = input("Write your username: ")
    
    alphanumeric_condition = username.isalnum() == False
    
    first_letter_condition = username[0] != "e"
    length_condition = len(username)>12 or len(username)<6
      
    if first_letter_condition:
        print("Username must begin with letter 'e'")
    
    elif alphanumeric_condition:
        print("Username can include only alphanumeric characters")
    
    elif length_condition:
        print("Please enter a Username in allowed length")
    
    else:
        print("Your username is VALID" )
        break



