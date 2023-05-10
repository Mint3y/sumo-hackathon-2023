# In Python, everything that comes after a '#' is a comment

we_can_declare_variables_by_using_the_equals_operator = 5

we_can_overwrite_variables_by_using_it_again = 0
we_can_declare_variables_by_using_the_equals_operator = 3

# Variable names cannot contain spaces or special characters '$', '*', etc
# Variable names cannot start with numbers or special characters
# Variables can be used on the right side of an operator
foo = 5
bar = foo

# There are different 'type's of variables in Python
an_integer = 5
a_floating_point_value = 5.0 # (a 'real' number)
# There's complex number
a_list = []
a_list.append(5)
a_list.append(5)
a_list.append(5)
a_list.append(5)
a_list.append(5)

print(foo)
print("Hello World")
print("Hello", "World")

print("Hello", foo)


a = 5

def function_name(name_of_arg1, a):
    print(a)
    return name_of_arg1 + a

b = function_name(a + 6, 7)
c = function_name(3, a)

# [inputs] -> [function] -> [output]

"This is also a comment."

"""
this is a multiline string
also a comment
"""



"""
Python:
Variable length
Any type
Indexes start from 0

a_list = []
a_list.append(5)
a_list.append("Hello World")

a_list[1]

C:
Fixed length
Same type
Indexes start from 0

int array[5] = {0, 6, 2, 3, 3};

int b = array[1];
"""