#Iniciamos descargando el modulo a través de pip
#pip install psycopg2
#A continuación importamos el módulo
import psycopg2
#abrimos la conexión, dando los argumentos de nuestro usuario en postgresql
try:
    connection = psycopg2.connect(user='postgres',password='uni20100420f',host='localhost',port='3254',database='miprimerabase')
    #Creamos un cursor, el cual manipula la base de datos
    print("conección exitosa")
    #Abrimos un cursor
    cursor = connection.cursor()
    #Revisamos la versión de postgress 
    cursor.execute("Select version()")
    row=cursor.fetchone()
    print(row)
    #Extraemos todos los datos de una tabla
    cursor.execute("SELECT * FROM curso") #lo ubicado dentro del paréntesis, es el elnguaje de la base de datos, en este caso PostgreSQL
    rows = cursor.fetchall()
    for row in rows:
        print(row)


except Exception as ex:
    print("ex")


#record = cur.fetchone()   #este comando trae solo una fila
#record = cur.fetchall() #este comando trae todas las filas

#print(record)
