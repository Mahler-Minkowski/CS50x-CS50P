// generate mario blocks as pyramid
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int h = get_int("Height: ");
    int n = 0;
    int h_ = h;
    for (int i = 0; i < h; i++)
    {
        for (int j = 1; j < h_; j++)
        {
            printf(" ");
        }
        for (int k = 0; k <= n; k++)
        {
            printf("#");
        }
        printf("\n");
        n++;
        h_--;
    }
}
