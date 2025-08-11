
# Tuples are immutable
a = ('a', 20, "Apple" )

print(a)



# Tuples Methods



# Count

print(a.count(20))



# index

d = a.index(20)

print(d)


# Max Min
num =  (10, 5, 4, 3, 8, 15)
print(max(num))
print(min(num))



# Find
print(10 in num)
print(55 in num)


# Length

print(len(num))



# Slicing

print(num[0:4]) # after we use slicing it return new tuple


# Unpacking 

b, c, d, e, f, g = num

print(b, c, d, e, f, g)