fruits = ['Apple', 'Banana', 'pomogranet']
for f in fruits[:]:
    if len(f) < 6:
        fruits.insert(2,f)
print fruits
