N = int(input('Type a number: '))

for i in range(1, N):
    if i % 15 == 0:
        i = 'FizzBuzz'
    
    elif i % 3 == 0:
        i = 'Fizz'
    
    elif i % 5 == 0:
        i = 'Buzz'
    
    print(i)
