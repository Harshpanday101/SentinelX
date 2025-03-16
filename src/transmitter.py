import cv2
import socket
import struct
import pickle


SERVER_IP = '0.0.0.0'  
PORT = 9999


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, PORT))
server_socket.listen(1)

print(f"[*] Waiting for a connection on {SERVER_IP}:{PORT}...")
conn, addr = server_socket.accept()
print(f"[+] Connected to {addr}")


cap = cv2.VideoCapture(0)  

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    data = pickle.dumps(frame)
    msg_size = struct.pack("Q", len(data))  


    conn.sendall(msg_size + data)

cap.release()
conn.close()
server_socket.close()
