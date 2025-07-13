prices = ["$120", "$340", "$50", "$90"]
prices_cleaned = list(map(lambda x: x.replace("$", ""), prices))
print(prices_cleaned)