
my_list = [10, 20, 30]
some_data = ["Python", 3.12]
my_list.extend(some_data)
print(my_list)  # [10, 20, 30, "Python", 3.12]
my_list.insert(1, "start")
print(my_list)  # [10, "start", 20, 30, "Python", 3.12]
my_list.reverse()
print(my_list)  # [3.12, "Python", 30, 20, "start", 10]