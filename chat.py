# client.py
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                message_box.config(state=tk.NORMAL)
                message_box.insert(tk.END, message + '\n')
                message_box.yview(tk.END)
                message_box.config(state=tk.DISABLED)
        except:
            print("An error occurred!")
            client_socket.close()
            break

def send_message():
    message = message_entry.get()
    if message:
        client_socket.send(message.encode('utf-8'))
        message_entry.delete(0, tk.END)

# Connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 5555))

# Start the GUI
root = tk.Tk()
root.title("Chat App")

frame = tk.Frame(root)
scrollbar = tk.Scrollbar(frame)

message_box = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=50, height=20, state=tk.DISABLED)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
message_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
frame.pack()

message_entry = tk.Entry(root, width=50)
message_entry.pack(pady=10)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

# Start a thread to receive messages from the server
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

root.mainloop()
