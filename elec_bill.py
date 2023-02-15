# electricity bill
unit = int(input("Enter the number of units: \n"))
first_hun_units = 0
next_hun_units = 0
after_two_hun = 0
excess = 0
if unit <= 100:
    total = first_hun_units + next_hun_units + after_two_hun

elif unit <= 200:
    excess = unit - 100
    next_hun_units = excess * 5
    total = first_hun_units + next_hun_units + after_two_hun

elif unit > 200:
    excess = unit - 200
    after_two_hun = 500 + (excess * 10)
    total = first_hun_units + next_hun_units + after_two_hun
else:
    print("Input a valid number.")
print("Total billed amount is " + str(total))
