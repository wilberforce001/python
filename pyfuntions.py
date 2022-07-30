def my_funtion ():
    print("Hello from a function")
my_funtion ()

def my_function (fname):
    print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function(fname, lname):
    print(fname + "" + lname)
my_function("Emil", " Refsnes")

#If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("Tobias", "Emil", "Linus")

def my_function(child3, child2, child1):
    print("The youngest child is " +child3)
my_function(child1 = "Emil", child2 = "Tobias", child3= "Linus")
def my_function(**kid):
    print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

#Default Parameter Value
def my_function(country = "Norway"):
    print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Passing a List as an Argument
def my_function(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

#Return Values
def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

#The Pass Statement
def myfunction():
    pass

#Rescursion
def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result 
print("\n\nRecursion Example Results")
tri_recursion(6)

def greet():
    print("Hi there")
    print("welcome aboard")


greet()

#parameter is the input you define for your function while an argument is the actual value for a given parameter

def increment(number, by=1):
    return number + by

print(increment(2, 5))

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total
        

#We use square brackets to create list of objects and parenthesis to create tuples(similar to a list of objects and are iterable) 
print(multiply(3, 8, 4, 5))

def save_user(**user):
    print(user["age"])

save_user(id=1, name="John", age=22)

#Scope - region of the code where a variable is defined

# without a function
print("Happy birthday to you!" )
print("Happy birthday to you!" )
print("Happy birthday, dear Fred...")
print("Happy birthday to you!")

# With a function
def happy():
    print("Happy birthday to you!")

def singFred():
    happy()
    happy()
    print("Happy birthday, dear Fred...")
    happy()

singFred()

# Defining the name as an argument(arg)
def sing(person):
    happy()
    happy()
    print("Happy birthday, dear " + person + "...")
    happy()

sing("Fred")
sing("Jane")


#Get user input
name = input("What is your name: ")
sing(name) # Once

# In a loop
for i in range(3): # 3 times
    sing(name)
    print("\n")




