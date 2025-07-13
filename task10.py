text = ["apple", "34", "banana", "100", "abc", "75"]
only_digits = list(filter(lambda x: x.isdigit(), text))
print(only_digits)