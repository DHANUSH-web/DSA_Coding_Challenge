import java.util.*;

class HelloWorld
{
	static int decimal(String bin)
	{
		char[] i_bits = bin.toCharArray();
		int sz = i_bits.length, dec=0, index;
		index = sz - 1;

		for (char c : i_bits)
		{
			if (c == '1')
			{
				dec += Math.pow(2, index);
			}

			index--;
		}

		return dec;
	}

	static String binary(int dec)
	{
		List<String> bits = new ArrayList<String>();
		String bin = "";

		while (dec > 0)
		{
			bits.add(""+(dec % 2));
			dec /= 2;
		}

		for (int i = bits.size()-1; i >= 0; i--)
		{
			bin += bits.get(i);
		}

		return bin;
	}

	public static void main(String[] args)
	{
		Scanner sc = new Scanner(System.in);

		char mode;

		System.out.print("Enter input type(b/d): ");
		mode = sc.nextLine().charAt(0);

		if (mode == 'b')
		{
			String bin;

			System.out.print("Enter binary value: ");
			bin = sc.nextLine();

			System.out.println("Decimal: " + decimal(bin));
		}

		else
		{
			int dec;

			System.out.print("Enter a decimal value: ");
			dec = sc.nextInt();

			System.out.println("Binary: " + binary(dec));
		}

		sc.close();
	}
}
