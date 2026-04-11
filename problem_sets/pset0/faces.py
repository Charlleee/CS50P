
# CS50P Problem set 0 - faces
# The task, take a users input sentence and replace every occurrence of :) with 😀 and every occurrence of :( with 🙁.

def main():
    text = input("input: ")
    print(convert(text))

def convert(s):

    s = s.replace(":)", "😀")
    s = s.replace(":(", "🙁")
    return s

main()