def question():
    rules=input("You need to answer every question by yes or no Do you understand: ")
    if rules!="yes":
        return print("Try again")
    else:print("Next question")
    Quest1=input("Are you hungry: ")
    if Quest1!="yes":
        return print("Then let's go for walk")
    else:print("Next question")
    Quest2=input("Do you want to eat at restaurant: ")
    if Quest2!="yes":
        return print("Come eat at my place")
    else:print("Next question")
    Quest3=input("Do you want to eat a pizza: ")
    if Quest3!="yes":
        return print("let's go to eat burger then")
    else:print("let's go to eat pizza")

question()