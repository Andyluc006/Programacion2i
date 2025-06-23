# Ejercicio 1
print("Ejercicio 1")
my_list_1 = ["apple", "banana", "cherry", "date", "elderberry"]
for index, element in enumerate(my_list_1):
    print(f"Element at index {index}: {element}")

# Ejercicio 2
print("\nEjercicio 2")
my_list_2 = ["red", "green", "blue", "yellow", "orange"]
for index, element in enumerate(my_list_2):
    print(f"Element at index {index}: {element}")

# Ejercicio 3
print("\nEjercicio 3")
my_list_3 = [10, 20, 30, 40, 50]
for index, element in enumerate(my_list_3):
    print(f"Element at index {index}: {element}")

# Ejercicio 4
print("\nEjercicio 4")
my_list_4 = ["cat", "dog", "bird", "fish", "rabbit"]
for index, element in enumerate(my_list_4):
    print(f"Element at index {index}: {element}")

# Ejercicio 5
print("\nEjercicio 5")
my_list_5 = ["mercury", "venus", "earth", "mars", "jupiter"]
for index, element in enumerate(my_list_5):
    print(f"Element at index {index}: {element}")

# Ejercicio 6
print("\nEjercicio 6")
my_list_6 = ["one", "two", "three", "four", "five"]
for index, element in enumerate(my_list_6):
    print(f"Element at index {index}: {element}")

# Ejercicio 7
print("\nEjercicio 7")
my_list_7 = [True, False, True, True, False]
for index, element in enumerate(my_list_7):
    print(f"Element at index {index}: {element}")

# Ejercicio 8
print("\nEjercicio 8")
my_list_8 = [0.1, 0.2, 0.3, 0.4, 0.5]
for index, element in enumerate(my_list_8):
    print(f"Element at index {index}: {element}")

# Ejercicio 9
print("\nEjercicio 9")
my_list_9 = ['A', 'B', 'C', 'D', 'E']
for index, element in enumerate(my_list_9):
    print(f"Element at index {index}: {element}")

# Ejercicio 10
print("\nEjercicio 10")
my_list_10 = ["alpha", "beta", "gamma", "delta", "epsilon"]
for index, element in enumerate(my_list_10):
    print(f"Element at index {index}: {element}")

# Ejercicio 11
print("\nEjercicio 11")
words_11 = []
while True:
    word = input("Enter a word (or 'done' to finish): ")
    if word.lower() == 'done':
        break
    words_11.append(word)

if words_11:
    longest_word = ""
    for word in words_11:
        if len(word) > len(longest_word):
            longest_word = word
    print(f"The longest word is: {longest_word}")
else:
    print("No words were entered.")

# Ejercicio 12
print("\nEjercicio 12")
words_12 = []
while True:
    word = input("Enter a word (or 'stop' to finish): ")
    if word.lower() == 'stop':
        break
    words_12.append(word)

if words_12:
    longest_word = ""
    for word in words_12:
        if len(word) > len(longest_word):
            longest_word = word
    print(f"The longest word is: {longest_word}")
else:
    print("No words were entered.")

# Ejercicio 13
print("\nEjercicio 13")
words_13 = []
while True:
    word = input("Enter a word (or 'fin' to finish): ")
    if word.lower() == 'fin':
        break
    words_13.append(word)

if words_13:
    longest_word = max(words_13, key=len)
    print(f"The longest word is: {longest_word}")
else:
    print("No words were entered.")

# Ejercicio 14
print("\nEjercicio 14")
words_14 = []
while True:
    word = input("Enter a word (or 'exit' to finish): ")
    if word.lower() == 'exit':
        break
    words_14.append(word)

if words_14:
    longest_word = ""
    for word in words_14:
        if len(word) > len(longest_word):
            longest_word = word
    print(f"The longest word is: {longest_word}")
else:
    print("No words were entered.")

# Ejercicio 15
print("\nEjercicio 15")
words_15 = []
while True:
    word = input("Enter a word (or 'done' to stop): ")
    if word.lower() == 'done':
        break
    words_15.append(word)

if words_15:
    longest_word = sorted(words_15, key=len, reverse=True)[0]
    print(f"The longest word is: {longest_word}")
else:
    print("No words were entered.")

