our_password="pass123"
your_answer=" "
number_of_try=0
number_max_of_try=3
max_try="Not Reached"

while your_answer!=our_password and max_try!="Reached":
    if number_of_try<number_max_of_try:
        your_answer=input("What is the password")
        number_of_try=number_of_try+1
    else:
        max_try="Reached"


if max_try=="Reached":
    print("account blocked")
else:
    print("access granted")
