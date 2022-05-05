
""" Example to demonstrate requirement mapping """

""" Part 1 """
option = input("Press any key, then tap 'enter':")

if option.isalnum():
    print("is not special")
else:
    print("is special!")
print("option='" + option + "'")


""" Part 2 (Above, with comments) """

# Get as str() from the user
option = input("Press any key, then tap 'enter':")

# Use associated "member function" of str() 
if option.isalnum():
    # If is alpha-numeric
    print("is not special")
else:
    # If is NOT alpha-numeric
    print("is special!")
# Show what was entered
print("option='" + option + "'")


""" Part 3 - BASIC FUNCTION ORGANIZATION """

def readInput():
    zoption = input("Input:")
    return zoption.isalnum()

torf = readInput()

if torf == True:
    print(option, "is not special")
else:
    print(option, "is special!")

""" Part 4 - BASIC CLASS ORGANIZATION """

class MyClass:
    def readInput():
        zoption = input("Input:")
        return zoption.isalnum()
    
""" Part 5 - SOLUTION """

optionA = input("Enter A:")

optionB = input("Enter B:")

concat = optionA + optionB

print("A + B",concat)


