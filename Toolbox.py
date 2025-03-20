def basic_output():
    print('Love you Kelley, please dont murder me for butchering this test')
    print('\n')
    return basic_output


def variable_example():
    name = "Jake"
    age = 23
    salary = 0.00
    print("Name:", name)
    print("Age:", age)
    print("Salary:", salary)
    return name,age,salary

def input_example():
    user_name = input("Enter your name: ")
    user_age = input("Enter your age: ")
    print("Hello,", user_name + "! You are", user_age, "years old and broke.")
    return user_name,user_age


def miles_per_gallon():
    miles = float(input("Please enter the number of miles you have driven: "))
    gallons = float(input("Please enter the number of gallons used: "))
    mpg = miles / gallons
    print(f"Miles per gallon: {mpg}")
    return miles, gallons, mpg

def meal_total():
    food_cost = float(input("Please enter the cost of your meal: "))
    tip = food_cost * 0.18
    tax = food_cost * 0.07
    total = food_cost + tip + tax
    print(f"Your total is: {total}")
    return food_cost, tip, tax, total

def stock_transactions():
    shares = 2000
    purchase_price = 40.00
    selling_price = 42.75
    commission_rate = 0.03
    purchase_cost = shares * purchase_price
    purchase_commission = purchase_cost * commission_rate
    selling_revenue = shares * selling_price
    selling_commission = selling_revenue * commission_rate
    profit = selling_revenue - selling_commission - purchase_cost - purchase_commission
    print(f"Joe made a profit/loss of: ${profit}")
    return shares, purchase_price, selling_price, commission_rate, purchase_cost, purchase_commission, selling_revenue

def day_of_week():
    num = int(input("Enter a number 1-7 for the day of the week: "))
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if 1 <= num <= 7:
        print(f"Day: {days[num - 1]}")
    else:
        print("Invalid input.")
    return day_of_week

def mass_weight():
    mass = float(input("Enter mass in kg: "))
    weight = mass * 9.8
    if weight > 500:
        print("Object is too heavy.")
    elif weight < 100:
        print("Object is too light.")
    else:
        print(f"Weight: {weight:.2f} N")
    return mass, weight

def change_for_dollar():
    pennies = int(input("Enter pennies: "))
    nickels = int(input("Enter nickels: "))
    dimes = int(input("Enter dimes: "))
    quarters = int(input("Enter quarters: "))
    total = (pennies * 0.01) + (nickels * 0.05) + (dimes * 0.10) + (quarters * 0.25)
    print(f"Total amount entered: ${total:.2f}")
    return total

def shipping_charges():
    weight = float(input("Enter package weight in pounds: "))
    if weight <= 2:
        cost = 1.50
    elif weight <= 6:
        cost = 3.00
    elif weight <= 10:
        cost = 4.00
    else:
        cost = 4.75
    print(f"Shipping cost: ${cost:.2f}")
    return weight, cost

def bug_collector():
    total_bugs = 0
    for day in range(1, 6):
        bugs = int(input(f"Enter bugs collected on day {day}: "))
        total_bugs += bugs
    print(f"Total bugs collected: {total_bugs}")
    return total_bugs

def register_customer():
    full_name = input('Please enter your full name: ')

    while True:
        try:
            age = input('Please enter your age: ')
            if age > 0:
                break
        except ValueError:
            print('Please enter a number greater than 0 for your age')
            break
    while True:
        email = input('Please enter your email: ')
        if "@" in email: 
            break
        else:
            print(''''Please make sure you put in @ in your email 
    ex. JohnDoe@Gmail.com''')
    while True:
        phone_number = input('Please enter your phone number: ')
        try:
            int(phone_number)
            break
        except ValueError:
            print('Please make sure your phone number contains only numbers. No letters or "-"')


    return full_name, age, email, phone_number

products = {
    1: {"name": "Keyboard", "price": 50},
    2: {"name": "Mouse", "price": 30},
    3: {"name": "Monitor", "price": 200},
    4: {"name": "Headset", "price": 80},
    5: {"name": "USB Drive", "price": 25}
}


def display_catalog():
    catalog = "Available Products:\n"
    for key, item in products.items():
        catalog += f"{key}. {item['name']} - ${item['price']}\n"
    return catalog


