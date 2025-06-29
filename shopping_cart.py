# Shopping cart project

foods = []
prices = []
total = 0

while True:
    food = input("Enter food to buy or press q to quit: ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of the {food}: M"))
        foods.append(food)
        prices.append(price)
        
print("---- Your Cart ----")

for food in foods:
    print(food,end=(" "))
    
for price in prices:
    total += price

print("\n")
print(f"Your total is: M{total}")