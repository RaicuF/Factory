from auth import Auth
import position

client = Auth()
user, user_id = client.login()



print("Welcome to Factory Menu!")

if user:
    if user['position'] == 'manager':
        manager = position.Manager(user_id, user)
        manager.meniu()
    if user['position'] == 'Administrator':
        Administrator = position.Administrator(user_id, user)
        Administrator.menu2()
    if user['position'] == 'operator':
        print('operator')

print("Program closed...")




