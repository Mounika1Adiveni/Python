# 1. When no start index is provided, the interpreter prints all the values from start up to the end index provided.
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[:9])

# 2. Print every 3rd consecutive element within a given range.
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[::3])

# 3. Print list items in given ranges [3:7] (positive indexes) and [-7:-2] (negative indexes).
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])
print(animals[-7:-2])

# 5. If you are given a list of characters, how would you convert it into a string?
list1 = ["h", "e", "l", "l", "o"]
result = "".join(list1)
print(result)

# 7. If you are provided with a comma-separated list, how would you convert it into a list?
fruits = "apple,banana,orange"
result = fruits.split(",")
print(result)

# 9. How to calculate the size of a Python list?
list2=[1,2,3,4,5,6,7,8,9,10]
print(len(list2))

# 12. How to identify the first matching element by its index?
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[1])


