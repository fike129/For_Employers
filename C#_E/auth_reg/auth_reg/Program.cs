using System;
using System.IO;

namespace auth_reg
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Title = "Create a new user";
            Console.WriteLine("Now we create a new user");
            string username, password = string.Empty;

            Console.WriteLine("Enter a user name");
            username = Console.ReadLine();
            Console.WriteLine("Enter a new password");
            password = Console.ReadLine();

            using (StreamWriter sw = new StreamWriter(File.Create("D:\\data.txt")))
            {
                sw.WriteLine(username);
                sw.WriteLine(password);
                sw.Close();
            }
            Console.WriteLine("Done!");

            Console.Read();

        }
    }
}
