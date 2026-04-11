#----------------------------------
# 1. Indoor Voice
# Convert input text to lower case.
#----------------------------------
def indoor_voice():
    text = input("How are you today? ")
    print(text.lower())

#indoor_voice()

def playback_speed():
    text = input("name your three favorite meals: ")  
    print(text.replace(" ", "..."))
                       
                       
#playback_speed()

#making faces
def making_faces():
    text = input("  ")
    text = text.replace(":)", "😊").replace(":(", "🙁")
    print(text)
#making_faces()


#Compute E = m * C^2 using c = 3000000
def einstein():
    m = int(input("Mass in kilograms: "))
    c = 3000000
    e = m * c * c
    print (e)
#einstein()

def tip_calculator():
    bill = float(input("Please provide bill amount: "))
    percent = float(input("What percentage tip would you like to leave? "))
    tip = bill * (percent/ 100)
    print(f"Total: {(bill) + (tip)}")
#tip_calculator()

# Check if input equals 42 in various forms
#def deep_thought():

def menu():
     print("\n---S1 M3 Practice Menu ---") 
     print("1. Variable Basics")
     print("2. Input + Type conversion")
     print("3. f-string practice")
     print("4. Exit")
 
#menu()

def variable_basics():
    x = 10
    y = 3.14
    z = "Python"
    print(f"x={x}, y={y}, z = {z}")
#variable_basics()

def input_conversion():
    age = int(input("Enter your age: "))
    print(f"In 5 years, you will lbe {age + 5}")
#input_conversion()

def fstring_practice():
    name = input("Name: ")
    city = input("City: ")
    print(f"{name} lives in {city} and is learninig Python!")
#fstring_practice()

 #while True:
  #  menu()
   # choice = input("Choose an option: ")

    #if choice == "1":
     #   variable_basics()
    #elif choice == "2":
    #    input_conversion()
    #elif choice == "3":
    #    fstring_practice()
    #elif choice == "4":
     #   print("Goodbye!")
     #   break
    #else:
    #    print("Invalid choice.  Try again.")
    
#menu()

# # Micro-Exercise 1
# a = 7
# b = 2
# c = a * b
# d = "Python"

# 5print(a, b, c, d)

          
# # Micro-Exercise 2
# num = input("Enter a number: ")
# print(type(num))

# num = int(num)
# print(type(num))
# print(num * 5)


#   # Micro-Exercise 3
# first = input("First name: ")
# last = input("Last name: ")
# city = input("City: ")

# print(f"{first} {last} lives in {city}.")
 
# 
# Micro-Exercise 5
age = int(input("Age: "))
years = int(input("Years to add: "))

future_age = age + years
print(f"In {years} years, you will be {future_age}.")
