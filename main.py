print("Hello, World!")
print("This is a Python script.")
s1 = 'Hello'
s2 = 'Margo!'
joined_string = f"{s1} {s2}"  # Hello Margo!
print(joined_string)
age = 18
is_adult = age > 18
print(is_adult)
name = "Oleg"
hello_string = f"Hello, {name}!"
print(hello_string)
ratio = 10  # коефіцієнт корекції
result = 8 * (ratio + 5) - ratio ** 2
print(result)
x = 10
print(f"Значення x: {x}")
# Встановлюємо ціни на продукти
price_per_croissant = 1.04
price_per_glass = 0.34
price_per_coffee_pack = 4.42

# Кількість кожного продукту
num_croissants = int(input("Введіть кількість круасанів: "))
num_glasses = int(input("Введіть кількість склянок: "))
num_coffee_packs = int(input("Введіть кількість упаковок кави: "))

# Обчислення загальної вартості
total_cost = num_croissants * price_per_croissant + \
             num_glasses * price_per_glass + \
             num_coffee_packs * price_per_coffee_pack

# Визначаємо кількість повних доларів і центів
total_dollars = int(total_cost)
total_cents = int(total_cost * 100)

# Вивід результату
print(f"Загальна вартість у повних доларах: {total_dollars} доларів")
print(f"Загальна вартість у центах: {total_cents} центів")
my_list = [1, "Hello", 3.14]
my_list.append(4)
print(my_list)
my_list.remove("Hello")
print(my_list)