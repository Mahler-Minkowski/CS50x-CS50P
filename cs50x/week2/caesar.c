#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int get_ascii(char c,int k);

int main(int argc, char *argv[])
{
    if (argc !=2 || *argv[1] <0)
    {
        return 0;
    }
    else
    {
        string I=get_string("Plaintext: ");
        int strlen_I = strlen(I);
        for(int i=0 ;i < strlen_I ;i++)
        {
            int k;
            sscanf(argv[1], "%d", &k);
            if(isalpha(I[i]))
            {
                int ASCII_aft = get_ascii(I[i], k);
                printf("%c", ASCII_aft);
            }
            else
            {
                printf("%c", I[i]);
            }

        }
        printf("\n");
    }

}

int get_ascii(char c, int k)
{
    if (isupper(c))
    {
        return ((c-'A'+k) % 26) + 'A';
    }
    else if(islower(c))
    {

       return ((c-'a'+k) % 26) + 'a';
    }
    else
    {
        return -1;
    }
}
