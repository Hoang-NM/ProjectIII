months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
print('Months:', months)

# Reverse the list
print('\n - Reverse the list')
months.reverse()
print('Months (After reverse):', months)

# Extend the list
ext_month = ('Oct', 'Nov', 'Dec')
print('\n - Extend:')
months.extend(ext_month)
print('Months (After extends:', months)

print('\n - Append:')
months.append('Jun')
print('Months (After appends:', months)

print('\n - Remove Dec:')
months.remove('Dec')
print('Months (After remove:', months)

# Remove the last element
print('\n - months.pop():')
last_element = months.pop()
print('Last element:', last_element)

# Count
print('months.count(Jun)', months.count('Jun'))
