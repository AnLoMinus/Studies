def per_1(name):
    print(name+": Hello, how can i help you")

def person2_1(food,drink,dessert,name):
    name=input("what is your name:")
    food=input("What do you want eat:")
    drink=input("what do you want to drink:")
    dessert=input("what dessert do you want:")
    print(name+": I would like "+food+" I want drink "+drink+" I want "+dessert+" as a dessert")

def per1_2(name):
    print(name+": Thank you")

per_1("cashier")
person2_1("food","drink","dessert","name")
per1_2("cashier")