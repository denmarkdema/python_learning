from python_lerning import restrict_access

# a = restrict_access.student.__name
b = restrict_access.student('dema',123)
# print(a)
print(b.get_age())
