# Project: Sal's Shipping
# by: @Brohmarr

# Sal runs the biggest shipping company in the tri-county area, Sal’s
#     Shippers. Sal wants to make sure that every single one of his
#     customers has the best, and most affordable experience shipping
#     their packages.
# 
# In this project, you’ll build a program that will take the weight of a
#     package and determine the cheapest way to ship that package using
#     Sal’s Shippers.


# The weight of the package (in pounds).
weight = 2.0

# Ground Shipping
ground_price = 0.0
ground_flat_charge = 20.0

if weight < 0:
  print("Error")
elif weight <= 2.0:
  ground_price = (weight * 1.5) + ground_flat_charge
elif weight > 2.0 and weight <= 6.0:
  ground_price = (weight * 3.0) + ground_flat_charge
elif weight > 6.0 and weight <= 10.0:
  ground_price = (weight * 4.0) + ground_flat_charge
else:
  ground_price = (weight * 4.75) + ground_flat_charge

print("Ground Shipping: $ ", ground_price)

# Ground Shipping Premium
ground_premium_price = 125.0

print("Ground Shipping Premium: $ ", ground_premium_price)

# Drone Shipping
drone_price = 0.0

if weight < 0:
  print("Error")
elif weight <= 2.0:
  drone_price = (weight * 4.5)
elif weight > 2.0 and weight <= 6.0:
  drone_price = (weight * 9.0)
elif weight > 6.0 and weight <= 10.0:
  drone_price = (weight * 12.0)
else:
  drone_price = (weight * 14.25)

print("Drone Shipping: $ ", drone_price)

# Checking which is the cheapest method of shipping.
default_message = 'The cheapest method of shipping for your package is the '
print()

if ground_price < ground_premium_price and ground_price < drone_price:
  print(default_message, '"Ground Shipping".')
elif ground_premium_price < drone_price:
  print(default_message, '"Ground Shipping Premium".')
else:
  print(default_message, '"Drone Shipping".')
