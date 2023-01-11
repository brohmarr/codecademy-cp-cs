# Project: Carly's Clippers
# by: @Brohmarr

# You are the Data Analyst at Carly’s Clippers, the newest hair salon on
#     the block. Your job is to go through the lists of data that have
#     been collected in the past couple of weeks. You will be
#     calculating some important metrics that Carly can use to plan out
#     the operation of the business for the rest of the month.


# Names of the cuts offered at Carly’s Clippers.
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob",
              "mohawk", "flattop"]

# Prices of each hairstyle.
prices = [30, 25, 40, 20, 20, 35, 50, 35]

# Number of purchases for each hairstyle in the last week.
purchases_last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Carly wants to be able to market her low prices. Let's calculate the
#     average price of a haircut.
total_price = 0

for price in prices:
  total_price += price

average_price = (total_price / len(prices))

# Displaying the average price.
print("Average Haircut Price: $", average_price)

# Carly thought the average price would be lower. Now she wants to cut
#     all prices by 5 dollars.
new_prices = [price - 5 for price in prices]

# Displaying the new prices.
print(new_prices)

# Carly wants to know how much revenue was brought in last week.
total_revenue = 0

for i in range(0, len(hairstyles)):
  total_revenue += prices[i] * purchases_last_week[i]

print("Total Revenue: $", total_revenue)

# Carly also wants to know the average daily revenue.
average_daily_revenue = total_revenue / 7

print(average_daily_revenue)

# Carly thinks she can bring in more customers by advertising all of the
#     haircuts she has that are under $ 30. Let's gather them!
cuts_under_30 = [hairstyles[i] for i in range(0, len(hairstyles)) if 
                 new_prices[i] < 30]

print(cuts_under_30)
