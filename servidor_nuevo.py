import socket
import random
ip = '127.0.0.1'
puerto = 8025
respuestas = 2
aleatorio = random.randrange(100)
print(aleatorio)

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def comprobar(numero, aleatorio):
    numero = int(numero)
    if 1<=(aleatorio -numero ) <= 10 or 1<= (numero -aleatorio) <= 10 and numero!= aleatorio:
        mns = ("Caliente, caliente")
    elif 10 < (aleatorio - numero )<99:
        mns = ("frío, frío por abajo  ")
    elif 10< (numero -aleatorio) <99:
        mns = ("frío, frío por arriba")
    elif numero == aleatorio:
        mns = ("Felicidades")

    return mns

def logicacliente(cliente):

    c_abierta = True
    while c_abierta:
        mensaje = (cliente.recv(1000).decode('utf-8'))
        print("El número del cliente es: ",mensaje)
        mns2 = str(comprobar(mensaje, aleatorio))
        mns = str.encode(mns2)
        cliente.send(mns)
        break




try:
    servidor.bind((ip, puerto))
    servidor.listen(respuestas)
    while True:

        print('Esperando conexion en {ip},{puerto}'.format(ip = ip, puerto = puerto))
        (cliente, direccion) = servidor.accept()
        print('Se ha conectado alguien')
        logicacliente(cliente)


except KeyboardInterrupt:
    cliente.close()
    servidor.close()
    print('Cerrando el chat...')

