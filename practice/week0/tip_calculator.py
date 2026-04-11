# Ask the user for a bill amoun and a tip percetage.  Print the total amount including tip.
# I know we use float for numbers with decimals.  We also use .02 for2 decimals.  Standard tip amount is 15%.45


print("Choose a version to run: ")
print("1. Bassic tip calculator")
print("2. Tip calculator with user input for tip percentage")
print("3. Cleanerformatted version")

choice = input("Enter 1, 2, or 3: ")

if choice == "1":
     bill = float(input("what is the bill amount? "))
     tip = (bill * 0.15)
     print(f"the total amount including tip is: {bill + tip:.2f}")

elif choice == "2":
    bill = float(input("what is the bill amount? "))
    tip_percent = float(input("What is the percentage you would like to tip? "))
    tip = (bill * (tip_percent / 100))
    print(f"The total amount including tip is: {bill + tip:.2f}")

    
elif choice == "3":
    bill = float(input("What is the bill amount: "))    
    tip = bill * 0.15
    total = bill + tip
    print(f" Bill: {bill:.2f}")
    print(f" Tip: {tip:.2f}")
    print(f" Total: {total:.2f}")