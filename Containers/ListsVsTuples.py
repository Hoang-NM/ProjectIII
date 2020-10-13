# List
list1 = [1996, 1997, 1998, 1999]
print('list1: ', list1)

list1Address = hex(id(list1))
print('Address of list1: ', list1Address)

print('\nAppend 2000 to list1')
list1.append(2000)
print('List1 (After append):', list1)
list1Address = hex(id(list1))
print('Address of list1 (After append): ', list1Address)

print('\n')

# Tuple
tuple1 = (1996, 1997, 1998, 1999)
print('tuple1: ', tuple1)

tuple1Address = hex(id(tuple1))
print('Address of tuple1: ', tuple1Address)

print('\nAdd 2000 to tuple1')
tuple1 = tuple1 + (2000, 2001)
print('tuple1 (After concat):', tuple1)
tuple1Address = hex(id(tuple1))
print('Address of tuple1 (After concat): ', tuple1Address)

# Tuples can be used as key in dictionaries and as elements of sets while lists cannot
d = {(x, x + 1): x for x in range(10)}
t = (5, 6)
print(type(t))
print(d[t])
print(d[(1, 2)])
