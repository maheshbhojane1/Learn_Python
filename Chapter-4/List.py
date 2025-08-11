# List are the container to store a set of values of any data types
# List are mutable
# if we perform any operation on list that case the originl list is change 
# in string the original string was not change they create new string



group = ["apple", "Orange", 22, True, "Rohan"]

print(group[0])

group[0] = "Mango"

print(group[0])




# Methods of lists


# Appends

group.append("Mahesh")



# Sort

num = [5, 4, 3, 7, 9, 10, 2]
num.sort()



# Reverse

num.reverse()



# insert

group.insert(0, "Banana")

print(group)

# pop

group.pop(0) # it return the result

# remove

group.remove(0)