using System;

namespace SecreteMissionCodes
{
    class MainClass
    {
        static int Decimal(string bin)
        {
            int sz, dec=0, index;

            sz = bin.Length;
            index = sz - 1;

            foreach (char bit in bin)
            {
                if (bit == '1')
                {
                    dec += Convert.ToInt32(Math.Pow(2, index));
                }

                index--;
            }

            return dec;
        }

        static string Binary(int dec)
        {
            string bits = "", bin = "";

            while (dec > 0)
            {
                bits += $"{dec % 2}";
                dec /= 2;
            }

            for (int i = bits.Length-1; i >= 0; i--)
            {
                bin += bits[i];
            }

            return bin;
        }

        public static void Main(string[] args)
        {
            char mode;

            Console.Write("Enter input type: ");
            mode = Console.ReadLine()[0];

            if (mode == 'b')
            {
                string bin;

                Console.Write("Enter binary value: ");
                bin = Console.ReadLine();

                Console.WriteLine($"Decimal: {Decimal(bin)}");
            }

            else
            {
                int dec;

                Console.Write("Enter the decimal input: ");
                dec = Convert.ToInt32(Console.ReadLine());

                Console.WriteLine($"Binary: {Binary(dec)}");
            }
        }
    }
}
