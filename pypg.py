import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="dtin_homolog", user='postgres', password='senha', host='172.16.1.12', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute('''SELECT * FROM ced.pessoa
                  WHERE id_pessoa = 3''')

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ",data)

#Closing the connection
conn.close()