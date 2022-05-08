price_product_1=input("What is the price of product 1:")
quantity_product_1=input("What will be the quantity of product 1:")
price_product_2=input("What is the price of product 2:")
quantity_product_2=input("What will be the quantity of product 2:")
price_product_3=input("What is the price of product 3:")
quantity_product_3=input("What will be the quantity of product 3:")

result_product_1=float(price_product_1)*float(quantity_product_1)
result_product_2=float(price_product_2)*float(quantity_product_2)
result_product_3=float(price_product_3)*float(quantity_product_3)

result=result_product_1+result_product_2+result_product_3
print("Your final price is "+str(result))