import tkinter as tk
import socket
import threading

def send_to_socket(message='Nick: Test messages'):
    if message:
        server_socket.send(message.encode())
        entry.delete(0, tk.END)

def receive_messages():
    while True:
        try:
            message = server_socket.recv(1024).decode()
            if message:
                message_list.insert(tk.END, message)
        except ConnectionAbortedError:
            break

def send_message():
    #todo: 2. Отримати повідомлення з entry
    #todo: 3. Отримати nickname з поля entry
    #todo: 4. Скласти одне повідомлення з nickname та повідомлення в форматі: "nickname: messages"
    #todo: 5. Передати повідомлення через функцію send_to_socket
    pass




root = tk.Tk()

root = root
root.title("Chat 37KI")

message_list = tk.Listbox(root, width=50, height=20)
message_list.pack(padx=10, pady=10)

entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=5)


#todo: 1. Додати entry поле на екран, щоб отримати nickname

send_button = tk.Button(root, text="Надіслати", command=send_message)
send_button.pack(padx=10, pady=5)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect(('151.115.78.136', 9999))

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

root.mainloop()
