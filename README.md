# 🖐️ Gesture-Controlled Keyboard using OpenCV and MediaPipe

This project lets you control your keyboard using hand gestures captured via your webcam. It uses MediaPipe to detect finger positions and simulates keypresses like arrows or spacebar using Python automation.

---

## 🚀 Features

- Real-time hand detection using MediaPipe
- Finger count (0 to 4) determines key press:
  - `0 fingers` → **Spacebar**
  - `1 finger`  → **Left Arrow**
  - `2 fingers` → **Right Arrow**
  - `3 fingers` → **Down Arrow**
  - `4 fingers` → **Up Arrow**
- Visual feedback with finger count overlay
- Simple and portable Python script

---

## 📦 Requirements

Install required packages using:

```bash
pip install -r requirements.txt
