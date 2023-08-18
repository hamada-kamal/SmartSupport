
# ************* the Explanations ******************
#1- import psycopy2 , Error from psycopy2 to handling erorrs
#1- create a connection with my database using connect() function
#2- create a cursor to execute the sql queries 
#3- fetch data using execute() function
#4- loop on the data and print it
#5- close the cursor and connection using close() function
#6- put the code between try and except to handeling errors
  
import psycopg2
from psycopg2 import Error


try:
    # connect to database
    connection = psycopg2.connect(user="postgres",
                                password="123",
                                host="127.0.0.1",
                                port="5432",
                                database="smart_db")

    # create a cursor to perform database operations
    cursor = connection.cursor()
    cursor.execute("SELECT * From products;")
    # use fetchall() to get a list of all products
    products = cursor.fetchall()  #products here is a list of tuples like >> [(id, name, price), (id, name, price)]
    #lets loop in products
    for product in products:
        print("name: ",product[1]," price: ",product[2])
    cursor.close()
    connection.close()

except (Exception, Error) as error:
    print("failed to connect", error)