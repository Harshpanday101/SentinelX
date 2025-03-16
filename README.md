# SentinelX - AI-Powered Crowd Monitoring for Mahakumbh 2025

SentinelX is an **AI-powered real-time surveillance system** designed to enhance **crowd monitoring and security** at **Mahakumbh 2025** using **computer vision and edge AI**. The system enables real-time video streaming from a Raspberry Pi to a laptop, where a YOLOv8 model detects and counts people in the frame.

## 🚀 Features
- **Live Video Streaming**: Transmits real-time video from a Raspberry Pi to a laptop over a network.
- **AI-Based Human Detection**: Uses YOLOv8 for detecting and counting people in the frame.
- **Autonomous Alerts**: Helps authorities track overcrowding and enhance crowd control.
- **Edge AI Processing**: Efficient computing for minimal latency and fast decision-making.

---

## 📌 System Architecture
### 🔹 Transmitter (Raspberry Pi)
- Captures video using a USB camera or Raspberry Pi camera module.
- Streams the video over a network to a receiver.

### 🔹 Receiver (Laptop)
- Receives the video stream from the Raspberry Pi.
- Applies the YOLOv8 model to detect and count people in real time.
- Displays the processed video feed with bounding boxes and count overlay.

---

## 💻 Installation & Setup

### 🔹 Requirements
- **Hardware:** Raspberry Pi 5, USB Camera/Raspberry Pi Camera, Laptop
- **Software:** Python 3, OpenCV, Ultralytics YOLOv8, Socket Programming

### 🔹 Install Dependencies
On the **Raspberry Pi** and **Laptop**, install the required packages:
```bash
pip install opencv-python ultralytics torch torchvision torchaudio pickle-mixin
```

### 🔹 Running the Transmitter (Raspberry Pi)
```bash
python3 transmitter.py
```

### 🔹 Running the Receiver (Laptop)
```bash
python3 receiver.py
```

---

## 📷 YOLOv8 Human Detection & Counting
SentinelX integrates **YOLOv8** for **real-time person detection**. The model processes each video frame and:
- Detects people in the scene.
- Draws bounding boxes around detected persons.
- Counts the number of people in the frame.
- Displays the processed video feed with live count overlay.

![IMG](https://github.com/Harshpanday101/SentinelX/blob/main/Image/img%205.jpg)

![IMG](https://github.com/Harshpanday101/SentinelX/blob/main/Image/img%202.jpg)

![IMG](https://github.com/Harshpanday101/SentinelX/blob/main/Image/img%201.jpg)

---

## 🔥 What's Next?
💡 **Something even crazier is coming soon!** Stay tuned for the next breakthrough in **smart surveillance and autonomous security**! 🚀

---


## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to improve.

## 📬 Contact
For any inquiries or collaborations, reach out via [GitHub](https://github.com/Harshpanday101) or [LinkedIn](www.linkedin.com/in/harshpanday101).

---

**#SentinelX #Mahakumbh2025 #AIForGood #ComputerVision #CrowdMonitoring #Surveillance #IoT #EdgeAI #SmartCity #Innovation**

