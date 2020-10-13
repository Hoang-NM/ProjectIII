fruits = ('apple', 'mango', 'banana', 'orange', 'coconut', 'lemon')

for fruit in fruits:
    print('Fruit: ', fruit)

print('Element count: ', len(fruits))

for i in range(0, len(fruits)):
    print(f'Element at {i} = {fruits[i]}')

# Sub tuple
subTuple = fruits[1:4]
print('Sub tuple[1:4]: ', subTuple)

print('fruits[-1]: ', fruits[-1])

subTuple1 = fruits[-4:]
print('\n Sub Tuple fruits[-4:]: ', subTuple1)

subTuple2 = fruits[-4:-2]
print('\n Sub Tuple fruits[-4:-2]: ', subTuple2)