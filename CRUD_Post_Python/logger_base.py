import logging as log
#Se muestren los errores a partil del nivel DEBUG(level=log.DEBUG)
#Hora en que se lanzo el error %(asctime)s
#Nivel en el que se lanzo el error %(levelname)s 
#Nombre del archivo que arrojo el mensaje ,-
#linea y nombre del mensaje que hemos agregado [%(file)s:%(lineno)s %(message)s]
#Modificar la forma en la que se muestra la fecha datefmt="%I:%M:%S %p"
#Creacion de archivo log.FileHandler("capa_Datos.log")
#Informacion consola log.StreamHandler()
log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()
                ])
#Solo se ejecuta si estamos en el mismo archivo
if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel info')
    log.warning('Mensaje a nivel de warning')
    log.error('Mensaje a nivel de error')
    log.critical('Mensaje a nivel critico')