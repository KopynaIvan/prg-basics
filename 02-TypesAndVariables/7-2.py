#university, peter123, (passwords ok) seven, anna333 (passwords to short)
password = 'seven'
password_ok = len(password) >= 8
print(f'Password length is valid: {password_ok}')
password = 'peter123'
password_ok = len(password) >= 8
print(f'Password length is valid: {password_ok}')