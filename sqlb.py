# INSERT Command


# import the sqlite3 library
import sqlite3

# create the connection object
print "connecting to the database..."
conn = sqlite3.connect("new.db")
print "connection established."

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# insert data
print "executing sql commands..."
cursor.execute("INSERT INTO population VALUES('New York City', \
	'NY', 8200000)")
cursor.execute("INSERT INTO population VALUES('San Francisco', \
	'CA', 800000)")
print "commands executed successfully."
# commit the changes
print "effecting the changes in the database..."
conn.commit()
print "Done."

# close the database connection
conn.close()