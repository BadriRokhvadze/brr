o = int(input('Please enter your age: '))

while o == 18:
    o = int(input('Your age is invalid please try again: '))
if o < 18:
    print('Youre too young')
if o > 18:
    print('Youre old enough to enter welcome')