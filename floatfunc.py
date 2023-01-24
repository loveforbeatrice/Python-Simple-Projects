#lfb
#ax + b = c

start_message = """

welcome the linear eqation solving program
Please type the values for

ax + b = c"""

print(start_message)
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

x = (c-b)/a
print("the value of x is: ", x)

