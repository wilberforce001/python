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

