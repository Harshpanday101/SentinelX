import cv2
import socket
import struct
import pickle
import torch
from ultralytics import YOLO


model = YOLO("yolov8n.pt")  

SERVER_IP = '192.168.0.105'  
PORT = 9999


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))

data = b""
payload_size = struct.calcsize("Q")

while True:
    while len(data) < payload_size:
        packet = client_socket.recv(4096)  
        if not packet:
            break
        data += packet

    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("Q", packed_msg_size)[0]

    while len(data) < msg_size:
        data += client_socket.recv(4096)

    frame_data = data[:msg_size]
    data = data[msg_size:]

    frame = pickle.loads(frame_data)

    results = model(frame)

    num_people = 0

    for result in results:
        for box in result.boxes:
            class_id = int(box.cls) 
            if class_id == 0: 
                num_people += 1
                x1, y1, x2, y2 = map(int, box.xyxy[0])  
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  
                cv2.putText(frame, "Person", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


    cv2.putText(frame, f"People Count: {num_people}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)


    cv2.imshow("YOLOv8 Human Detection", frame)

    if cv2.waitKey(1) == ord('q'):
        break

client_socket.close()
cv2.destroyAllWindows()
