using System;
using System.Collections.Generic;
using System;

namespace ConsoleApplication4
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            new Game().Init();
            Console.ForegroundColor = ConsoleColor.Yellow;

            Console.WriteLine("Игра окончена, дорогой друг!");
            NewMethod();
            Console.ReadKey();
        }


        private static void NewMethod()
        {
            Console.WriteLine("Нажмите ENTER для выхода");
        }
    }
}
