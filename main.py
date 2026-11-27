cities = ["Москва", "Казань", "Тула"]
temperatures = [5, 12, 8]
for x, y in zip(cities, temperatures):
    print(f"В городе {x} температура {y}°C")