# Ejercicio 16
print("\nEjercicio 16")
words_16 = []
while True:
    word = input("Enter a word (or 'quit' to finish): ")
    if word.lower() == 'quit':
        break
    words_16.append(word)

if words_16:
    longest_word = ""
    for word in words_16:
        if len(word) > len(longest_word):
            longest_word = word
    print(f"The longest word is: {longest_word}")
else:
    print("No words were entered.")

# Ejercicio 17
print("\nEjercicio 17")
words_17 = []
while True:
    word = input("Enter a word (or 'end' to finish): ")
    if word.lower() == 'end':
        break
    words_17.append(word)

if words_17:
    longest_word = max(words_17, key=len)
    print(f"The longest word is: {longest_word}")
else:
    print("No words were entered.")

# Ejercicio 18
print("\nEjercicio 18")
words_18 = []
while True:
    word = input("Enter a word (or 'finish' to stop): ")
    if word.lower() == 'finish':
        break
    words_18.append(word)

if words_18:
    longest_word = ""
    for word in words_18:
        if len(word) > len(longest_word):
            longest_word = word
    print(f"The longest word is: {longest_word}")
else:
    print("No words were entered.")

# Ejercicio 19
print("\nEjercicio 19")
words_19 = []
while True:
    word = input("Enter a word (or 'x' to finish): ")
    if word.lower() == 'x':
        break
    words_19.append(word)

if words_19:
    longest_word = ""
    for word in words_19:
        if len(word) > len(longest_word):
            longest_word = word
    print(f"The longest word is: {longest_word}")
else:
    print("No words were entered.")

# Ejercicio 20
print("\nEjercicio 20")
words_20 = []
while True:
    word = input("Enter a word (or 'done' to end): ")
    if word.lower() == 'done':
        break
    words_20.append(word)

if words_20:
    longest_word = max(words_20, key=len)
    print(f"The longest word is: {longest_word}")
else:
    print("No words were entered.")

# Ejercicio 21
print("\nEjercicio 21")
text_21 = input("Enter a line of text: ")
word_freq_21 = {}
words = text_21.lower().split()
for word in words:
    word_freq_21[word] = word_freq_21.get(word, 0) + 1
print("Word frequencies:", word_freq_21)

# Ejercicio 22
print("\nEjercicio 22")
text_22 = input("Enter a line of text: ")
word_freq_22 = {}
words = text_22.lower().split()
for word in words:
    word_freq_22[word] = word_freq_22.get(word, 0) + 1
print("Word frequencies:", word_freq_22)

# Ejercicio 23
print("\nEjercicio 23")
text_23 = input("Enter a line of text: ")
word_freq_23 = {}
words = text_23.lower().split()
for word in words:
    word_freq_23[word] = word_freq_23.get(word, 0) + 1
print("Word frequencies:", word_freq_23)

# Ejercicio 24
print("\nEjercicio 24")
text_24 = input("Enter a line of text: ")
word_freq_24 = {}
words = text_24.lower().split()
for word in words:
    word_freq_24[word] = word_freq_24.get(word, 0) + 1
print("Word frequencies:", word_freq_24)

# Ejercicio 25
print("\nEjercicio 25")
text_25 = input("Enter a line of text: ")
word_freq_25 = {}
words = text_25.lower().split()
for word in words:
    word_freq_25[word] = word_freq_25.get(word, 0) + 1
print("Word frequencies:", word_freq_25)

# Ejercicio 26
print("\nEjercicio 26")
text_26 = input("Enter a line of text: ")
word_freq_26 = {}
words = text_26.lower().split()
for word in words:
    word_freq_26[word] = word_freq_26.get(word, 0) + 1
print("Word frequencies:", word_freq_26)

# Ejercicio 27
print("\nEjercicio 27")
text_27 = input("Enter a line of text: ")
word_freq_27 = {}
words = text_27.lower().split()
for word in words:
    word_freq_27[word] = word_freq_27.get(word, 0) + 1
print("Word frequencies:", word_freq_27)

# Ejercicio 28
print("\nEjercicio 28")
text_28 = input("Enter a line of text: ")
word_freq_28 = {}
words = text_28.lower().split()
for word in words:
    word_freq_28[word] = word_freq_28.get(word, 0) + 1
print("Word frequencies:", word_freq_28)

