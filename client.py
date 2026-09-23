import socket

HOST = "127.0.0.1"
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    print("Підключення до серверу...")

    while True:
        message = input("Клієнт: ")
        client.sendall(message.encode("utf-8"))

        if message.strip().lower() == "exit":
            print("Чат завершено.")
            break

        data = client.recv(1024)

        if not data:
            print("Сервер відключився.")
            break

        reply = data.decode("utf-8")

        if reply.strip().lower() == "exit":
            print("Сервер завершив чат.")
            break

        print("Сервер:", reply)