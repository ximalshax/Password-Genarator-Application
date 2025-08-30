import random

digits = "123456789"
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = lowercase.upper()
special_cha = "!@#$%&/"


def main_menu() -> str:
    print("1 - Generate Digits Only Key")
    print("2 - Generate Lowercase Letters Only Key")
    print("3 - Generate Uppercase Letters Only Key")
    print("4 - Generate Special Charactors Only Key")
    print("5 - Generate All Mix Key")


def error_massage(text: str) -> str:
    return f"Do Not Enter {text} ..."


def get_password_leght_int() -> input:
    while True:
        password_lenght = input("Enter Your Password Lenght : ")

        if password_lenght == "":
            print(error_massage("Space"))
            continue
        elif password_lenght.isdigit() == False:
            print(error_massage(password_lenght))
            continue
        else:
            password_lenght = int(password_lenght)
        
        if password_lenght > 50:
            print("Do Not Enter More Than Values of 50 ...")
            continue
        else:
            break

    return password_lenght


def generate_password(password_lenght: int, charactors: str) -> str:
    generated_psswd = []
    checker = None
    while len(generated_psswd) < password_lenght:
        generated_value = random.choice(charactors)

        if checker != generated_value:
            generated_psswd.append(generated_value)
            checker = generated_value

    return "".join(generated_psswd)


while True:
    main_menu()

    while True:
        user_choice = input("Enter Your Choice : ")

        if user_choice == "":
            print(error_massage("Space"))
            continue
        elif user_choice.isdigit() is False:
            print(error_massage(user_choice))
            continue
        else:
            user_choice = int(user_choice)

        if user_choice > 5:
            print(error_massage(user_choice))
            continue
        else:
            break

    if user_choice == 1:
        password_lenght = get_password_leght_int()
        psswd = generate_password(password_lenght,digits)
        print("Password Is : ",psswd)

    elif user_choice == 2:
        password_lenght = get_password_leght_int()
        psswd = generate_password(password_lenght,lowercase)
        print("Password Is : ",psswd)

    elif user_choice == 3:
        password_lenght = get_password_leght_int()
        psswd = generate_password(password_lenght,uppercase)
        print("Password Is : ",psswd)

    elif user_choice == 4:
        password_lenght = get_password_leght_int()
        psswd = generate_password(password_lenght,special_cha)
        print("Password Is : ",psswd)

    elif user_choice == 5:
        password_lenght = get_password_leght_int()
        generated_psswd = []

        while len(generated_psswd) < password_lenght:
            charactors_list = [digits, lowercase, uppercase, special_cha]
            psswd_list = random.choice(charactors_list)
            psswd = random.choice(psswd_list)

            if psswd not in generated_psswd:
                generated_psswd.append(psswd)

        print("Password Is : ","".join(generated_psswd))

    save_massage = input("Do You Want To Save This Password [y/n] : ")
    save_text = ["Y", "y", "YES", "yes"]

    if save_massage in save_text:
        with open("saved_password.txt", "w") as saved_file:
            saved_file.write(f"Your Passsword - {psswd}")
        print("Password Is Saved In txt File")

    continue_massage = input("Do You Want To Continue [y/n] : ")
    continue_text = ["Y", "y", "YES", "yes"]
    
    if continue_massage in continue_text:
        continue
    else:
        exit()