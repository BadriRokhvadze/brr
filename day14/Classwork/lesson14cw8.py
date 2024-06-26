o = []

counter = 0

for i in range(5):
    name = input('Please enter a desired name: ')
    o.append(name)
    if name == 'luka':
        counter = counter + 1

print('This is how many times name luka was mentioned: ')
print(counter,'times')