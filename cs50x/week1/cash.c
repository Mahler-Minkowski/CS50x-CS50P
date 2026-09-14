#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int amount=0;
    int change=get_int("Change owed: ");
    if (change/25 !=0)
    {
        amount+=change/25;
        change-=amount*25;
    }
    if (change/10 !=0)
    {
        int delta_change=change/10;
        amount+=change/10;
        change-=delta_change*10;
    }
    if (change/5 !=0)
    {
        int delta_change=change/5;
        amount+=change/5;
        change-=delta_change=change*5;
    }
    if (change/1 !=0)
    {
        amount+=change/1;
    }
    printf("%i\n",amount);

}
