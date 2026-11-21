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

my_list = [1, "Hello", 3.14]
my_list.append(4)
print(my_list)
my_list.remove("Hello")
print(my_list)
some_iterable = ["a", "b", "c"]
some_iterable[1] = -2
first_letter = some_iterable[-3]
middle_one = some_iterable[-2]
last_letter = some_iterable[-1]

print(f"Перша літера: {first_letter}")
print(f"Середня літера: {middle_one}")
print(f"Остання літера: {last_letter}")
chars = ['a', 'b', 'c']
numbers = [1, 2]
chars.extend(numbers)
print(chars)
chars = ["a", "c"]
chars.insert(1, "b")
print(chars)
chars = ['a', 'b']
chars.clear() 
print(chars)
chars = ['a', 'b', 'c', 'd']
c_ind = chars.index('c')
print(f"Індекс літери 'c': {c_ind}")
my_list = [1, 2, 3, 4, 2, 2, 5, 2]
count_2 = my_list.count(2)
print(count_2)  # Виведе 4, оскільки число 2 зустрічається 4 рази
