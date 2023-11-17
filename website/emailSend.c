#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main()
{
    // get the file that holds the issue
    FILE *inputFile = fopen("issue.txt", "r");
    // create new file for email
    FILE *emailFile = fopen("email.txt", "w"); 
    char line[500];
    int isFirstLine = 1;

    // check if file successfully opened, error testing
    if (inputFile == NULL || emailFile == NULL)
    {
        printf("ERROR - unable to open files\n");
        // return a 1 indicating error
        return 1;
    }
    // otherwise it was successful
    else
    {
        printf("Files opened successfully\n");
    }

    // read the file line by line
    while (fgets(line, sizeof(line), inputFile) != NULL)
    {
        // If its the first line, construct the email headers
        if (isFirstLine)
        {
            fprintf(emailFile, "To: 2502sophia@gmail.com\nSubject: %s\n", line);
            isFirstLine = 0;  // Set the flag to false after processing the first line
        }
        else
        {
            // Write each subsequent line to the new file
            fprintf(emailFile, "%s", line);
        }
    }

    // close the files
    fclose(inputFile);
    fclose(emailFile);

    // this is for error testing
    int result = system("sendmail -t < email.txt");

    // Check if the sendmail command returned 0, indicating success
    if (result == 0)
    {
        printf("sendmail command executed successfully.\n");
    }
    // otherwise it failed, show error message
    else
    {
        printf("sendmail command failed.\n");
    }


    remove("issue.txt");
    remove("email.txt");

    return 0;
}
