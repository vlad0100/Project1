
#print(boolean + var)
#print(boolean - var)
#print(boolean * var)
#print(boolean / var)
#print('  ')
#print(4/2)
#print(4/3)
#value_int = int(input("Enter a int"))   #int
#value_float = float(input("Enter a float"))#float
# = input("Enter a int")   #string
#value_boolean = bool(input("Enter a boolean"))  #boolean
#(value_int)
#print(value_float)
#print(value_string)
#print(value_boolean)

#major = 18
#var_input = int(input("Enter a number"))

#if major < var_input : #True #Condition 1
    #print(">") ##True
#elif major == var_input:
    #print("=")
#else: #Else
    #print("<")

#var1 = "2"
#var_input = (input("Cat este 1+1?"))

#if var_input == var1:
   # print("corect")
#else:
   # print("gresit.")

#for count in range(1, 10):
    #print(count)

#var = 1
#while var < 100:
    #print(var) #99
    #var = var + 10 #99 + 1 != 100

import random
var_check = random.randint(0, 25)
var_in = int(input("Enter a number"))

while var_in != var_check:
    if var_in < var_check:
        print("Less than need")
    else:
        print("More than need")
    var_in = int(input("Enter a number"))
else:
    print("Congratulations!")