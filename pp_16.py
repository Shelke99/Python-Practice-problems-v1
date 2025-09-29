# Compute profit or loss given the cost price and the selling price.
cost_price = float(input("enter cost of price: "))
selling_price = float(input("enter selling price: "))
if cost_price > selling_price:
    loss = cost_price - selling_price
    print("we are in the loss")
elif cost_price < selling_price:
    loss = selling_price - cost_price
    print("we are in the gain")
else:
    print("we are in the no profit and loss")