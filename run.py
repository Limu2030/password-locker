#!/usr/bin/env python3
from user import User
from credentials import Credentials

def create_user(username, password):
    new_user = User(username, password)
    return new_user


def save_user(user):
    user.save_User()


def delete_user(user):
    return User.delete_User(user)


def user_exist(user):
    return User.find_by_username(user)


def create_credentials(appname, appusername, apppassword):
    new_credentials = Credentials(appname, appusername, apppassword)
    return new_credentials


def save_credentials(credential):
    credential.save_Credentials()


def del_credentials(platform):
    return Credentials.delete_Credentials(platform)


def find_credential(platform):
    return Credentials.find_by_appname(platform)


def check_credentials(platform):
    return Credentials.credentials_exists(platform) 


def display_credentials():
    return Credentials.display_credentials()


def main():
    print("Welcome to Password Locker. Enter your name to proceed: ")
    user_name = input()

    print(f"Hello {user_name}. Here in Password Locker we store your passwords credentials for you")
    print("--------------------------------------------------------------------------------------------- ")

    while True: 
        print("Use short codes : l - to login, s - to sign-up, x - to exit")

        short_code1 = input().lower()
        if short_code1 == "s":
            print("sign-up")
            print("-----------------------------------------------------------------------------------------")
            print("Enter prefered username ......")
            u_name = input()

            print("Enter prefered password")
            password = input()


            save_user(create_user(u_name, password))

            print("\n")
            print(f"New user {u_name} has been created successfully")
            print("--------------------------------------------------------------------------------------------")
            print("Login to proceed......")
            print("\n")
            
            
        elif short_code1 == "l":
            print("login")
            print("----------------------------------------------------------------------------------------------")
            print('Enter username:')
            user_name_input = input()
            print("Enter password")
            user_password = input()

            if user_exist(user_name_input):
                print("User found......Logging in")

                print("\n")
                while True:
                    print("Welcome to your dashboard")
                    print("\n")
                    print("Use the following shortcodes: c - create credential, d - display credentials, f - find credential, del - delete credential, x - exit")
                    short_code2 = input().lower()
                    if short_code2 == "c":
                        print("store new password")
                        print("------------------------------")
                        print("Enter application name:")
                        app_name = input().lower()
                        print("Enter your application username:")
                        app_username = input()
                        print("Enter application password:")
                        app_password = input()
                        save_credentials(create_credentials(app_name, app_username, app_password))
                        print("\n")
                        print(f"New {app_name} password details have been saved successfully")
                        print("\n")


                    elif short_code2 == "d":
                        if display_credentials():
                            print(" This are your current credentials")
                            print("-------------------------------------")

                            for credential in display_credentials():
                                print (f"{credential.appname}.....{credential.appusername}.......{credential.apppassword}")
                                print("\n")
                        else: 
                            print("\n")
                            print("Sorry no credentials found")
                            print("\n")
                    elif short_code2 == "f":
                        print("Enter application name to find stored credentials")
                        search_app = input().lower()
                        if check_credentials(search_app):
                            found_app = find_credential(search_app)
                            print(f"{found_app.appname} has been found")
                            print("------------------")
                            print(f"username .......{found_app.appusername}")
                            print(f"password .......{found_app.apppassword}")
                        else:
                            print("Sorry that application was not found")    
                    elif short_code2 == "del":
                        print("Enter the application to delele its stored credentials:")
                        deleted = input()   
                        del_credentials(deleted)
                        print("Details deleted successfully")
                    elif short_code2 == "x":
                        print("Goodbye....")
                        break
                    else:
                        print("please use the short codes")


            else:
                print("Username does not exist please sign-up or enter the correct username")


        elif short_code1 == "x":
            print("Good bye...")
            break
        
        else : 
            print("kindly use the shortcodes provided")

















if __name__ == "__main__":
    main()
