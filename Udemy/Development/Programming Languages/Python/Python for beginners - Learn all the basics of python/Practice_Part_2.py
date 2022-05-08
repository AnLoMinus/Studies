name_1=input("What is your name:")
name_2=input("What is your name:")
name_3=input("What is your name:")
slices_in_the_pizza=input("How many slices in the pizza:")
price_of_the_pizza=input(" What is the price of the pizza:")

percentage_ate_by_person_1=input(name_1+" What percentage of the pizza you have ate:")
percentage_ate_by_person_2=input(name_2+" What percentage of the pizza you have ate:")
percentage_ate_by_person_3=input(name_3+" What percentage of the pizza you have ate:")

number_of_slices_ate_person_1=float(percentage_ate_by_person_1)*float(slices_in_the_pizza)
number_of_slices_ate_person_2=float(percentage_ate_by_person_2)*float(slices_in_the_pizza)
number_of_slices_ate_person_3=float(percentage_ate_by_person_3)*float(slices_in_the_pizza)

price_paid_by_name_1=float(percentage_ate_by_person_1)*float(price_of_the_pizza)
price_paid_by_name_2=float(percentage_ate_by_person_2)*float(price_of_the_pizza)
price_paid_by_name_3=float(percentage_ate_by_person_3)*float(price_of_the_pizza)

print(name_1+" have ate "+str(number_of_slices_ate_person_1)+" slices and have paid "
      +str(price_paid_by_name_1)+"$ for his meal")
print(name_2+" have ate "+str(number_of_slices_ate_person_2)+" slices and have paid "
      +str(price_paid_by_name_2)+"$ for his meal")
print(name_3+" have ate "+str(number_of_slices_ate_person_3)+" slices and have paid "
      +str(price_paid_by_name_3)+"$ for his meal")