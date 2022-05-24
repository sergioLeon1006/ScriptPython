import MySQLdb;from datetime import datetime;from random import randrange;
listaIds = [18,19] #users to insert jaja
miConexion = MySQLdb.connect( host='localhost', user= 'root', passwd='Serviun1x', db='db_serviunix_pausas' )
cur = miConexion.cursor()
insertDate = datetime.today().strftime('%Y-%m-%d')
day = datetime.today().weekday() #know what day is it (0 monday-6 sunday)
if(day < 5):
    for person in listaIds:
        minutes = randrange(59); seconds = randrange(59); hour = randrange(14,16)
        fullHour = insertDate+' '+ str(hour)+':'+str(minutes)+':'+str(seconds)
        cur.execute("INSERT INTO db_serviunix_pausas.tbl_registro (usuario, fechaRegistro)VALUES(%s,%s)",(int(person),str(fullHour)))
    miConexion.commit(); miConexion.close()