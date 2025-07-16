# 🛒 E-Commerce Order Analytics Dashboard

A user-friendly, interactive Python program to collect and analyze e-commerce order data. It helps visualize sales insights, avoid duplicate entries, and generate key performance metrics using **Pandas**, **Matplotlib**, and **Colorama**.

## 🚀 Features

- 🔐 **Prevents Duplicate Entries** for Order ID and Customer ID
- 📦 **Collects Detailed Order Info** (product, category, quantity, price)
- 📈 **Generates Analytics Summary**
  - Total Orders
  - Total Revenue
  - Average Order Value (AOV)
  - Top-Selling Products
  - Orders by Category
- 📊 **Visual Charts**
  - Bar chart for top-selling products
  - Pie chart for category distribution
- 🌈 **Color-coded Terminal Output** for better interactivity

## 📁 Project Structure

```
ecommerce-analytics-dashboard/
├── order_dashboard.py        # Main Python script
├── README.md                 # Project documentation
```

## 🛠️ Requirements

- Python 3.x
- pandas
- matplotlib
- colorama

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/ecommerce-analytics-dashboard.git
cd ecommerce-analytics-dashboard
```

2. Install dependencies:
```bash
pip install pandas matplotlib colorama
```

## 🧪 Usage

Run the script:
```bash
python order_dashboard.py
```

Follow the on-screen prompts to enter orders. Type `done` when finished.

### Sample Input Flow:
```
🆔 Enter Order ID (or 'done' to finish): ORD001
👤 Enter Customer ID: CUST001
📦 Enter Product Name: Laptop
🏷️ Enter Category: Electronics
🔢 Enter Quantity: 2
💵 Enter Price per Item: 65000
✅ Order added successfully!
```

### Output Summary:
```
📈 ANALYTICS SUMMARY
🧾 Total Orders: 3
💰 Total Revenue: $129999.99
📊 Average Order Value (AOV): $43333.33

🛍️ Top Selling Products:
Laptop       2
Mouse        1
Phone        1

🏷️ Orders by Category:
Electronics    3
Accessories    1
```

### Charts:
- 📊 Bar chart: Top selling products
- 🥧 Pie chart: Category-wise order distribution

## 📌 Tech Stack

- **Python**
- **Pandas** for data handling
- **Matplotlib** for charting
- **Colorama** for colored terminal UI

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---
Made with ❤️ using Python
