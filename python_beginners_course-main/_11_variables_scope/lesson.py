var1 = "Out"


def my_function():

    global var1
    var1 = "In"
    # var1 = "In"
    # print(var1)


my_function()
print(var1)
