//This code is cs50x's homework of runoff
#include <cs50.h>
#include <stdio.h>
#include <string.h>


//new data strcture
//We can also add a Boolean expression to indicate whether or not he/she is eliminated
typedef struct
{
    string name;
    int votes;
  //bool check;
} candidate;

//declare global variables
# define MAX 9
candidate candidates[MAX];
int voter_count;
int candidate_count;
int indicator_eli = 0;
string ballot[MAX][MAX];

void tabulate(void);
bool judge_50(void);
void find_min(void);


int main(int argc, string argv[])
{
    if (argc < 2 || argc > 10)
    {
        return -1;
    }

    candidate_count = (argc - 1);
    voter_count = get_int("Voter number: ");
    if (voter_count < 1 || voter_count > 10)
    {
        return -1;
    }

    for (int i = 0; i < (candidate_count); i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }


    for(int i = 0; i < voter_count; i++)
    {
        for(int j = 0; j < candidate_count; j++)
        {
            string input = get_string("Rank %i: ", j+1);
            ballot[i][j] = input;
        }
        printf("\n");
    }

    tabulate();
    while(!judge_50())
    {
        find_min();
        tabulate();
    }
}

void tabulate(void)
{
    for(int i = 0 ;i < candidate_count ;i++)
    {
        candidates[i].votes = 0;
    }
    int indicator = 0;
    for(int i = 0; i < voter_count ; i++)
    {
        for(int k = 0; k < (candidate_count) ;k++)
        {
            if(strcmp(ballot[i][0], candidates[k].name)==0)
            {
                candidates[k].votes++;
            }
        }
    }
}

bool judge_50(void)
{
    bool indicator_bool = false;
    for(int i_ = 0; i_ < candidate_count ; i_++)
    {
        if(candidates[i_].votes > voter_count * 0.5)
        {
            printf("%s Wins!\n", candidates[i_].name);
            indicator_bool = true;
        }
    }
    return indicator_bool;
}


void find_min(void)
{
    int temp_min = candidates[0].votes;
    int temp_num = 0;
    for (int q = 0; q < (candidate_count - 1); q++)
    {
        if (candidates[q].votes > candidates[q + 1].votes)
        {
            if (candidates[q+1].votes < temp_min)
            {
                temp_min = candidates[q+1].votes;
                temp_num = q+1;
            }
        }
    }

    for (int r = 0; r < voter_count; r++)
    {
        if (strcmp(ballot[r][0], candidates[temp_num].name) == 0)
        {
            ballot[r][0] = ballot[r][indicator_eli+1];
        }
    }
    indicator_eli++;
}



