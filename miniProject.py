import pandas as pd
import matplotlib.pyplot as plt
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

print(Fore.CYAN + "\n📊 Welcome to the E-Commerce Order Analytics Dashboard\n")

# Collect orders
orders = []
order_ids = set()
customer_ids = set()

while True:
    order_id = input(Fore.YELLOW + "🆔 Enter Order ID (or 'done' to finish): ")
    if order_id.lower() == "done":
        break
    if order_id in order_ids:
        print(Fore.RED + "⚠️ Duplicate Order ID! Try again.\n")
        continue

    customer_id = input(Fore.YELLOW + "👤 Enter Customer ID: ")
    if customer_id in customer_ids:
        print(Fore.RED + "⚠️ Duplicate Customer ID! Try again.\n")
        continue

    product = input(Fore.YELLOW + "📦 Enter Product Name: ")
    category = input(Fore.YELLOW + "🏷️ Enter Category: ")

    try:
        quantity = int(input(Fore.YELLOW + "🔢 Enter Quantity: "))
        price = float(input(Fore.YELLOW + "💵 Enter Price per Item: "))
    except ValueError:
        print(Fore.RED + "❌ Invalid number! Start again.\n")
        continue

    orders.append({
        "order_id": order_id,
        "customer_id": customer_id,
        "product_name": product.title(),
        "category": category.title(),
        "quantity": quantity,
        "price": price
    })

    order_ids.add(order_id)
    customer_ids.add(customer_id)
    print(Fore.GREEN + "✅ Order added successfully!\n")

# Create DataFrame
if not orders:
    print(Fore.RED + "\n⚠️ No orders entered. Exiting.")
    exit()

df = pd.DataFrame(orders)
df["total_price"] = df["quantity"] * df["price"]

# --- Metrics ---
total_orders = len(df)
total_revenue = df["total_price"].sum()
aov = round(total_revenue / total_orders, 2)
popular_products = df.groupby("product_name")["quantity"].sum().sort_values(ascending=False)
category_counts = df["category"].value_counts()

# --- Summary ---
print(Fore.CYAN + "\n📈 ANALYTICS SUMMARY")
print(Fore.MAGENTA + f"🧾 Total Orders: {total_orders}")
print(Fore.MAGENTA + f"💰 Total Revenue: ${total_revenue}")
print(Fore.MAGENTA + f"📊 Average Order Value (AOV): ${aov}")

print(Fore.CYAN + "\n🛍️ Top Selling Products:")
print(popular_products.to_string())

print(Fore.CYAN + "\n🏷️ Orders by Category:")
print(category_counts.to_string())

# --- Plot 1: Top Products ---
plt.figure(figsize=(8, 5))
popular_products.plot(kind="bar", color="lightblue")
plt.title("Top Selling Products")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.tight_layout()
plt.show()

# --- Plot 2: Category Distribution ---
plt.figure(figsize=(6, 6))
category_counts.plot(kind="pie", autopct="%1.1f%%", startangle=90, colors=["lightgreen", "orange", "lightcoral"])
plt.title("Orders by Category")
plt.ylabel("")
plt.tight_layout()
plt.show()
