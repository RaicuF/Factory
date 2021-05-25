import json
# import getpass


class Employer:
    def __init__(self,user_id, user):
        self.user_id = user_id
        self.user = user




class Manager(Employer):
    def __init__(self,user_id, user):
        super().__init__(user_id, user)
        print("Logged as <Manager>")

    def add_operator(self):
        name = input('Name\n > ')
        last_name = input('Last name\n >')
        position = 'Position'
        CNP = input('CNP\n> ')
        phone = input('Phone\n >')
        city = input('city\n >')
        skills = input(" Choose one option from skills>> F(frigotehnist), E(electrician) ,S(Welder)\n ").upper().split(",")
        user_id = last_name[0] + name
        password = "123"
        user_id = f"{last_name[0]}{name}".lower()
        user_file = open("users.json", 'r')
        user_dict = json.loads(user_file.read())
        user_file.close()

        user_dict[user_id] = {
            'password': password,
            "name": name,
            "last name": last_name,
            "position": position,
            "CNP": CNP,
            "phone number": phone,
            "city": city,
            "skills": skills
        }
        user_file = open("user.json", 'w')
        user_file.write(json.dumps(user_dict,indent=4))
        user_file.close()
        print(f"User {user_id} has been added.")


    def delete_operator(self):
        user_file = open("users.json", 'r')
        user_dict = json.loads(user_file.read())
        user_file.close()
        for user in user_dict:
            if user_dict[user]['position'] == 'manager':
                pass
            else:
                print(user)

        while True:
            user_to_delete = input("User\n").lower()
            try:
                user_dict.pop(user_to_delete)
                user_file = open("users.json", "w")
                user_file.write(json.dumps(user_dict,indent=4))
                user_file.close()
                print(f"User {user_to_delete} deleted successfull")
                return True
            except:
                print("User does not exist")
                continue


    def modify_skills(self):
        user_file = open("users.json", "r")
        user_dict = json.loads(user_file.read())
        user_file.close()
        while True:
            for user in user_dict:
                if user_dict[user]['position'] == "operator":
                    print(user)

            user_to_change = input("User >")
            if user_to_change in user_dict:
                skills = user_dict[user_to_change]["skills"]
                for skill in skills:
                    print(skill)
                new_skill = input("Write your skills separate").upper()
                user_dict[user_to_change]['skills'] = new_skill
                user_file = open("users.json", "w")
                user_file.write(json.dumps(user_dict,indent=4))
                user_file.close()
                print("Skills changed")
                return True
            elif user_to_change == "exit":
                 return False
            else:
                print("Wrong user")
                continue

    def meniu(self):
        menu_list = ['1. Add operator', '2.Delete operator','3.Modify Skills','4.Exit']
        while True:
            for opt in menu_list:
                print(opt)
            opt = int(input("\nOption >> "))
            if opt > 4:
                print('Option d.ont exist')
                continue
            elif opt == 1:
                self.add_operator()
            elif opt == 2:
                self.delete_operator()
            elif opt == 3:
                self.modify_skills()
            elif opt == 4:
                return False


class Administrator(Employer):
    def __init__(self,user_id, user):
        super().__init__(user_id,user)
        print("Logged as <Administrator>")

    def menu2(self):
        opt_list = ["1. Show materials",
                    "2. Add materials",
                    "3. See statistics",
                    "4. Exit"
                    ]
        while True:
            for opt in opt_list:
                print(opt)
            option = input("Option\n> ")
            if option == "1":
                file_materials = open("materials.json", "r")
                dict_materials = json.loads(file_materials.read())
                file_materials.close()
                print(50* '-')
                for materie in dict_materials:
                    print(f"{materie} > {dict_materials[materie]}")
                print(50* '-')
                continue
            elif option == '2':
                file_materials = open("materials.json", "r")
                dict_materials = json.loads(file_materials.read())
                materii = []
                for materie in dict_materials:
                    materii.append(materie)
                    print(50* '-')
                mat_change = input("Chose materies: \n> ").lower()
                if mat_change not in dict_materials:
                    print("Materials d.ont exist!")
                    continue


                stock = int(input("Stock\n >"))
                file_materials = open("materials.json", "w")
                new_materials = json.loads(file_materials.read())
                new_materials[mat_change] = dict_materials[mat_change] + stock
                file_materials.write(json.dumps(new_materials,indent=4))




class Operator(Employer):
    pass