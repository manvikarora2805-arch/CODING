
snack_name   = "Chips"    # str   — text
price        = 1.50       # float — decimal
quantity     = 10         # int   — whole number
is_available = True       # bool  — True or False

print("Snack:", snack_name)
print("Price: $", price)
print("In Stock:", quantity)
print("Available?", is_available)

print(type(snack_name))
print(type(price))
print(type(quantity))
print(type(is_available))

total = price * quantity
print("Total value: $", total)
print("Sale price: $", price - 0.25)
print("Double stock:", quantity * 2)

print("Is price under $2?", price < 2)
print("More than 5 in stock?", quantity > 5)
print("Is price exactly $1.50?", price == 1.50)

price_a = 1.50
price_b = 3.00
print("Before:", price_a, "and", price_b)

temp    = price_a
price_a = price_b
price_b = temp

print("After:", price_a, "and", price_b)