using System;
using System.IO;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            string username, password, username1, password1 = string.Empty;
            Console.WriteLine("Enter a username: ");
            username = Console.ReadLine();
            Console.WriteLine("Enter a password: ");
            password = Console.ReadLine();

            using (StreamReader sr = new StreamReader (File.Open("D:\\data.txt", FileMode.Open)))
            {
                username1 = sr.ReadLine();
                password1 = sr.ReadLine();
                sr.Close();
            }
            if (username == username1 && password == password1)
            {
                Console.WriteLine("Login successful");
            }
            else
            {
                Console.WriteLine("Login Failed");
            }
            Console.Read();
        }
    }
}
