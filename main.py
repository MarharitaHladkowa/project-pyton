text = input("Введи строку: ")
count = 0

for char in text:
    if char == "a" or char == "A":
        count += 1

print(count)
