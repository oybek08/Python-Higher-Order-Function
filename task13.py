sentence = "Functional programming in Python is very powerful and elegant"
words = sentence.split()
top3 = sorted(words, key=lambda x: len(x), reverse=True)[:3]
print(top3)