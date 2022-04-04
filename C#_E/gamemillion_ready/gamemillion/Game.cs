using System;
using System.Collections.Generic;
using System.Linq;

namespace ConsoleApplication4
{
    public class Game
    {
        protected int _count = 0;
        List<Question> _questions = new List<Question>(); // Коллекция вопросов

        public void Init()
        {
            Console.ForegroundColor = ConsoleColor.Cyan;
            Console.WriteLine($"\n ДОБРО ПОЖАЛОВАТЬ В ИГРУ 'КТО ХОЧЕТ СТАТЬ МИЛЛИОНЕРОМ' !!! \n");
            Console.WriteLine($"\n Нажмите ENTER чтобы продолжить \n");
            Console.ReadKey();
            Console.WriteLine($"\n Выбирать правильный ответ можно с помощью буквы  \n");
            _questions.Add(new Question("Сколько ног у слона?", 1, 4, "1", "2", "3", "4"));
            _questions.Add(new Question("Сколько хвостов у слона?", 1, 1, "1", "2", "3"));
            _questions.Add(new Question("Сколько глаз у слона?", 1, 2, "1", "2", "3", "4"));
            _questions.Add(new Question("Что является национальным животным Шотландии?", 1, 2, "Лошадь", "Единорог", "Волк", "Корова"));
            _questions.Add(new Question("Как называется колокол часов Вестминстерского дворца в Лондоне?", 1, 1, "Биг Бен", "Мумия", "Башня", "Клуб"));
            _questions.Add(new Question("Какой безалкогольный напиток первым был взят в космос?", 1, 3, "Пепси", "Фанта", "Кока-Кола", "Снапл"));
            _questions.Add(new Question("Сколько весит костюм Чубакки?", 1, 2, "3.6 кг", "7.7 кг", "2.7 кг", "6.8 кг"));
            _questions.Add(new Question("За какую страну играл Дэвид Бекхэм?", 1, 4, "Испания", "Бразилия", "США", "Англия"));
            _questions.Add(new Question("Кто был первым человеком, увидевшим луны Юпитера?", 1, 1, "Галилео Галилей", "Альберт Эйнштейн", "Исаак Ньютон", "Николай Коперник"));
            _questions.Add(new Question("Кто была первой женщиной, получившей Нобелевскую премию в 1903 году?", 1, 3, "Перл Бак", "Розалинд Франклин", "Мария Кюри", "Джейн Аддамс"));
            _questions.Add(new Question("“K” - это химический символ какого элемента?", 1, 4, "Хром", "Титан", "Водород", "Калий"));
            _questions.Add(new Question("Кто был первым человеком, побывавшим на Луне?", 1, 4, "Джеймс Б. Ирвин", "Пит Конрад", "Алан Шепард", "Нил Армстронг"));
            _questions.Add(new Question("Как называются животные, которые питаются только растениями?", 1, 2, "Плотоядные", "Травоядные", "Всеядные", "Вегетарианец"));
            _questions.Add(new Question("Что это за животное - косатка?", 1, 4, "Тюлень", "Осьминог", "Акула", "Кит"));
            _questions.Add(new Question("В 2017 году как звали артистку, у которой было больше всего стримов на Spotify?", 1, 4, "Бейонсе", "Селена Гомес", "Тейлор Свифт", "Рианна"));
            _questions.Add(new Question("Как Леди Гага ласково называет своих поклонников?", 1, 2, "Army", "Little Monsters", "Beliebers", "KatyCats"));
            _questions.Add(new Question("Из какой страны родом Шакира?", 1, 1, "Колумбия", "Аргентина", "Бразилия", "Испания"));
            _questions.Add(new Question("Что является столицей Австралии?", 1, 1, "Канберра", "Аделаида", "Сидней", "Мельбурн"));
            _questions.Add(new Question("Какая страна является самой подверженной землетрясениям страной в мире?", 1, 2, "Малайзия", "Япония", "Корея", "Тайвань"));
            _questions.Add(new Question("Какая кошка самая большая на планете?", 1, 2, "Лев", "Тигр", "Гепард", "Барс"));
            _questions.Add(new Question("Какое сухопутное животное может открыть рот максимально широко?", 1, 4, "Аллигатор", "Крокодил", "Бабуин", "Бегемот"));
            _questions.Add(new Question("Какое животное самое крупное на Земле?", 1, 2, "Африканский слон", "Синий кит", "Кашалот", "Гигантский кальмар"));
            _questions.Add(new Question("Какое млекопитающее умеет летать?", 1, 1, "Летучая мышь", "Белка-летяга", "Белоголовый орлан", "Колуго"));
            _questions.Add(new Question("Как называется еврейский Новый год?", 1, 1, "Ханука", "Йом Кипур", "Кванза", "Рош ха-Шана"));
            _questions.Add(new Question("Какая планета самая горячая?", 1, 4, "Венера", "Сатурн", "Меркурий", "Марс"));
            _questions.Add(new Question("Какое животное находится под защитой закона в Риме?", 1, 3, "Курицы", "Собаки", "Кошки", "Львы"));
            _questions.Add(new Question("В каком животном можно найти жемчуг?", 1, 2, "Крабы", "Устрицы", "Мидии", "Омары"));
            _questions.Add(new Question("Какая птица ассоциируется у вас с миром?", 1, 4, "Робин", "Страус", "Голубь", "Орел"));
            _questions.Add(new Question("Как зовут домашнюю обезьянку Росса в сериале “Друзья”?", 1, 4, "Малыш", "Лесси", "Марли", "Марсель"));
            _questions.Add(new Question("Какой самый большой остров в мире?", 1, 3, "Исландия", "Исландия", "Гренландия", "Ирландия"));
            Start();
        }

        protected void Start()
        {
            for (int i = 0; i < _questions.Count; i++)
            {
                Console.WriteLine(String.Concat(_questions[i].Name, "\r\n", _questions[i].GetAnswers(), " "));

                int res = _questions[i].SetAnswer(Console.ReadLine());
                _count += res;

                if (res > 0)
                {
                    Console.ForegroundColor = ConsoleColor.Green;
                    Console.WriteLine("Верно");
                    Console.ResetColor();
                }
                else
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("Неверно");
                    Console.ResetColor();
                }
                {
                    Console.ForegroundColor = ConsoleColor.Blue;
                    Console.WriteLine("Ваш результат: " + _count);
                    Console.ResetColor();
                }
            }
        }
    }
}