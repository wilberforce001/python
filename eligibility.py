age = 22
message = "Eligible" if age >=18 else "Not eligible"
print (message)

high_income = False
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")

#In python logical operators are short-circuit. Meaning that when python interpreter wants to evaluate an expression it starts with the first argument and checks for one hat is true.#

#Chaining Comparison Operators 
# age should be between 18 and 65
age = 17
if 18 <= age < 65:
    print("Eligible")
else:
    print("Not eligible") 

# Quiz
if 10 == "10":
    print ("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")