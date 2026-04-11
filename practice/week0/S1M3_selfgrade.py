# ============================================
# S1 M3 — Variables, Types, Input, f-Strings
# Menu-Driven Practice + Self-Grading
# ============================================

def menu():
    print("\n=== S1 M3 Practice Menu ===")
    print("1. Variable Basics (Prediction)")
    print("2. Input + Type Conversion")
    print("3. f-String Assembly")
    print("4. Type Guessing")
    print("5. Convert & Combine")
    print("6. Stretch Challenge")
    print("7. Exit")


# ------------------------------------------------
# Q1: Variable Basics — Predict the Output
# ------------------------------------------------
def q1_variable_basics():
    print("\n# Q1: Variable Basics — Predict the Output")
    print("# Task: Predict the value of c before the program reveals it.")

    a = 7
    b = 2
    c = a * b

    user_answer = input("What do you think c equals? ")

    try:
        user_answer = int(user_answer)
        if user_answer == c:
            print("Correct! Nice prediction.")
        else:
            print(f"Not quite. c is actually {c}.")
    except:
        print(f"That wasn't a number. c is {c}.")


# ------------------------------------------------
# Q2: Input + Type Conversion
# ------------------------------------------------
def q2_input_conversion():
    print("\n# Q2: Input + Type Conversion")
    print("# Task: Convert input to an integer and predict the result.")

    num = input("Enter a number: ")

    # Ask user to predict the type BEFORE conversion
    prediction = input("Before conversion, what type is num? (str/int/float/bool) ")

    # Self-grade prediction
    if prediction.lower() == "str":
        print("Correct — input() always returns a string.")
    else:
        print("Not quite — input() always returns a string.")

    # Convert and show type
    num = int(num)
    print(f"After conversion, type is: {type(num)}")


# ------------------------------------------------
# Q3: f-String Assembly
# ------------------------------------------------
def q3_fstring():
    print("\n# Q3: f-String Assembly")
    print("# Task: Build a sentence using variables and an f-string.")

    first = input("First name: ")
    last = input("Last name: ")
    city = input("City: ")

    user_sentence = input("Write your own f-string sentence using these values: ")

    # Simple self-grade: check if all variables appear
    if first in user_sentence and last in user_sentence and city in user_sentence:
        print("Nice! You used all variables.")
    else:
        print("Your sentence is missing one or more variables.")

    print(f"My example: {first} {last} lives in {city}.")


# ------------------------------------------------
# Q4: Type Guessing
# ------------------------------------------------
def q4_type_guessing():
    print("\n# Q4: Type Guessing")
    print("# Task: Guess the type of each variable before the program reveals it.")

    x = "42"
    y = 42
    z = 4.2
    w = True

    guess_x = input("Guess type of x ('42'): ")
    guess_y = input("Guess type of y (42): ")
    guess_z = input("Guess type of z (4.2): ")
    guess_w = input("Guess type of w (True): ")

    # Self-grading
    print("\nResults:")
    print(f"x is {type(x)} — {'Correct' if guess_x.lower() == 'str' else 'Incorrect'}")
    print(f"y is {type(y)} — {'Correct' if guess_y.lower() == 'int' else 'Incorrect'}")
    print(f"z is {type(z)} — {'Correct' if guess_z.lower() == 'float' else 'Incorrect'}")
    print(f"w is {type(w)} — {'Correct' if guess_w.lower() == 'bool' else 'Incorrect'}")


# ------------------------------------------------
# Q5: Convert & Combine
# ------------------------------------------------
def q5_convert_combine():
    print("\n# Q5: Convert & Combine")
    print("# Task: Convert input to integers and calculate future age.")

    age = int(input("Age: "))
    years = int(input("Years to add: "))

    future_age = age + years

    user_sentence = input("Write the sentence: 'You will be X years old in Y years.' ")

    # Self-grade: check if numbers appear
    if str(future_age) in user_sentence and str(years) in user_sentence:
        print("Great! You included both values.")
    else:
        print("Your sentence is missing one or both values.")

    print(f"My example: You will be {future_age} years old in {years} years.")


# ------------------------------------------------
# Q6: Stretch Challenge — Mini Profile Generator + Error Handling
# ------------------------------------------------
def q6_stretch():
    print("\n# Q6: Stretch Challenge — Profile Generator with Error Handling")
    print("# Task: Gather user info, convert types safely, and print a summary.")

    name = input("Name: ")
    city = input("City: ")

    # Safe integer input
    while True:
        age_input = input("Age: ")
        if age_input.isdigit():
            age = int(age_input)
            break
        else:
            print("Please enter a valid number for age.")

    while True:
        fav_input = input("Favorite number: ")
        if fav_input.lstrip("-").isdigit():
            fav = int(fav_input)
            break
        else:
            print("Please enter a valid number.")

    future_age = age + 10
    triple = fav * 3

    print("\nYour Profile Summary:")
    print(f"{name} lives in {city} and is {age} years old.")
    print(f"In 10 years, they will be {future_age}.")
    print(f"Their favorite number tripled is {triple}.")

    print("\nStretch challenge complete — nice work.")


# ------------------------------------------------
# Main Loop
# ------------------------------------------------
while True:
    menu()
    choice = input("Choose an option: ")

    if choice == "1":
        q1_variable_basics()
    elif choice == "2":
        q2_input_conversion()
    elif choice == "3":
        q3_fstring()
    elif choice == "4":
        q4_type_guessing()
    elif choice == "5":
        q5_convert_combine()
    elif choice == "6":
        q6_stretch()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
