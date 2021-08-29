from colorama import Fore, Style


class Client:

    def __init__(self, username, passcode):
        self.username = username
        self.passcode = passcode
        self.userData = "/home/dhanush/Documents/Python/assets/user_data.txt"

    def isUser(self):
        user_data = open(self.userData, 'r')
        data = user_data.readlines()
        user_data.close()

        if f"{self.username} {self.passcode}\n" in data:
            return True

        return False

    def register(self):
        if not self.isUser():
            f = open(self.userData, 'a')
            f.write(f"{self.username} {self.passcode}\n")
            f.close()

            for _ in range(3):
                re_pass = input("Re-enter password: ")

                if re_pass == self.passcode:
                    print(f"\n{Fore.CYAN}Registration successful{Style.RESET_ALL}")
                    break

                else:
                    print(f"{Fore.RED}Password won't match{Style.RESET_ALL}")

        else:
            print(f"\n{Fore.RED}You already registered please signIn{Style.RESET_ALL}")

    def isCorrectUser(self):
        conditions = [self.username.endswith("@gmail.com"),
                      len(self.username) >= 7 and len(self.passcode) >= 7]

        if all(conditions):
            return True

        return False

    def deleteAccount(self):
        if self.isUser():
            warning = input(f"{Fore.RED}Delete Account {Fore.CYAN}(y/n):{Style.RESET_ALL} ").lower()

            if warning == "y":
                f1 = open(self.userData, 'r')
                c1 = f1.read()
                f1.close()

                c1 = c1.replace(f"{self.username} {self.passcode}\n", "")
                f2 = open(self.userData, 'w')
                f2.write(c1)
                f2.close()

                print(f"{Fore.CYAN}Your account successfully deleted{Style.RESET_ALL}")

            else:
                print(f"{Fore.GREEN}Account delete denied{Style.RESET_ALL}")

        else:
            print(f"{Fore.RED}No account found with USERNAME: {self.username} to delete{Style.RESET_ALL}")

    def signIn(self):
        import hashlib

        if self.isUser():
            passcode = self.passcode.encode("utf-8")
            passcode = hashlib.md5(passcode).hexdigest()
            print(f"{Fore.GREEN}>>> Sign-In Successful:\nUsername/Email ID : {self.username}\nPassword(HashCode): {passcode}{Fore.RESET}")

        else:
            print(f"{Fore.RED}>>> Sign-In failed: May be due to"
                  f"\n\t- Incorrect Username/password"
                  f"\n\t- You have not registered{Fore.RESET}")

    def getUserData(self):
        file = open(self.userData, 'r')
        lines = file.readlines()
        file.close()

        user_data = {}

        for line in lines:
            user_id, pass_code = line.split(" ")
            user_data[user_id] = pass_code.strip("\n")

        return user_data


if __name__ == "__main__":
    user = input("Enter username: ")
    _pass = input("Enter password: ")

    c = Client(user, _pass)

    if c.isCorrectUser():
        print(f"{Fore.CYAN}s) Sign-In\nr) Register\nd) Delete Account\nu) User Data\n{Fore.RESET}")
        login = input("Enter: ").lower()

        if login == "s":
            c.signIn()

        elif login == "r":
            c.register()

        elif login == "d":
            c.deleteAccount()

        elif login == "u":
            print(c.getUserData())

        else:
            print(f"{Fore.RED}Invalid User Response{Style.RESET_ALL}")

    else:
        print(f"{Fore.RED}Incorrect Username/password{Style.RESET_ALL}")
