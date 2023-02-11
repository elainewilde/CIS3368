#more concise way to code for connection & table creation from tutorialspoint
#originally used the example in class but liked this better due to being more concise

#---------------------------------------CONNECTION---------------------------------------------
import mysql.connector

#making the connection with mysql connector & inserting my database info in
mydb = mysql.connector.connect(
   user='admin', password='Dustylaw95931337!m33pNowAy', host='cis3368spring.clhkjoaevkn8.us-east-2.rds.amazonaws.com', database='cis3368springdb'
)

#Making the cursor object & using the cursor method
cursor = mydb.cursor()



#---------------------------------------CREATES TABLE------------------------------------------

#I wasn't sure if I should Create the table here due to us making it in class in MySQL but
#here is the code for table creation if it is needed

#Creates the table, this can also be created in MySQL.#
#sql ='''CREATE TABLE FISH(
   #ID INT NOT NULL AUTO_INCREMENT,
   #SUPERCLASS VARCHAR(30),
   #SPECIES VARCHAR(30),
   #COLOR CHAR(20),
   #ACQUIRED VARCHAR(3),
   #ALIVE VARCHAR(3),
   #PRIMARY KEY (ID)
#)'''

#cursor.execute(sql)
#----------------------------------------------------------------------------------------------




#---------------------------------------FISH MENU----------------------------------------------

#created the menu with help of reference. The link to this at the end of document
def fish_menu():
    print ("MENU")
    print ("a - Add fish")
    print ("o - Output all fish in console")
    print ("q - Quit\n")

#enter a, o, or q here to toggle menu
fish_menu()
option = str(input("Enter option:"))

#only 5 inputs because the 6th one is auto incremented source for this at the end of document
while option !="q":
    if option.lower() == "a":
        super_class = input("Enter superclass here: ")
        final_species= input("Enter species here: ")
        final_color= input("Enter color here: ")
        if_acquired= input("Enter aquisition status here: ")
        if_alive = input("Is the fish alive? ")
        sql = "INSERT INTO FISH (SUPERCLASS, SPECIES, COLOR, ACQUIRED, ALIVE) VALUES (%s, %s, %s, %s, %s)"
        val = (super_class,final_species, final_color, if_acquired, if_alive)
        cursor.execute(sql, val)
        #commit saves to the database table
        mydb.commit()
        print(cursor.rowcount, "record inserted.")
    elif option.lower() == "o":
        #select statement to print out all the values entered, reference at end of document
        print("Outputting fish\n")
        cursor.execute("SELECT * FROM FISH")
        result = cursor.fetchall()
        for row in result:
            print(row)
    print("\n")
    fish_menu()
    option = str(input("Enter option:"))
    #----------------------------------------------------------------------------------------------



#---------------------------------------SOURCES / REFERENCES----------------------------------------------
# I haven't taken a python course in around 2 years so that's why there are so many guides here
# making the connection & the table https://www.tutorialspoint.com/python_data_access/python_mysql_create_table.htm
# Instructions say to auto increment ID so here is a source that I used for this https://www.w3schools.com/sql/sql_autoincrement.asp #
# Inserting 1 row in to test connection and inserting the data in https://www.w3schools.com/python/python_mysql_insert.asp
# making a menu help video https://www.youtube.com/watch?v=63nw00JqHo0 #
# setting up mysql & python connection video: www.youtube.com/watch?v=3vsC05rxZ8c to better understand the process#
# insert record data values into sql table https://www.w3schools.com/python/python_mysql_insert.asp #
# store data into sql table with inputs https://www.youtube.com/watch?v=R3YiQV1Ho4s#
# printing outputs in entire table https://www.geeksforgeeks.org/how-to-print-out-all-rows-of-a-mysql-table-in-python/#