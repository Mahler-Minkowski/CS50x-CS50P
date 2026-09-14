#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
} candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
        else
        {
            for(int j = 0; j < candidate_count; j++)
            {
                if(strcmp(candidates[j].name, name) == 0)
                candidates[j].votes++;
            }

        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    if (strcmp(name, " ") == 0)
    {
        return false;
    }
    else
    {
        bool indicator_ = false;
        for(int k = 0; k < (candidate_count - 1); k++)
        {
            if (strcmp(candidates[k].name, name) ==0)
            {
                indicator_ = true;
            }
            else
            {
                indicator_ = false;
            }
        }
        return indicator_;
    }
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    int temp_win = candidates[0].votes;
    int temp_num = 0;
    for (int i = 0; i < (candidate_count - 1); i++)
    {
        if (candidates[i].votes < candidates[i + 1].votes)
        {
            if (candidates[i+1].votes > temp_win)
            {
                temp_win = candidates[i+1].votes;
                temp_num = i+1;
            }
        }
    }
    for (int p = 0; p < candidate_count; p++)
    {
        if (candidates[p].votes == temp_win && temp_win != 0)
        {
            printf("%s\n", candidates[p].name);
        }
    }
    if (temp_win != 0)
    {
         printf("%s\n", candidates[temp_num].name);
    }
}

