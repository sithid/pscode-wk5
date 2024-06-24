using System;

class Program
{
    static void Main()
    {
        Console.Clear();

        Console.WriteLine("First Task: Find the sum of 2 numbers.");

        Console.Write("Enter your first number: ");
        int num1 = Convert.ToInt32(Console.ReadLine());
        
        Console.Write("Enter your second number: ");
        int num2 = Convert.ToInt32(Console.ReadLine());

        int sum = num1 + num2;

        Console.WriteLine($"The sum of {num1} and {num2} is {sum}");

        Console.Write("Continue? (y/n): ");
        string temp = Console.ReadLine();

        if (temp == "n")
            Environment.Exit(0);

        Console.Clear();

        Console.WriteLine("Second Task: Decide if the given number is odd or even.");

        Console.Write("Enter your number: ");
        int num = Convert.ToInt32(Console.ReadLine());

        if (num % 2 == 0)
            Console.WriteLine($"{num} is an even number!");
        else
            Console.WriteLine($"{num} is an odd number!");

        Console.Write("Continue? (y/n): ");
        temp = Console.ReadLine();

        if (temp == "n")
            Environment.Exit(0);

        Console.Clear();

        Console.WriteLine("Find the average of 5 numbers.");

        int min = 0;
        int max = 0;
        int totalSum = 0;

        for (int i = 0; i < 5; i++)
        {
            Console.Write(i == 0 ? "Enter your first value: " : i == 4 ? "Enter your last value: " : "Enter your next value: ");
            num = Convert.ToInt32(Console.ReadLine());

            totalSum += num;

            if (num < min || min == 0)
                min = num;
            else if (num > max || max == 0)
                max = num;
        }

        double average = totalSum / 5.0;

        Console.WriteLine($"The smallest number is {min}. The largest number is {max}.");
        Console.WriteLine($"The sum of these 5 numbers is {totalSum}.");
        Console.WriteLine($"The average of these 5 numbers is {average}.");

        Console.Write("Continue? (y/n): ");
        temp = Console.ReadLine();

        if (temp == "n")
            Environment.Exit(0);

        Console.Clear();

        Console.Write("Enter the number to end after: ");
        num = Convert.ToInt32(Console.ReadLine());

        int fizz = 0;
        int buzz = 0;
        int fizzBuzz = 0;
        int none = 0;

        for (int i = 0; i <= num; i++)
        {
            if (i % 3 == 0)
            {
                if (i % 4 == 0)
                {
                    Console.WriteLine("FizzBuzz");
                    fizzBuzz++;
                }
                else
                {
                    Console.WriteLine("Fizz");
                    fizz++;
                }
            }
            else if (i % 4 == 0)
            {
                Console.WriteLine("Buzz");
                buzz++;
            }
            else
            {
                Console.WriteLine(i);
                none++;
            }
        }

        Console.WriteLine($"Divisible by 3: {fizz}, Divisible by 4: {buzz}, Divisible by both: {fizzBuzz}, Divisible by neither: {none}");
    }
}
