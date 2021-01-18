a = [1, 2, 3]
b = a # Apuntan a la misma memoria
c = [a, b]

a.append(5)
print(c)

print(id(a))
print(id(b))



a = [1, 2, 3]
b = a
c = list(a) # Clona la lista
d = a[::] # Clona la lista




# List Comprehension
my_list = list(range(100))
double = [ i * 2 for i in my_list ]
pares = [i for i in my_list if i % 2 == 0]