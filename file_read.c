#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *fptr;
    char dataToBeRead[256];     // maximum array bit size (i.e 256)
    char fileName[256];

    printf("Note: File name should not contain spaces\nEnter file name: ");
    scanf("%s", fileName);
    
    fptr = fopen(fileName, "r");

    if (fptr == NULL)
    {
        printf("File not found\n");
        exit(1);
    }

    else
    {
        int i = 0;

        while (fgets(dataToBeRead, 256, fptr) != NULL)
        {
            i++;
            if (i < 10)
                printf("0%d| %s", i, dataToBeRead);
            else
                printf("%d| %s", i, dataToBeRead);
        }

        printf("\n");
    }
    
    return 0;
}