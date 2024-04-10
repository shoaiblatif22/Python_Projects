print("Welcome to my computer quiz!") 

playing = input("Do you want to play? ")

if playing == "Yes" or "yes":
    print("Okay! Let's play")
else:
    quit()

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("Correct!")
else:
    print("Incorrect, try again")