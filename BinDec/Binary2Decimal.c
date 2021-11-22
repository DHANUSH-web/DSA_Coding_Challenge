// DHANUSH H V  https://www.github.com/DHANUSH-web

#include<stdio.h>
#include<math.h>

int decimal(char bin[])
{
	// find the length of the char array
	int n = 0, dec = 0;

	while (bin[n])
	{
		n++;
	}

	int index = n-1;

	for (int i=0; i<n; i++)
	{
		if (bin[i] == '1')
			dec += pow(2, index);

		index--;
	}

	return dec;
}

int main()
{
	char str[256];

	printf("Enter a binary data: ");
	scanf("%s", str);

	printf("The decimal value is: %d\n", decimal(str));
	return 0;
}
