# Project: Lovely Loveseats

# Inventory #
# Item: "Lovely Loveseat"
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price = 254.00

# Item: "Stylish Settee"
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.50

# Item: "Luxurious Lamp"
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15

# Defining the sales tax value.
sales_tax = .088


# We're ready for business! #

# First Customer Arrives
customer_one_total = 0
customer_one_itemization = ""
customer_one_total_items = 0

# Customer One makes their first purchase.
customer_one_total += lovely_loveseat_price
customer_one_total_items += 1
customer_one_new_item_text = "(" + str(customer_one_total_items) + ") "
customer_one_itemization += customer_one_new_item_text + lovely_loveseat_description

# Customer One makes their second purchase.
customer_one_total += luxurious_lamp_price
customer_one_total_items += 1
customer_one_new_item_text = "(" + str(customer_one_total_items) + ") "
customer_one_itemization += " " + customer_one_new_item_text + luxurious_lamp_description

# Customer One is ready to check out.
# Calculating the sales tax and adding to their total.
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

# Printing their receipt.
print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)