# Ejercicio 29
print("\nEjercicio 29")
text_29 = input("Enter a line of text: ")
word_freq_29 = {}
words = text_29.lower().split()
for word in words:
    word_freq_29[word] = word_freq_29.get(word, 0) + 1
print("Word frequencies:", word_freq_29)

# Ejercicio 30
print("\nEjercicio 30")
text_30 = input("Enter a line of text: ")
word_freq_30 = {}
words = text_30.lower().split()
for word in words:
    word_freq_30[word] = word_freq_30.get(word, 0) + 1
print("Word frequencies:", word_freq_30)

# Ejercicio 31
print("\nEjercicio 31")
# Create a dummy datos.txt file for testing
with open("datos.txt", "w") as f:
    f.write("apple banana apple orange banana apple cherry")

word_freq_31 = {}
try:
    with open("datos.txt", "r") as file:
        content = file.read().lower()
        words = content.split()
        for word in words:
            word_freq_31[word] = word_freq_31.get(word, 0) + 1
    
    sorted_words = sorted(word_freq_31.items(), key=lambda item: item[1], reverse=True)
    print("Top 3 most repeated words:")
    for word, freq in sorted_words[:3]:
        print(f"{word}: {freq}")
except FileNotFoundError:
    print("Error: datos.txt not found.")

# Ejercicio 32
print("\nEjercicio 32")
# Create a dummy datos.txt file for testing
with open("datos.txt", "w") as f:
    f.write("the quick brown fox jumps over the lazy dog the dog")

word_freq_32 = {}
try:
    with open("datos.txt", "r") as file:
        content = file.read().lower()
        words = content.split()
        for word in words:
            word_freq_32[word] = word_freq_32.get(word, 0) + 1
    
    sorted_words = sorted(word_freq_32.items(), key=lambda item: item[1], reverse=True)
    print("Top 3 most repeated words:")
    for word, freq in sorted_words[:3]:
        print(f"{word}: {freq}")
except FileNotFoundError:
    print("Error: datos.txt not found.")

# Ejercicio 33
print("\nEjercicio 33")
# Create a dummy datos.txt file for testing
with open("datos.txt", "w") as f:
    f.write("python is a great language python is versatile python")

word_freq_33 = {}
try:
    with open("datos.txt", "r") as file:
        content = file.read().lower()
        words = content.split()
        for word in words:
            word_freq_33[word] = word_freq_33.get(word, 0) + 1
    
    sorted_words = sorted(word_freq_33.items(), key=lambda item: item[1], reverse=True)
    print("Top 3 most repeated words:")
    for word, freq in sorted_words[:3]:
        print(f"{word}: {freq}")
except FileNotFoundError:
    print("Error: datos.txt not found.")

# Ejercicio 34
print("\nEjercicio 34")
# Create a dummy datos.txt file for testing
with open("datos.txt", "w") as f:
    f.write("hello world hello python hello world")

word_freq_34 = {}
try:
    with open("datos.txt", "r") as file:
        content = file.read().lower()
        words = content.split()
        for word in words:
            word_freq_34[word] = word_freq_34.get(word, 0) + 1
    
    sorted_words = sorted(word_freq_34.items(), key=lambda item: item[1], reverse=True)
    print("Top 3 most repeated words:")
    for word, freq in sorted_words[:3]:
        print(f"{word}: {freq}")
except FileNotFoundError:
    print("Error: datos.txt not found.")

# Ejercicio 35
print("\nEjercicio 35")
# Create a dummy datos.txt file for testing
with open("datos.txt", "w") as f:
    f.write("data science machine learning data analysis data")

word_freq_35 = {}
try:
    with open("datos.txt", "r") as file:
        content = file.read().lower()
        words = content.split()
        for word in words:
            word_freq_35[word] = word_freq_35.get(word, 0) + 1
    
    sorted_words = sorted(word_freq_35.items(), key=lambda item: item[1], reverse=True)
    print("Top 3 most repeated words:")
    for word, freq in sorted_words[:3]:
        print(f"{word}: {freq}")
except FileNotFoundError:
    print("Error: datos.txt not found.")

# Ejercicio 36
print("\nEjercicio 36")
# Create a dummy datos.txt file for testing
with open("datos.txt", "w") as f:
    f.write("programming is fun programming with python is more fun")

