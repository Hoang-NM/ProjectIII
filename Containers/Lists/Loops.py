animals = ['cat', 'dog', 'hamster', 'bird']
for animal in animals:
    print(animal)

for i, animal in enumerate(animals):
    print('#%d: %s' % (i + 1, animal))
