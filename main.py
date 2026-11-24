number = 18
if number % 2 == 0 and number % 9 == 0:
    print("FizzBuzz")
elif number % 2 == 0:
    print("Fizz")
elif number % 9 == 0:
    print("Buzz")
else:
    print(number)