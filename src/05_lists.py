# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE 
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE 
for num in y: #<-- colon != '=' ?
    x.append(num)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE 
x.remove(8)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE 

#Awwww thought this would work
# for num in x:
#     print(num)
#     if num == 9:
#         break
#         x.append(99)
x.insert(5, 99)

print(x)

# Print the length of list x
# YOUR CODE HERE 
print(len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
for i in x:    
    print(i * 1000)