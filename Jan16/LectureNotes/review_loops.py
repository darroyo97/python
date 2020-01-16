# for x in range(3):
#     for i in range(3):
#         print(x)


# for x in range(1, 11):
#     for i in range(1, 11):
#         m = x * i
#         print(f'{x} X {i} = {m}')


list1 = ["Week One", "Week Two", "Week Three", "Week Four", "Week Five "]
list2 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
list3 = ["Lecture", "Exercises"]
for x in list1:
    print(x)
    for i in list2:
        print(f' \v {i}')
        for y in list3:
            print(f' \t  {y}')
