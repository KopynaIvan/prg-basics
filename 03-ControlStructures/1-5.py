total_tasks = 20*0.5
tasks_ok = int(input('Print your tasks'))
test_passed = False

if tasks_ok >= total_tasks :
    test_passed = True

if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')