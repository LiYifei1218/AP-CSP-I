def inventory():
    prices = {"banana":4, "apple":2, "orange":1.5, "pear":3}
    stock = {"banana":6, "apple":7, "orange":31, "pear":15}
    total = 0.0
    for item in prices.keys():
        total += (prices[item] * stock[item])
    return total

print(inventory())