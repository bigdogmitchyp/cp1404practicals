number_of_items = int(input("Number of items: "))
total_of_items = 0
price_of_item = 0

while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items, 0, -1):
    price_of_item = float(input("Price of item: "))
    total_of_items = total_of_items + price_of_item

if total_of_items > 100:
    total_of_items = total_of_items * .9
print(f"Total price for {number_of_items} items is ${total_of_items:.2f}")