def select_product():
    while True:
        try:
            product_num = int(input("Enter product number: "))
            if product_num in products:
                break
            print("Invalid product number. Choose from catalog.")
        except ValueError:
            print("Invalid. Enter a numeric value.")

    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity > 0:
                break
            print("Invalid quantity. Please enter a positive number.")
        except ValueError:
            print("Invalid input. Enter a numeric value.")
    
    return product_num, quantity


def calculate_discount(subtotal, quantity):
    return subtotal * 0.10 if quantity > 5 else 0


def calculate_tax(subtotal):
    return subtotal * 0.085


def generate_receipt(customer, product, quantity, subtotal, discount, tax, total):
    receipt = (f"\nReceipt:\n"
            f"Customer: {customer}\n"
            f"Product: {products[product]['name']} ({quantity})\n"
            f"Subtotal: ${subtotal:.2f}\n"
            f"Discount: -${discount:.2f}\n"
            f"Sales Tax: ${tax:.2f}\n"
            f"Final Total: ${total:.2f}\n")
    return receipt

def collect_data():
    business_name = input("What is the name of your business?: ")
    revenue = float(input("What is your businesses total revenue?: $ "))
    expenses = float(input("What are your businesses total expenses?: $ "))
    employees = int(input("How many employees does your business have?: "))
    tax_rate = float(input("What is your businesses tax rate?:% ")) / 100
    loan_balance = float(input("What is the balance of your loans?: $ "))
    return business_name, revenue, expenses, employees, tax_rate, loan_balance

def calculate_financials(revenue, expenses, employees, tax_rate, loan_balance):
    net_profit = revenue - expenses
    tax_owed = net_profit * tax_rate if net_profit > 0 else 0
    profit_per_employee = net_profit / employees if employees > 0 else 0
    if loan_balance > 0:
        debt_ratio = loan_balance / revenue
    return net_profit, tax_owed, profit_per_employee, debt_ratio

def evaluate_financials(net_profit, profit_per_employee, tax_owed, debt_ratio):   
    recommendations = []
    if net_profit < 0:
        recommendations.append(print("Net profit is negative, you are operating at a loss. Increase revenue or reduce expenses suggested."))
    if profit_per_employee < 100:
        recommendations.append(print('Profit Per Employee is low, workforce efficiency improvements suggested'))
    if tax_owed > 50000:
        recommendations.append(print('Taxes owed were found to be high. Reviewing business tax deductions suggested'))
    if debt_ratio > 1:
        recommendations.append(print('Debt ratio is high. Caution advised on further borrowing and additional financial planning suggested.'))
    if not recommendations:
        recommendations.append("Your business is fine.")
    return recommendations

def generate_report(business_name, revenue, expenses, net_profit, tax_owed, profit_per_employee, debt_ratio, recommendations):
    print(business_name + ' Financial Report')
    print(f"Revenue: ${revenue:,.2f}")
    print(f"Expenses: ${expenses: ,.2f}")
    print(f"Net Profit: ${net_profit: ,.2f}")
    print(f"Tax Owed: ${tax_owed: ,.2f}")
    print(f"Profit Per Employee: ${profit_per_employee: ,.2f}")
    print(f"Debt Ratio: %{debt_ratio * 100: .2f}")


def main():
    basic_output()
    name,age,salary = variable_example()
    user_name,user_age = input_example()
    miles, gallons, mpg = miles_per_gallon()
    food_cost, tip, tax, total = meal_total()
    shares, purchase_price, selling_price, commission_rate, purchase_cost, purchase_commission, selling_revenue = stock_transactions()
    day_of_week()
    mass, weight = mass_weight()
    total_amount = change_for_dollar()
    weight, shipping_cost = shipping_charges()
    total_bugs = bug_collector()
    customer = register_customer()
    print(display_catalog())
    product, quantity = select_product()
    subtotal = products[product]['price'] * quantity
    discount = calculate_discount(subtotal, quantity)
    tax = calculate_tax(subtotal - discount)
    total = subtotal - discount + tax
    print(generate_receipt(customer, product, quantity, subtotal, discount, tax, total))
    print("\nBusiness Financial Report Generator")
    business_name, revenue, expenses, employees, tax_rate, loan_balance = collect_data()
    net_profit, tax_owed, profit_per_employee, debt_ratio = calculate_financials(revenue, expenses, employees, tax_rate, loan_balance)
    recommendations = evaluate_financials(net_profit, profit_per_employee, tax_owed, debt_ratio)
    generate_report(business_name, revenue, expenses, net_profit, tax_owed, profit_per_employee, debt_ratio, recommendations)


main()