word_freq_36 = {}
try:
    with open("datos.txt", "r") as file:
        content = file.read().lower()
        words = content.split()
        for word in words:
            word_freq_36[word] = word_freq_36.get(word, 0) + 1
    
    sorted_words = sorted(word_freq_36.items(), key=lambda item: item[1], reverse=True)
    print("Top 3 most repeated words:")
    for word, freq in sorted_words[:3]:
        print(f"{word}: {freq}")
except FileNotFoundError:
    print("Error: datos.txt not found.")

# Ejercicio 37
print("\nEjercicio 37")
# Create a dummy datos.txt file for testing
with open("datos.txt", "w") as f:
    f.write("software development is interesting development")

word_freq_37 = {}
try:
    with open("datos.txt", "r") as file:
        content = file.read().lower()
        words = content.split()
        for word in words:
            word_freq_37[word] = word_freq_37.get(word, 0) + 1
    
    sorted_words = sorted(word_freq_37.items(), key=lambda item: item[1], reverse=True)
    print("Top 3 most repeated words:")
    for word, freq in sorted_words[:3]:
        print(f"{word}: {freq}")
except FileNotFoundError:
    print("Error: datos.txt not found.")

# Ejercicio 38
print("\nEjercicio 38")
# Create a dummy datos.txt file for testing
with open("datos.txt", "w") as f:
    f.write("coding is a skill skill skill")

word_freq_38 = {}
try:
    with open("datos.txt", "r") as file:
        content = file.read().lower()
        words = content.split()
        for word in words:
            word_freq_38[word] = word_freq_38.get(word, 0) + 1
    
    sorted_words = sorted(word_freq_38.items(), key=lambda item: item[1], reverse=True)
    print("Top 3 most repeated words:")
    for word, freq in sorted_words[:3]:
        print(f"{word}: {freq}")
except FileNotFoundError:
    print("Error: datos.txt not found.")

# Ejercicio 39
print("\nEjercicio 39")
# Create a dummy datos.txt file for testing
with open("datos.txt", "w") as f:
    f.write("web development html css javascript web")

word_freq_39 = {}
try:
    with open("datos.txt", "r") as file:
        content = file.read().lower()
        words = content.split()
        for word in words:
            word_freq_39[word] = word_freq_39.get(word, 0) + 1
    
    sorted_words = sorted(word_freq_39.items(), key=lambda item: item[1], reverse=True)
    print("Top 3 most repeated words:")
    for word, freq in sorted_words[:3]:
        print(f"{word}: {freq}")
except FileNotFoundError:
    print("Error: datos.txt not found.")

# Ejercicio 40
print("\nEjercicio 40")
# Create a dummy datos.txt file for testing
with open("datos.txt", "w") as f:
    f.write("databases sql nosql databases")

word_freq_40 = {}
try:
    with open("datos.txt", "r") as file:
        content = file.read().lower()
        words = content.split()
        for word in words:
            word_freq_40[word] = word_freq_40.get(word, 0) + 1
    
    sorted_words = sorted(word_freq_40.items(), key=lambda item: item[1], reverse=True)
    print("Top 3 most repeated words:")
    for word, freq in sorted_words[:3]:
        print(f"{word}: {freq}")
except FileNotFoundError:
    print("Error: datos.txt not found.")

# Ejercicio 41
print("\nEjercicio 41")
products_41 = {
    "laptop": 1200,
    "mouse": 25,
    "keyboard": 75,
    "monitor": 300,
    "webcam": 50
}

print("Available products:")
for product, price in products_41.items():
    print(f"- {product.capitalize()}: ${price}")

search_query = input("Enter a product to search for: ").lower()
if search_query in products_41:
    print(f"{search_query.capitalize()} is available for ${products_41[search_query]}.")
else:
    print(f"Sorry, {search_query} is not found in our store.")

# Ejercicio 42
print("\nEjercicio 42")
products_42 = {
    "shirt": 20,
    "jeans": 50,
    "shoes": 80,
    "hat": 15
}

print("Available products:")
for product, price in products_42.items():
    print(f"- {product.capitalize()}: ${price}")

search_query = input("Enter a product to search for: ").lower()
if search_query in products_42:
    print(f"{search_query.capitalize()} is available for ${products_42[search_query]}.")
