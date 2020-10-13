# Create a new dictionary
d = {'cat': 'cute', 'dog': 'furry'}

# Get the value of key 'cat'
print(d['cat'])

# Check if dictionary have the given key - return boolean
print('cat' in d)

# Set an entry in a dictionary
d['fish'] = 'wet'
print(d['fish'])

print(d.get('monkey', 'N/A'))  # Get an element with a default value
print(d.get('fish', 'N/A'))
del d['fish']  # Remove an element
print(d.get('fish', 'N/A'))
