x = object()
y = object()

# Making X list = 10X
x_list = [x] * 10

# Making Y list = 10Y
y_list = [y] * 10

# Making big list = Y list and X list
big_list = x_list + y_list

# Printing the list values
print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# Testing to see if code is right
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")