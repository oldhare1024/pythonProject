import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(user='username', password='password',
                              host='127.0.0.1',
                              database='database_name')

# Create a cursor object
cursor = cnx.cursor()

# Execute a query
query = "SELECT * FROM table_name WHERE column_name = %s"

# Get user input for search term
search_term = input("Enter search term: ")

# Execute the query with the search term as a parameter
cursor.execute(query, (search_term,))

# Fetch the results
results = cursor.fetchall()

# Print the results
for result in results:
    print(result)

# Close the cursor and connection
cursor.close()
cnx.close()
