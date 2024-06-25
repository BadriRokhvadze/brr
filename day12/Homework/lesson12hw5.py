o = input("Please enter a desired operation : ")

o1 = int(input("Please enter the first number: "))
o2 = int(input("Please enter the second number: "))

if o == '+':
    print(o1 + o2)
elif o == '*':
    print(o1 * o2)
elif o == '-':
    print(o1 - o2)
elif o == '/':
    print(o1 / o2)
else:
    print('Invalid Operation.')