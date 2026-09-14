#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int compare(string W);

int main(void)
{
    string A = get_string("Player A: ");
    string B = get_string("Player B: ");
    int score_A = compare(A);
    int score_B = compare(B);
    if (score_A < score_B)
    {
        printf("B wins!\n");
    }
    if (score_A > score_B)
    {
        printf("A wins!\n");
    }
    else
    {
        printf("Both wins!\n");
    }
}

int compare(string W)
{
    int score = 0;
    for(int i = 0 ;i < strlen(W) ;i++)
    {
        char Key = toupper(W[i]);
        switch(Key)
        {
            case 'A': score += 1; break;
            case 'B': score += 3; break;
            case 'C': score += 3; break;
            case 'D': score += 2; break;
            case 'E': score += 1; break;
            case 'F': score += 4; break;
            case 'G': score += 2; break;
            case 'H': score += 4; break;
            case 'I': score += 1; break;
            case 'J': score += 8; break;
            case 'K': score += 5; break;
            case 'L': score += 1; break;
            case 'M': score += 3; break;
            case 'N': score += 1; break;
            case 'O': score += 1; break;
            case 'P': score += 3; break;
            case 'Q': score += 10; break;
            case 'R': score += 1; break;
            case 'S': score += 1; break;
            case 'T': score += 1; break;
            case 'U': score += 1; break;
            case 'V': score += 4; break;
            case 'W': score += 4; break;
            case 'X': score += 8; break;
            case 'Y': score += 4; break;
            case 'Z': score += 10; break;
        }
    }
    return score;
}
