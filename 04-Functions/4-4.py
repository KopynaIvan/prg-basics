def sum_digits(any_number):
    str1 = str(abs(any_number))
    number = 0 
    for a in str1:
        number = int(a) + number
        
    return number

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number  is {result}')