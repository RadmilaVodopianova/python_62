import socket

HOST = "127.0.0.1"
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print("Сервер очікує підключення...")

    client_socket, address = server.accept()

    with client_socket:
        print(f"Клієнт підключився: {address}")

        while True:
            data = client_socket.recv(1024)

            if not data:
                print("Клієнт відключився.")
                break

            message = data.decode("utf-8")

            if message.strip().lower() == "exit":
                print("Клієнт завершив чат.")
                break

            print("Клієнт:", message)

            reply = input("Сервер: ")
            client_socket.sendall(reply.encode("utf-8"))

            if reply.strip().lower() == "exit":
                print("Чат завершено.")
                break