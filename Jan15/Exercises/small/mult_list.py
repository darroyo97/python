list1 = [7, 4, 3]
list2 = [9, 4, 7]

new_list = []

for i in range(len(list1)):
    new_number = list1[i] * list2[i]
    new_list.append(new_number)

# print outside the loop
print(new_list)
