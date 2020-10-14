d = {'people': 2, 'cats': 4, 'dogs': 2, 'hamsters': 6}

for animal in d:
    quantity = d[animal]
    print('The family have %d %s' % (d[animal], animal))

# Access to key & value of a dictionary
for animal, quantity in d.items():
    print(f'The family have {d[animal]} {animal}')  # Formatted String
