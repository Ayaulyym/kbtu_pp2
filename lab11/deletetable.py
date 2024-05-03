import psycopg2

# Connect to the database
connection = psycopg2.connect(host = "localhost",
                        user = "postgres",
                        password = "AZAMAT",
                        database = "phonebook",
                        port="5432")

# Create a cursor object to execute SQL commands
cur = connection.cursor()

# Create the phonebook table
cur.execute("CREATE TABLE phonebook (username VARCHAR(50), phone VARCHAR(20))")

# Commit the changes
connection.commit()

# Close the cursor and database connection
cur.close()
connection.close()