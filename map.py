prices = [
    ("Product1", 10),
    ("Product2", 20),
    ("Product3", 30)
]


# print(list(map(lambda item:item[1], prices)))

list_created = [item for item in prices if item[1] > 10]

# list comprehension is [expression for item in items ]
print(list_created)

print(list(filter(lambda item: item[1] > 10, prices)))

list1 = [1, 2, 3]
list2 = [10, 20, 30]

list3 = list(zip("abc", list1, list2))
print(list3)

print(list1)
