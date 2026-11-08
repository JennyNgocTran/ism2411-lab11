# Reflection Questions
# 1. I would use bracket notation when I know that the key must be there. But, I would use .get() for fields that may be blank to avoid raising an error.
# 2. It reminds me of Excel SUMIFs and PivotTables. Python uses the same four lines of code to process it instantly no matter how long the list.

print("--- Exercise 1: One Customer ---")

customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400,
}

print(customer["name"]) # Accessing value using bracket notation
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

print("--- Exercise 2: Update and Add ---")

customer["phone"] = "813-555-0142"

print(customer)
customer["tier"] = "platinum"

print(customer)
del customer["email"]

print(customer)

print("--- Exercise 3: Safe Lookup ---")

# New Version
print(customer.get("email", "No email on file"))

# Old Version
try:
    print(customer["email"])
except KeyError as error:
    print(f"KeyError Caught: {error}")

print("--- Excercise 4: Iterate ---")

for key, value in customer.items():
    print(f"{key} : {value}")
# Iterating with .items() prints every key:value pair

for item in customer:
    print(item)
# Iterating without .items() only gives the key

print("--- Exercise 5: Lookup Table ---")

tier_discounts = {"bronze": 0, 
                  "silver": .05,
                  "gold": .10,
                  "platinum": .15}
purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)

print(f"Tier: {customer['tier']}") # platinum
print(f"Discount: {discount_rate * 100:.0f}%") # 15%
print(f"Final price: ${final_price:.2f}") # $170.00

print("--- Exercise 6: List of dicts ---")

customers = [
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "Carol", "tier": "gold", "ytd_spend": 8750},
    {"name": "David", "tier": "bronze", "ytd_spend": 450}
]

for record in customers:
    rate = tier_discounts.get(record["tier"], 0)
    discount = 300 * rate # assuming a purchase of $300 for each customer
    print(f"{record['name']} ({record['tier']}): ${discount:.2f} discount on $300 purchase")

print("--- Exercise 7: Nested Catalog ---")

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} - Only {details['stock']} left in stock!")

print("--- Exercise 8: Sales by Region ---")

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]
sales_by_region = {} # empty dictionary to hold sales totals by region
for sale in transactions:
    region = sale["region"]
    sales_by_region[region] = sales_by_region.get(region, 0) + sale["amount"]
print(sales_by_region) # prints raw dictionary with sales totals by region

for key, value in sales_by_region.items():
    print(f"{key}: {value}")