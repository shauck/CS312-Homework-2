# CS312-Homework-2

#When looking at the assignment, I saw that we were going to working with large sets of data so i decided that using SQL of some form would be a good method.  I tried using SQLite3 for
#python, but after hours of debugging and rewriting code, I couldn't figure out how to get it to run properly.(This attempt is in main.py)  So, I did a little more research and discovered
#that the pandas library for python might be a good fit for what i was trying to accomplish: merge two .csv files together.  Using pandas, and innate python file reading capabilities I was
#able to read both file by fetching the file path from my computer, print out the info, and merge the two on a common column.  (This part of the code, the working part, is in attempt.py)

#i included the main.py, but all the lines are commented out to avoid errors when running the working program

#the merged .csv file is in output.csv

#Findings
   #For the catagories in the Socioeconomic indicators data, I decided to look at the top three and then compare that information to the language data for those neighborhoods
   #(the parenthesis on the langauge line indicate the percentage of people that speak that language in that neighborhood
    #Communities with highest Overcrowding per household
        #Gage Park: 15.8%
            #Prodominant non-English Language: Spanish (44.5%)
        #South Lawndale: 15.2%
            #Prodominant non-English Language: Spanish (43.8%)
        #Humbolt Park: 14.8%
            ##Prodominant non-English Language: Spanish (18.4%)
    #Communities with highest Percent of households below poverty line
        #Riverdale: 56.5%
            #Prodominant non-English Language: Spanish (1.1%)
        #Fuller Park: 51.2%
            #Prodominant non-English Language: Spanish (2.5%)
        #Englewood: 46.6%
            #Prodominant non-English Language: Spanish (0.4%)
    #Percent Unemployed Age 16+
        #West Englewood: 35.9%
            #Prodominant non-English Language: Spanish (1.2%)
        #Riverdale: 34.6%
            #Prodominant non-English Language: Spanish (1.1%)
        #Fuller Park: 33.9%
            #Prodominant non-English Language: Spanish (2.5%)
    #Percent Age 25+ w/o High school Diploma
        #South Lawndale: 54.8%
            #Prodominant non-English Language: Spanish (43.8%)
        #Gage Park: 51.5%
            #Prodominant non-English Language: Spanish (15.8%)
        #Brighton Park:45.1%
            #Prodominant non-English Language: Spanish (37.9%)
    #Per Capita Income (Decided to look at the lowest here)
        #Riverdale: $8201
            #Prodominant non-English Language: Spanish (1.1%)
        #South Lawndale: $10402
            #Prodominant non-English Language: Spanish (43.8%)
        #Fuller Park: $10432
            #Prodominant non-English Language: Spanish (2.5%)
    #Harship index
        #Riverdale: 98
            #Prodominant non-English Language: Spanish (1.1%)
        #Fuller Park: 97
            #Prodominant non-English Language: Spanish (2.5%)
        #South Lawndale: 96
            #Prodominant non-English Language: Spanish (43.8%)






#Although, all of the neighborhoods listed have spanish as their main non-english language,
#this does not paint the whole picture.  For example, spanish neighborhoods like Gage Park and South Lawndale lead the list in
#terms of homes that are overcrowded.  Despite this, these neighborhoods are not in the top three in terms of households below
#poverty line or the percent of people that are unemployed.  So, these overcrowded Spanish neighborhoods are full are working individuals(even
#though these neighborhoods rank highest in terms of people that do not have their high school diploma), while neighborhoods like
#West Englewood (1.2% spanish-speaking), Riverdale (1.1% Spanish-speaking), and Fuller Park (2.5% spanish-speaking) rank the
#highest in terms of unemployment. 