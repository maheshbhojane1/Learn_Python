
# It is unorderd
# It is mutable
# It is indexed
# can not contain duplicate keys

empty = {} # empty Dictionary

marks = {
    "Rohan": 45,
    "Abhi": 50,
    "Amit": 85,
}
print(marks, type(marks))



#  Methods of Dictionary



# clear() remove all items

print(marks.clear())


# copy() return all shallow copy

print(marks.copy())


# items() return list of (key, values) pair
print(marks.items())


# keys()

print((marks.keys()))


# pop() remove and returns values for key
marks.pop(key, default)


# popitems() remove and return last pair
print(marks.popitem("Rohan", 45))


# Values() return list view of values
print(marks.values())


# update() it add update the value in old key also add new key and value
marks.update({"Rohan": 99, "Ritik": 100})

print(marks)


# get() get the values from Dictionary

print(marks.get("Rohan"))
# Diff between 
print(marks.get("Rohan1"))
print(marks["Rohan1"])  # it is strick












