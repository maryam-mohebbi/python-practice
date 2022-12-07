from getpass import getpass

username = input('Username: ')
password = getpass('Password:')
password_lenght = len(password)
hidden_password = '*'*password_lenght
print(f'{username}, Your password {hidden_password} is {password_lenght} letter long')
