#name = input("What's your name? ").strip().title()
#.strip() removes any leading or trailing whitespace from the input, ensuring that the name is clean and properly formatted. .title() converts the first letter of each word to uppercase and the rest to lowercase, making the name look neat and standardized.
#.title() Capitalizes the first letter of each word in the input string, which is useful for formatting names properly. For example, if the user inputs "john doe", it will be transformed to "John Doe".    
#input() gets users text
#variable stores it
#f-string prints it cleanly



#CS50P Problem set 0 - playback speed
#The task, take a users input sentence and replace every space with "..." and print the result.
#playback.py

text = input("input: ")
text = text.replace(" ", "...")
print (text)

