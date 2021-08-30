using System;
using System.IO;
using System.Collections.Generic;

class Client
{
    // username and password of the users
    protected string username, passcode, userData;
    private static Dictionary<string, string> users;

    // Client constructor
    public Client(string username=null, string passcode=null)
    {
        this.username = username;
        this.passcode = passcode;
        this.userData = @"/home/dhanush/Documents/C#/LearnCS/user_data.txt";

        string[] lines = File.ReadAllLines(this.userData);
        users = new Dictionary<string, string>();

        foreach (string line in lines) 
        {
            string[] data = line.Split(" ");
            users.Add(data[0], data[1]);
        }
    }

    public bool IsCorrectUser()
    {
        bool isValid_id = this.username.EndsWith("@gmail.com") && (this.username.Length >= 7);
        bool isValid_pc = this.passcode.Length >= 7;

        if (isValid_id && isValid_pc)
        {
            return true;
        }

        return false;
    }


    protected bool IsUser()
    {
        bool nxt = (users.ContainsKey(this.username)) && (users[this.username] == this.passcode);

        if (IsCorrectUser() && nxt)
            return true;

        return false;
    }

    public void LogIn()
    {
        if (IsUser())
        {
            Console.WriteLine($">>> LogIn successful\nUsername: {this.username}\nPassword: {this.passcode}");
        }

        else
        {
            Console.WriteLine(">>> LogIn Failed - May be due to\n\t- Incorrect Username/password\n\t- Not Registered");
        }
    }

    public void Register()
    {
        if (!(IsUser())) {
            string re_pass;

            for (int i = 0; i < 3; i++)
            {
                Console.Write("\nRe-Enter password: ");
                re_pass = Console.ReadLine();

                if (this.passcode == re_pass) {
                    Console.WriteLine("\n>>> Registration successful");

                    File.AppendAllText(this.userData, $"{this.username} {this.passcode}\n");
                    break;
                }

                else {
                    Console.WriteLine(">>> Password won't match");
                }
            }
        }

        else {
            Console.WriteLine(">>> You already Registered, Please Login");
        }
    }

    public void ContactServer()
    {
        Console.WriteLine(">>> Contact Server: clientservice@gmail.com");
        Console.WriteLine("M) Send Mail\nP) Reset Password");
        Console.Write("Enter: ");
        string op = Console.ReadLine().ToUpper();

        if (op == "M")
        {
            Console.WriteLine("Main Service is under development, sorry for inconvinience");
        }

        else
        {
            string id, pass, old_pass, re_pass;

            Console.Write("Enter Email ID: ");
            id = Console.ReadLine();

            if (users.ContainsKey(id))
            {
                Console.Write("Enter new password: ");
                pass = Console.ReadLine();

                this.username = id;
                this.passcode = pass;

                if (IsCorrectUser())
                {
                    string text = File.ReadAllText(this.userData);
                    old_pass = $"{this.username} {users[id]}";
                    re_pass = $"{this.username} {this.passcode}";

                    text = text.Replace(old_pass, re_pass);
                    File.WriteAllText(this.userData, text);
                }

                else {
                    Console.WriteLine(">>> Invalid Password (Length >= 7)");
                }
            }
        }
    }
}
/*
class Server : Client
{
    private const string server_id = "serverid@gmail.com";
    private const string server_pc = "serverPC@12345";

    // sever constructor
    public Server(string username, string passcode)
    {
        base.username = username;
        base.passcode = passcode;

        if ((username == server_id) && (passcode == server_pc))
        {
            Console.WriteLine("Server Accessed the Client");
        }

        else
        {
            Console.WriteLine("Access to Client failed");
        }
    }

    // server has access to all Clients information
}
*/
namespace ClientServer
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            
            string user, pass, process;

            Console.Write("Email ID/Username: ");
            user = Console.ReadLine();

            Console.Write("Passcode/Password: ");
            pass = Console.ReadLine();
            
            Client c = new Client(user, pass);
            
            if (((user == "null") && (pass == "null")) || c.IsCorrectUser())
            {
                Console.WriteLine("\nL) LogIn\nR) Register\nC) Contact Server");
                Console.Write("Enter: ");
                process = Console.ReadLine().ToUpper();

                switch (process)
                {
                    case "L":
                        c.LogIn();
                        break;

                    case "R":
                        c.Register();
                        break;

                    case "C":
                        c.ContactServer();
                        break;

                    default:
                      Console.WriteLine("\n>>> Invalid Process");
                      break;
                }
            }

            else
            {
                Console.WriteLine(">>> Incorrect Username and password");
            }
            
        }
    }
}
