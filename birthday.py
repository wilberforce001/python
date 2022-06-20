people = [{'name': 'John', 'age':25}, {'name': 'Sarah', 'age':23}, {'name': 'Lisa', 'age':101}]
for person in people:
    name = person['name']
    age = person['age']
    if str(age)[-1]=='1': #convert integer to string, get the last character from the string
        Variable_text = 'st'
    elif str(age)[-1]=='2':
        Variable_text = 'nd'
    elif str(age)[-1]=='3':
        Variable_text = 'rd'
    else:
        Variable_text = 'th'
    
    message = 'Hello ' + name + ', happy ' + str(age) + Variable_text + ' birthday!'
    print(message)
#Prints out 
#Hello John, happy 25th birthday!
#Hello Sarah, happy 23rd birthday!
#Hello Lisa, happy 101st birthday!
    
