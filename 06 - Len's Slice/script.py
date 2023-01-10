# Project: Len's Slice
# by: @Brohmarr

# You work at Len’s Slice, a new pizza joint in the neighborhood. You
#     are going to use your knowledge of Python lists to organize some
#     of your sales data.


# List of toppings.
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives",
            "anchovies", "mushrooms"]

# List of prices.
prices = [2, 6, 1, 3, 2, 7, 2]

# Boss asked to do some research on $2 slices.
num_two_dollar_slices = prices.count(2)

# Number of different pizza slices we have.
num_pizzas = len(toppings)

# Displaying how many different pizza slices we have.
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

# Revamping the types of pizza slices available.
prices_and_pizzas = [[4, "egg and bacon"], [2, "pineapple"],
                     [4, "four cheese pizza"], [3, "pepperoni"],
                     [5, "chocolate"], [10, "all in one"]]

# Displaying the new pizza slices.
print(prices_and_pizzas)

# Sorting the new slices list in ascending order (prices).
prices_and_pizzas.sort()

# Getting the cheapest pizza on the menu.
cheapest_pizza = prices_and_pizzas[0]

# A customer walks into the pizza store and shouts "I will have your
#     MOST EXPENSIVE pizza!". Let's sell it!
priciest_pizza = prices_and_pizzas[-1]

# That was the last "all in one" pizza slice, let's remove it from the
#     menu.
prices_and_pizzas.pop()

# Let's add a new topping to keep customers excited.
prices_and_pizzas.insert(1, [2.5, "peppers"])

# Displaying the new menu.
print(prices_and_pizzas)

# Three mice walk into the store looking a bit hungry... Let's give
#     Ratatouille's friends the cheapest pizza slices.
three_cheapest = prices_and_pizzas[0:3]

# They loved it! Earned ourselves a 5-star review!
print(three_cheapest)
