__author__ = 'samhauck'
import csv
import sqlite3
import sys


#This didnt work

# create a local database using SQLite3 to store the information from the .csv files
createDB = sqlite3.connect(':memory:')

# create a cursor using SQLite3 to iterate through the database
#createCursor = createDB.cursor()


#def main():
    # create a table using SQLite3 to store the information from the .csv file about languages


   # createCursor.executescript('''DROP TABLE IF EXISTS language; CREATE TABLE language
   # (id INTEGER PRIMARY KEY, name TEXT, promLang TEXT, african REAL, arabic REAL, armenian REAL,cambodian REAL, chinese REAL ,creole REAL,
   # french REAL, german REAL, greek REAL, gujarati REAL, hebrew REAL, hindi REAL, hmong REAL, hungarian REAL, italian REAL,
   # japanese REAl, korean REAL, laotian REAL, navajo REAL, other_asain REAL, other_indic REAL, other_indo_european REAL,
   # other_native_north_american REAL, other_pacific_island REAL, other_slavic REAL, other_west_germanic REAL, persian REAL,
   # polish REAL, portuguese REAL, russian REAL, scandinavian REAL, serbo_croatian REAL, spanish REAL, tagalog REAL, thai REAL,
    #unspecified REAL, urdu REAL, vietnamese REAL, yiddish REAL);''')

    # reads the first .csv file to store it in the database as a table
   # with open('Census_Data_-_Languages_spoken_in_Chicago__2008___2012.csv', 'rb') as csvfile1:
        #reader1 = csv.reader(csvfile1, delimiter=',',)
        #for row in reader1:
            #to_db1 = [unicode(row[0], "utf8")], [unicode(row[1], "utf8")], [unicode(row[2], "utf8")],  [unicode(row[3], "utf8")], \
                    # [unicode(row[4], "utf8")], [unicode(row[5], "utf8")], [unicode(row[6], "utf8")], [unicode(row[7], "utf8")], \
                     #[unicode(row[8], "utf8")], [unicode(row[9], "utf8")], [unicode(row[10], "utf8")], [unicode(row[11], "utf8")], \
                     #[unicode(row[12], "utf8")], [unicode(row[13], "utf8")], [unicode(row[14], "utf8")], [unicode(row[15], "utf8")], \
                     #[unicode(row[16], "utf8")], [unicode(row[17], "utf8")], [unicode(row[18], "utf8")], [unicode(row[19], "utf8")], \
                     #[unicode(row[20], "utf8")], [unicode(row[21], "utf8")], [unicode(row[22], "utf8")], [unicode(row[23], "utf8")], \
                    # [unicode(row[24], "utf8")], [unicode(row[25], "utf8")], [unicode(row[26], "utf8")], [unicode(row[27], "utf8")], \
                    # [unicode(row[28], "utf8")], [unicode(row[29], "utf8")], [unicode(row[30], "utf8")], [unicode(row[31], "utf8")], \
                    # [unicode(row[32], "utf8")], [unicode(row[33], "utf8")], [unicode(row[34], "utf8")], [unicode(row[35], "utf8")], \
                    # [unicode(row[36], "utf8")], [unicode(row[37], "utf8")], [unicode(row[38], "utf8")], [unicode(row[39], "utf8")], \
                     #[unicode(row[40], "utf8")]


    # uses cursor to write the data from .csv file into the table called languages
   # createCursor.executemany('''INSERT INTO language
   # (name, promLang, african, arabic, armenian,cambodian, chinese ,creole,
    #french, german, greek, gujarati, hebrew, hindi, hmong, hungarian, italian,
   # japanese, korean, laotian, navajo, other_asain, other_indic, other_indo_european,
    #other_native_north_american, other_pacific_island, other_slavic, other_west_germanic, persian,
   # polish, portuguese, russian, scandinavian, serbo_croatian, spanish, tagalog, thai,
    #unspecified, urdu, vietnamese, yiddish) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);''',
                           #  (to_db1,))

    #createDB.commit()

    #for row in createCursor.execute('''SELECT * FROM languages'''):
       #print row

    # create a table using SQLite3 to store the information from the .csv file about socioeconomic trends
   # createCursor.execute('''CREATE TABLE socioEcon
   # (id INTEGER PRIMARY KEY, name TEXT, percent_crowded REAL, percent_below_poverty REAL, unemployment REAL,
   # percent_without_hs_diploma REAL, percent_children_elderly REAL, per_capita_income REAL, hardship_index REAL)''')


#main()
