import socket

ip = '127.0.0.1'
puerto = 8025
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    cliente.connect((ip, puerto))
    print('Bienvenido al chat!')

    c_abierta = True
    while c_abierta:
        out = input("Introduzca un número entre 0 y 99 : ")
        outbox = str.encode(out)
        cliente.send(outbox)
        a = cliente.recv(2048).decode("utf-8")
        print("El servidor nos dice: ", a)
        if a.lower() == "felicidades":
            condition = False
            cliente.close()
            break

except KeyboardInterrupt:
    cliente.close()
    print('Cerrando el chat...')
