#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0 ;i < height ;i++)
    {
        for (int j = 0 ;j < width ;j++)
        {
            int R = image[i][j].rgbtRed;
            int G = image[i][j].rgbtGreen;
            int B = image[i][j].rgbtBlue;
            float avg = round(( R + G + B) / 3.0);
            image[i][j].rgbtRed = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtBlue = avg;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int R = image[i][j].rgbtRed;
            int G = image[i][j].rgbtGreen;
            int B = image[i][j].rgbtBlue;
            sepiaRed = .393 *R + .769 * G + .189 * B
            if (sepiaRed < 255)
            {
                image[i][j].rgbtRed = sepiaRed
            }
            else
            {
                image[i][j].rgbtRed = 255
            }
            sepiaGreen = .349 * R + .686 * G + .168 * B
            if (sepiaGreen < 255)
            {
                image[i][j].rgbtGreen = sepiaGreen
            }
            else
            {
                image[i][j].rgbtGreen = 255
            }
            sepiaBlue = .272 * R + .534 * G + .131 * B
            if (sepiaBlue < 255)
            {
                image[i][j].rgbtBule = sepiaBlue
            }
            else
            {
                image[i][j].rgbtBlue = 255
            }

        }
    }


    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < round(height/2.0); i++)
    {
        for (int j = 0; j < round(width/2.0); j++)
        {
            //original color
            int R = image[i][j].rgbtRed;
            int G = image[i][j].rgbtGreen;
            int B = image[i][j].rgbtBlue;
            //Temporary color(for swap)
            int TR = 0;
            int TG = 0;
            int TB = 0;
            //Reflected color
            int RR = image[i][width - j].rgbtRed;
            int RG = image[i][width - j].rgbtGreen;
            int RB = image[i][width - j].rgbtBlue;

            //Store original color
            TR = R;
            TG = G;
            TB = B;

            //Set Values
            image[i][j].rgbtRed = RR;
            image[i][j].rgbtGreen = RG;
            image[i][j].rgbtBlue = RB;

            image[i][width - j].rgbtRed = TR;
            image[i][width - j].rgbtGreen = TG;
            image[i][width - j].rgbtBlue = TB;


        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
            int counter = 9
            int surroundings[9] = {}
            int up = i - 1
            int down = i + 1
            int left = j - 1
            int right = j + 1
        }
    }

    return;
}
