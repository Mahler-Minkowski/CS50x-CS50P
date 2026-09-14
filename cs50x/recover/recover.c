#This is the homework of cs50x
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>

bool jpeg(unsigned char* block);

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Call the file name\n");
        return 1;
    }
    FILE *card = fopen(argv[1] , "r");
    if (card == NULL)
    {
       printf("Call the file name\n");
       return 1;
    }
    int counter = 1;
    unsigned char* block = malloc(512);
    bool ind_1 = true;
    bool ind_2 = true;
    char buf_[20];
    FILE *writefile = NULL;


    while(fread(block, 512,1,card) == 1)
    {
        if(jpeg(block))
        {
            if(writefile != NULL)
            {
                fclose(writefile);
                counter++;
                sprintf(buf_ ,"%03d.jpeg", counter);
                writefile = fopen(buf_ ,"w");
                fwrite(block, 512, 1, writefile);
            }
            else
            {
                sprintf(buf_ ,"%03d.jpeg", counter);
                writefile = fopen(buf_, "w");
                fwrite(block, 512, 1, writefile);
            }

        }
        else
        {
            if(writefile != NULL)
            {
                fwrite(block, 512, 1, writefile);
            }
        }

    }
    free(block);
}

bool jpeg(unsigned char* block)
{
    bool ori = false;
    for(int i = 0 ;i < 508; i++)
    {
        if (block[i] == 0xff && block[i+1] == 0xd8 && block[i+2] == 0xff)
        {
            if (block[i+3] ==0xe0 || block[i+3] ==0xe1 || block[i+3] ==0xe2 ||
                block[i+3] ==0xe3 || block[i+3] ==0xe4 || block[i+3] ==0xe5 ||
                block[i+3] ==0xe6 || block[i+3] ==0xe7 || block[i+3] ==0xe8 ||
                block[i+3] ==0xe9 || block[i+3] ==0xea || block[i+3] ==0xeb ||
                block[i+3] ==0xec || block[i+3] ==0xed || block[i+3] ==0xef)
            {
                ori = true;
            }
        }
    }
    return ori;
}





