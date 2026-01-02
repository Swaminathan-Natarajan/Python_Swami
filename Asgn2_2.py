a = 10
b = 10
print(a)
print(b)
print(id(a)) #as this is immutable the memory will be shared, so same memory id will be displayed
print(id(b)) #as this is immutable the memory will be shared,so same memory id will be displayed

a = [10]
b = [10]
print(a)
print(b)
print(id(a)) #as list is mutable, new memory will be allocated for each value.
print(id(b)) #as list is mutable, new memory will be allocated for each value.
