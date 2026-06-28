prices = [10_000, 20, 3_000, 3, -200, 1_000]
# price1 = prices[0]
# price2 = prices[2]
# price3 = prices[-1]
#
# # TODO: Print the first, third, and last item
# print(f"Current Price: {price1}")
# print(f"Current Price: {price2}")
# print(f"Current Price: {price3}")

indices = [0, 2, -1]
for index in indices:
    print(f"Current Price: {prices[index]}")

for index in indices:
    prices[index] = prices[index] // 2
    print(f"New Price: {prices[index]}")
