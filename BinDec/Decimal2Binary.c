#include <stdio.h>

// function to print the binary digits
void bin(long decimal)
{
    int bit[256];
    int i = 0;

    while (decimal)
    {
        bit[i] = decimal % 2;
        decimal /= 2;
        i++;
    }

    for (int j = i - 1; j >= 0; j--)
    {
        printf("%d", bit[j]);
    }

    printf("\n");
}

int main()
{
    // decimal to binary using C
    long dec;

    printf("Enter a decimal value: ");
    scanf("%ld", &dec);

    for (int i = 1; i <= dec; i++)
    {
        bin(i);
    }

    return 0;
}
