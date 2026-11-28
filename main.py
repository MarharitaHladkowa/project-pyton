numbers = [1, 2, 2, 3, 4, 4, 4]
new_list = []
for index in (numbers):
         if numbers.count(index)>1 and index not in new_list:
                 new_list.append(index)
print (new_list)