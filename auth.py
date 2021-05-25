import json




class Auth:
    users_file = open("users.json", "r")
    user_dict = json.load(users_file)
    def login(self):
        while True:
            user = input("User\n> ").lower()
            if user in self.user_dict:
                password = input("Pass:\n> ")
                if password == self.user_dict[user]["password"]:
                 print("Logged In")
                 return self.user_dict[user],user
                else:
                    print("Password incorrect")
            else:
                print("User not found")








