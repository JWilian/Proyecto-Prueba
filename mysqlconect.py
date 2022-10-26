#Iniciamos descargando el modulo a través de pip
#pip install mysql-connector-python
#A continuación importamos el módulo
import mysql.connector
try:
    #abrimos la conexión, dando los argumentos de nuestro usuario en postgresql
    connection = mysql.connector.connect(user='root',password='Uni20100420f',host='localhost',port='0633',database='basedeprueba')
    #Creamos un cursor, el cual manipula la base de datos
    print("conección exitosa")
    #Abrimos un cursor
    cursor = connection.cursor()
    #Revisamos la versión de MySQL 
    cursor.execute("Select version();")
    row=cursor.fetchone() #fetchone, para extraer solo un dato
    print(row)
    #Creamos datos en nuestra base de datos
    cursor.execute("insert into pelicula (idpelicula,nombrepelicula) values(3,'HappyFeet1');") 
    #lo ubicado dentro del paréntesis, es el elnguaje de la base de datos, en este caso MySQL
    #pelicula, es el nombre de mi tabla en mi base de datos
    connection.commit() #Graba los valores dados en la tabla
    cursor.execute("SELECT * FROM pelicula;")
    peliculas = cursor.fetchall() #fetchall para etraer todos los datos de la tabla
    for row in peliculas:
        print(row)
except Exception as ex:
    print("ex")

finally:
    connection.close()
    print("Conección finalizada")
