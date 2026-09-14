c

int calculate_L(string W);
int calculate_S(string W);
int calculate_Blk(string W);

int main(void)
{
    string text = get_string("Text: ");
    int L = calculate_L(text);
    int S = calculate_S(text);
    int W = calculate_Blk(text);
    float index = 0.0588 * (L*1.0)/W *100 - 0.296 * (S*100.0)/W  - 15.8;
    index = round(index);
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade: %.0f\n" , index);
    }

}

int calculate_L(string W)
{
    int n = 0;
    for(int i=0 ;i<strlen(W) ;i++)
    {
        char word = toupper(W[i]);
        if ( 'A' <= word && word<= 'Z' )
        {
            n++;
        }
    }
    return n;
}

int calculate_S(string W)
{
    int n = 0;
    for(int i=0 ;i<strlen(W) ;i++)
    {
        char word = (W[i]);
        if (word == '.' || word == '!' || word == '?')
        {
            n++;
        }
    }
    return n;
}

int calculate_Blk(string W)
{
    int n = 1;
    for(int i=0 ;i<strlen(W) ;i++)
    {
        char word = (W[i]);
        if (word == ' ')
        {
            n++;
        }
    }
    return n;
}
