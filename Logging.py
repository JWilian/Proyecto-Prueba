import logging

#Configuraciòn del registro de actividades
logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w", format="%(asctime)s - %(levelname)s - %(message)s") 
    #INFO: puede ir DEBUG, WARNING, ERROR, CRITICAL, eso dependerà de que tipo de actividad o error se quiera registrar.
    #log.log: nombre del archivo en el cual se editará el registro
    #w, indica que se creará un nuevo archivo cada vez que se ejecute el programa
    #para crear un registro continuo, se deberá utilizar un nombre dinámico en vez de log.log
    #format: da formato a la presentaciòn del documento, asctime: registra la hora del evento


#NIVELES DE REGISTRO - Depuración, información, advertencia, error y critical
logging.debug("debug") #Depuración.
logging.info("info")  #Información
logging.warning("warning")   #Advertencia
logging.error("error") #Error
logging.critical("critical")  #Critical

#Un ejemplo para mostrar el evento de INFO
X=2
logging.info(f"the value of x is {X}")