else:
    print(f"Sorry, {search_query} is not found in our store.")

# Ejercicio 43
print("\nEjercicio 43")
products_43 = {
    "book": 10,
    "pen": 2,
    "notebook": 5,
    "backpack": 40
}

print("Available products:")
for product, price in products_43.items():
    print(f"- {product.capitalize()}: ${price}")

search_query = input("Enter a product to search for: ").lower()
if search_query in products_43:
    print(f"{search_query.capitalize()} is available for ${products_43[search_query]}.")
else:
    print(f"Sorry, {search_query} is not found in our store.")

# Ejercicio 44
print("\nEjercicio 44")
products_44 = {
    "coffee maker": 70,
    "toaster": 35,
    "blender": 60,
    "microwave": 120
}

print("Available products:")
for product, price in products_44.items():
    print(f"- {product.capitalize()}: ${price}")

search_query = input("Enter a product to search for: ").lower()
if search_query in products_44:
    print(f"{search_query.capitalize()} is available for ${products_44[search_query]}.")
else:
    print(f"Sorry, {search_query} is not found in our store.")

# Ejercicio 45
print("\nEjercicio 45")
products_45 = {
    "guitar": 200,
    "piano": 500,
    "drums": 400,
    "microphone": 80
}

print("Available products:")
for product, price in products_45.items():
    print(f"- {product.capitalize()}: ${price}")

search_query = input("Enter a product to search for: ").lower()
if search_query in products_45:
    print(f"{search_query.capitalize()} is available for ${products_45[search_query]}.")
else:
    print(f"Sorry, {search_query} is not found in our store.")

# Ejercicio 46
print("\nEjercicio 46")
products_46 = {
    "football": 25,
    "basketball": 30,
    "tennis racket": 70,
    "yoga mat": 20
}

print("Available products:")
for product, price in products_46.items():
    print(f"- {product.capitalize()}: ${price}")

search_query = input("Enter a product to search for: ").lower()
if search_query in products_46:
    print(f"{search_query.capitalize()} is available for ${products_46[search_query]}.")
else:
    print(f"Sorry, {search_query} is not found in our store.")

# Ejercicio 47
print("\nEjercicio 47")
products_47 = {
    "smartphone": 800,
    "tablet": 400,
    "smartwatch": 200,
    "headphones": 150
}

print("Available products:")
for product, price in products_47.items():
    print(f"- {product.capitalize()}: ${price}")

search_query = input("Enter a product to search for: ").lower()
if search_query in products_47:
    print(f"{search_query.capitalize()} is available for ${products_47[search_query]}.")
else:
    print(f"Sorry, {search_query} is not found in our store.")

# Ejercicio 48
print("\nEjercicio 48")
products_48 = {
    "chair": 50,
    "table": 100,
    "lamp": 30,
    "shelf": 60
}

print("Available products:")
for product, price in products_48.items():
    print(f"- {product.capitalize()}: ${price}")

search_query = input("Enter a product to search for: ").lower()
if search_query in products_48:
    print(f"{search_query.capitalize()} is available for ${products_48[search_query]}.")
else:
    print(f"Sorry, {search_query} is not found in our store.")

# Ejercicio 49
print("\nEjercicio 49")
products_49 = {
    "camera": 500,
    "lens": 300,
    "tripod": 70,
    "drone": 700
}

print("Available products:")
for product, price in products_49.items():
    print(f"- {product.capitalize()}: ${price}")

search_query = input("Enter a product to search for: ").lower()
if search_query in products_49:
    print(f"{search_query.capitalize()} is available for ${products_49[search_query]}.")
else:
    print(f"Sorry, {search_query} is not found in our store.")

# Ejercicio 50
print("\nEjercicio 50")
products_50 = {
    "refrigerator": 800,
    "washing machine": 600,
    "oven": 500,
    "dishwasher": 450
}

print("Available products:")
for product, price in products_50.items():
    print(f"- {product.capitalize()}: ${price}")

search_query = input("Enter a product to search for: ").lower()
if search_query in products_50:
    print(f"{search_query.capitalize()} is available for ${products_50[search_query]}.")
else:
    print(f"Sorry, {search_query} is not found in our store.")
