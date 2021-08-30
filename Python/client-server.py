from colorama import Fore, Style

# console colors
cred, green, blue, cyan, reset = Fore.RED, Fore.GREEN, Fore.BLUE, Fore.CYAN, Style.RESET_ALL

class Client:
    # simple login network
    def __init__(self, username=None, passcode=None):
        self.username = username
        self.passcode = passcode
        self.__userData = "/home/dhanush/Documents/Python/assets/user_data.txt"
        self.user_data = {}

        file = open(self.__userData, 'r')
        lines = file.readlines()
        file.close()

        for line in lines:
            user_id, pass_code = line.split(" ")
            self.user_data[user_id] = pass_code.strip("\n")

    def __isUser(self):
        user_data = open(self.__userData, 'r')
        data = user_data.readlines()
        user_data.close()

        if f"{self.username} {self.passcode}\n" in data:
            return True

        return False

    def register(self):
        if not self.__isUser() and self.isCorrectUser():
            for _ in range(3):
                re_pass = input("Re-enter password: ")

                if re_pass == self.passcode:
                    with open(self.__userData, 'a') as f:
                        f.write(f"{self.username} {self.passcode}\n")
                    print(f"\n{cyan}Registration successful{reset}")
                    break

                else:
                    print(f"{cred}Password won't match{reset}")

        else:
            print(f"\n{cred}You already registered please signIn{reset}")

    def isCorrectUser(self):
        conditions = [self.username.endswith("@gmail.com"),
                      len(self.username) >= 7 and len(self.passcode) >= 7]

        if all(conditions):
            return True

        return False

    def deleteAccount(self):
        if self.__isUser():
            warning = input(f"{cred}Delete Account {cyan}(y/n):{reset} ").lower()

            if warning == "y":
                f1 = open(self.__userData, 'r')
                c1 = f1.read()
                f1.close()

                c1 = c1.replace(f"{self.username} {self.passcode}\n", "")
                f2 = open(self.__userData, 'w')
                f2.write(c1)
                f2.close()

                print(f"{cyan}Your account successfully deleted{reset}")

            else:
                print(f"{cred}Account delete denied{reset}")

        else:
            print(f"{cred}No account found with USERNAME: {self.username} to delete{reset}")

    def signIn(self):
        import hashlib

        if self.__isUser():
            passcode = self.passcode.encode("utf-8")
            passcode = hashlib.md5(passcode).hexdigest()
            print(f"{green}>>> Sign-In Successful:\nUsername/Email ID : {self.username}\nPassword(HashCode): {passcode}{reset}")

        else:
            print(f"{cred}>>> Sign-In failed: May be due to"
                  f"\n\t- Incorrect Username/password"
                  f"\n\t- You have not registered{reset}")

    def __getUserData(self):
        return self.user_data

    def contactServer(self):
        print(f"{green}Contact Server: {blue}clientservice@gmail.com")
        print(f"{blue}\nM) Mail Report\nP) Reset password{reset}")
        op = input("Enter: ").upper()

        if op == "M":
            print(f"{blue}Mail report is under development, sorry for the inconvinience{reset}")

        else:
            email = input("Enter Email ID/Username: ")

            if email in self.user_data.keys():
                new_pass = input("Enter new password: ")
                self.username = email
                self.passcode = new_pass

                if self.isCorrectUser():
                    # password replacement
                    old_pass = f"{self.username} {self.user_data[self.username]}"
                    new_pass = f"{self.username} {new_pass}"

                    with open(self.__userData, 'r') as txt:
                        text = txt.read()
                        text = text.replace(old_pass, new_pass)

                    with open(self.__userData, 'w') as f:
                        f.write(text)

                    print(f"{cyan}>>> Password reset successful{reset}")

                else:
                    print(f"{cred}>>> Invalid Password (Week password){reset}")

            else:
                print(f"{cred}>>> No account is registered with {blue}{email}{reset}")

'''
class Server(Client):

    def __init__(self, username, passcode):
        super(Server, self).__init__()

    def serverAccess(self):
        pass
'''

if __name__ == "__main__":
    print(f"{cred}Note:{green} Enter {cred}'none'{green} for {blue}username & password{green} to {cred}reset password{reset}")
    user = input("Enter username: ")
    _pass = input("Enter password: ")

    c = Client(user, _pass)

    if c.isCorrectUser() or (user == "none" and _pass == "none"):
        print(f"{cyan}s) Sign-In\nr) Register\nd) Delete Account\nu) User Data\nc) Contact Server{reset}")
        login = input("Enter: ").lower()

        if login == "s":
            c.signIn()

        elif login == "r":
            c.register()

        elif login == "d":
            c.deleteAccount()

        elif login == "c":
            c.contactServer()

        elif login == "u":
            try:
                print(c.__getUserData())
                
            except:
                print(f"{blue}WARNING: {cred}Only admin has access to UserData{reset}")

        else:
            print(f"{cred}Invalid User Response{reset}")

    else:
        print(f"{cred}Incorrect Username/password{reset}")
