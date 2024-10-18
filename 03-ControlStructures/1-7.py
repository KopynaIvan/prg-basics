###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
total_salary = int(input('Write the number:'))
is_bonus = True # does the employee receive a bonus
bonus = 0.15 # 15%

if is_bonus:
    total_salary = (basic_salary * bonus) + basic_salary
else :
    basic_salary

print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {total_salary}')