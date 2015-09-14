__author__ = 'samhauck'

import os
import csv
import pandas as pd



#get_file_path takes the file name and returns where it is stored on your computer to properly access the file
def get_file_path(filename):
    currDirPath = os.getcwd()
    file_path = os.path.join(os.getcwd(), filename)
    print file_path
    return file_path

#created objects for each of the .csv filepaths
path1 = get_file_path('Census_Data_-_Languages_spoken_in_Chicago__2008___2012.csv')
path2 = get_file_path('Census_Data_-_Selected_socioeconomic_indicators_in_Chicago__2008___2012.csv')

#i made this method to first make sure i could read the files adn print them in the console
def read_CSV(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print row

#using pandas to read the .csv files
a = pd.read_csv(path1)
b = pd.read_csv(path2)

#creating a new object by merging the two files on the column 'Community Area' which is the same throughout both files
merged = a.merge(b, on='Community Area')

#printing the colomn titles to make sure they merged properly
for eachline in merged:
    print(eachline)

#saving the newly created 'merged' object as a .csv file called output.csv
merged.to_csv("output.csv", index=False)


#read_CSV(path1)
#read_CSV(path2)