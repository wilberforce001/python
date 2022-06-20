#Check if one is eligble for voting
age = 21

if age < 18:
    print("Not Eligible")
else:
    print("Eligible")

#Loan eligibility
amount = 106000

if amount <= 50000: #No commas in numbers - smallest to largest (<= or <)
    print("Not eligible for a loan")
elif amount <= 100000:
    print ("Eligible for a loan over 100,000")
elif amount <= 500000:
    print ("Eligible for a loan over 500000")
else:
    print("Eligible for a loan over 1 million")