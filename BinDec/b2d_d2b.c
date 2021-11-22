// DHANUSH H V  https://www.github.com/DHANUSH-web
// Binary to decimal or Decimal to binary in one program
#include <stdio.h>
#include <math.h>
#include <string.h>

// function returns decimal value
int decimal(char bin[])
{
	int sz, i, index, dec = 0;
	sz = strlen(bin);
	index = sz - 1;

	for (i = 0; i < sz; i++)
	{
		if (bin[i] == '1')
		{
			dec += pow(2, index);
		}

		index--;
	}

	return dec;
}

// function prints the binary output
void binary(int dec)
{
	int bits[256], i=0, j;

	while (dec > 0)
	{
		bits[i] = (dec % 2);
		dec /= 2;
		i++;
	}

	for (j = i-1; j >= 0; j--)
	{
		printf("%d", bits[j]);
	}

	printf("\n");
}

int main(int argc, char const *argv[]) {
	char mode;

	printf("Enter input type: ");
	scanf("%c", &mode);

	if (mode == 'b')
	{
		char bin[256];
		printf("Enter the binary value: ");
		scanf("%s", bin);
		printf("Decimal: %d\n", decimal(bin));
	}

	else
	{
		int dec;

		printf("Enter the decimal value: ");
		scanf("%d", &dec);
		printf("Binary: ");
		binary(dec);
	}
	return 0;
}
