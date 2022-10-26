#Iniciamos descargando el modulo a través de pip
#pip install psycopg2
#A continuación importamos el módulo
import psycopg2
try:
    #abrimos la conexión, dando los argumentos de nuestro usuario en postgresql
    connection = psycopg2.connect(user='postgres',password='uni20100420f',host='localhost',port='3254',database='miprimerabase')
    #Creamos un cursor, el cual manipula la base de datos
    print("conección exitosa")
    #Abrimos un cursor
    cursor = connection.cursor()
    #Revisamos la versión de postgress 
    cursor.execute("SELECT version()")
    row=cursor.fetchone() #fetchone, para extraer solo un dato
    print(row)
    #Extraemos todos los datos de una tabla
    cursor.execute("SELECT * FROM contacts") 
    #lo ubicado dentro del paréntesis, es el elnguaje de la base de datos, en este caso PostgreSQL
    #contacts, es el nombre de mi tabla en mi base de datos
    contactos = cursor.fetchall() #fetchall para etraer todos los datos de la tabla
    for row in contactos:
        print(row)

except Exception as ex:
    print("ex")

finally:
    connection.close()
    print("Conección finalizada")