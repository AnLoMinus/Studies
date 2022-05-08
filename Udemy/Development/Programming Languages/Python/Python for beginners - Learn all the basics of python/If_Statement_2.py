pers1_name=input("What is your Name: ")
pers1_wallet=input("How much money do you have: ")

pers2_name=input("What is your Name: ")
pers2_wallet=input("How much money do you have: ")

pers3_name=input("What is your Name: ")
pers3_wallet=input("How much money do you have: ")

if float(pers1_wallet)>float(pers2_wallet) and float(pers1_wallet)>float(pers3_wallet):
    print(pers1_name+ " is the richest")
elif float(pers2_wallet)>float(pers1_wallet) and float(pers2_wallet)>float(pers3_wallet):
    print(pers2_name+ " is the richest")
elif float(pers3_wallet)>float(pers1_wallet) and float(pers3_wallet)>float(pers2_wallet):
    print(pers3_name+ " is the richest")