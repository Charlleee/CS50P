# ----------------------------------------
# 1. Indoor Voice
# Convert input text to lowercase.
# ----------------------------------------
def indoor_voice():
    text = input("___")
    print(text.___())


# ----------------------------------------
# 2. Playback Speed
# Replace spaces with "..." in the input.
# ----------------------------------------
def playback_speed():
    text = input("___")
    print(text.replace("___", "___"))


# ----------------------------------------
# 3. Making Faces
# Replace :) with 🙂 and :( with 🙁.
# ----------------------------------------
def making_faces():
    text = input("___")
    text = text.replace("___", "___").replace("___", "___")
    print(text)


# ----------------------------------------
# 4. Einstein
# Compute E = m * c^2 using c = 300000000.
# ----------------------------------------
def einstein():
    m = int(input("___"))
    c = ___
    e = m * c * c
    print(e)


# ----------------------------------------
# 5. Tip Calculator
# Calculate bill + tip percentage, formatted to 2 decimals.
# ----------------------------------------
def tip_calculator():
    bill = float(input("___"))
    percent = float(input("___"))
    tip = bill * (percent / ___)
    print(f"Total: {___:.2f}")


# ----------------------------------------
# 6. Deep Thought
# Check if input equals 42 in various forms.
# ----------------------------------------
def deep_thought():
    answer = input("___").lower()
    if answer == "___" or answer == "___" or answer == "___":
        print("Yes")
    else:
        print("No")


# ----------------------------------------
# 7. Home Federal Savings Bank
# Greeting → cost based on how it starts.
# ----------------------------------------
def bank():
    greet = input("___").lower()
    if greet.startswith("___"):
        print("$0")
    elif greet.startswith("___"):
        print("$20")
    else:
        print("$100")


# ----------------------------------------
# 8. File Extensions
# Determine media type based on file extension.
# ----------------------------------------
def file_extensions():
    file = input("___").lower().strip()
    ext = file.split(".")[-1]

    if ext == "___":
        print("___")
    elif ext == "___":
        print("___")
    elif ext == "___":
        print("___")
    else:
        print("application/octet-stream")


# ----------------------------------------
# 9. Math Interpreter
# Evaluate simple expressions like "3 + 4".
# ----------------------------------------
def math_interpreter():
    x, op, y = input("___").split()
    x = float(x)
    y = float(y)

    if op == "___":
        print(___)
    elif op == "___":
        print(___)
    elif op == "___":
        print(___)
    elif op == "___":
        print(___)


# ----------------------------------------
# 10. Meal Time
# Convert HH:MM to float and check meal ranges.
# ----------------------------------------
def meal_time():
    time = input("___")
    hours, minutes = time.split(":")
    t = int(hours) + int(minutes) / ___

    if ___ <= t <= ___:
        print("breakfast time")
    elif ___ <= t <= ___:
        print("lunch time")
    elif ___ <= t <= ___:
        print("dinner time")


# ----------------------------------------
# MENU SYSTEM
# ----------------------------------------
def main():
    while True:
        print("\nCS50P Week 0 Practice Menu")
        print("1. Indoor Voice")
        print("2. Playback Speed")
        print("3. Making Faces")
        print("4. Einstein")
        print("5. Tip Calculator")
        print("6. Deep Thought")
        print("7. Home Federal Savings Bank")
        print("8. File Extensions")
        print("9. Math Interpreter")
        print("10. Meal Time")
        print("0. Exit")

        choice = input("Choose a problem: ")

        if choice == "1":
            indoor_voice()
        elif choice == "2":
            playback_speed()
        elif choice == "3":
            making_faces()
        elif choice == "4":
            einstein()
        elif choice == "5":
            tip_calculator()
        elif choice == "6":
            deep_thought()
        elif choice == "7":
            bank()
        elif choice == "8":
            file_extensions()
        elif choice == "9":
            math_interpreter()
        elif choice == "10":
            meal_time()
        elif choice == "0":
            print("Goodbye")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
