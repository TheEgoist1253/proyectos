def apply_discount(price,discount):
    if not isinstance(price,(int,float)):
       return "The price should be a number"
    if not isinstance(discount,(int,float)):
        return "The discount should be a number"
    if price <=0:
        return "The price should be greater than 0"
    if discount <0 or discount > 100:
        return "The discount should be between 0 and 100"
    result = price - (price * (discount / 100))
    return  result



    



price = input("Coloque precio del producto: ")
discount = input("Coloque descuento: ")

try:
    price = float(price)
    discount = float(discount)
except:
    print("The price and discount should be numbers")
else:
    final_result = apply_discount(price, discount)
    print(final_result)

