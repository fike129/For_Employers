using System;

namespace ConsoleApplication4
{
    public class Question
    {
        public string Name; // Вопрос
        public int Price; // Цена вопроса
        public bool Result; // Результат ответа
        private string[] AnArray; // Массив ответов
        private string An = String.Empty; // Выходная строка ответов
        private int rightAnswer; // Номер верного ответа  от 0
        private string sym = "abcd";
        public Question(string n, int p, int rihgt, params string[] a)
        {
            AnArray = new string[a.Length];
            a.CopyTo(AnArray, 0);
            rightAnswer = rihgt - 1;
            Name = n;
            Price = p;
        }

        public string GetAnswers()
        {
            string endStr = String.Empty;
            char[] endSym = new char[AnArray.Length];
            sym.CopyTo(0, endSym, 0, AnArray.Length);
            for (int i = 0; i < AnArray.Length; i++)
            {
                endStr += endSym[i] + "-" + AnArray[i] + " ";
            }
            return endStr;
        }

        public int SetAnswer(string s) // Возвращает цену вопроса в случае удачи, иначе - 0
        {
            int num = sym.IndexOf(s, StringComparison.Ordinal);
            if (num == rightAnswer) return Price;
            else return 0;

        }
    }
}
