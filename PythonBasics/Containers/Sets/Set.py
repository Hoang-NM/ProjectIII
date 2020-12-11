animals = {'cat', 'dog', 'bird'}

print('cat' in animals)  # Check if an element is in a set
print('fish' in animals)

animals.add('fish')
print('fish' in animals)

print(len(animals))  # Number of elements in a set

animals.add('cat')  # Add an element that already in the set does nothing
print(len(animals))

animals.remove('cat')
print(len(animals))
