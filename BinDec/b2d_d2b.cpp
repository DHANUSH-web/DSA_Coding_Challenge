// DHANUSH H V  https://www.github.com/DHANUSH-web
// Both binary to decimal and decimal to binary in a single program
// Programmed in: C++

#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

void binary(int dec)
{
	int bits[256], i=0;

	while (dec > 0)
	{
		bits[i] = (dec % 2);
		dec /= 2;
		i++;
	}

	for (int j = i - 1; j >= 0; j--)
	{
		cout << bits[j];
	}

	cout << endl;
}

int decimal(char bin[])
{
	int sz, dec=0, index;
	sz = strlen(bin);
	index = sz - 1;

	for (int i = 0; i < sz; i++)
	{
		if (bin[i] == '1')
		{
			dec += pow(2, index);
		}

		index--;
	}

	return dec;
}

int main()
{
	char mod;

	cout << "Enter input type(b/d): ";
	cin >> mod;

	if (mod == 'b')
	{
		char bin[256];

		cout << "Enter binary value: ";
		cin >> bin;

		cout << "Decimal: " << decimal(bin) << endl;
	}

	else
	{
		int dec;

		cout << "Enter a decimal value: ";
		cin >> dec;

		cout << "Binary: ";
		binary(dec);
	}

	return 0;
}
