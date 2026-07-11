# Motion Detection AI

A real-time motion detection system built with Python and OpenCV.

The project detects motion from a surveillance camera or video file, highlights moving objects, and records video when motion is detected.

---

## Features

* Motion Detection using Frame Difference
* Video Recording
* Camera Mode
* Video File Mode
* Bounding Box Visualization
* Modular Architecture
* Configurable Parameters

---

## Project Structure

```text
Motion_Detection_AI

├── main_camera.py
├── main_video.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── videos
├── recordings
│
└── src
    ├── detector.py
    ├── recorder.py
    └── __init__.py
```

---

## Installation

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run with a video file:

```bash
python main_video.py
```

Run with a camera:

```bash
python main_camera.py
```

---

## Architecture

The project follows a modular architecture.

### main_video.py

Responsible for coordinating the application workflow.

### detector.py

Responsible for motion detection.

### recorder.py

Responsible for video recording.

### config.py

Responsible for project configuration.

---

## Future Improvements

* Email Notification
* Logging System
* Screenshot Capture
* Background Subtraction (MOG2)
* YOLO Object Detection
* Telegram Notification
* Django Dashboard

---

## Author

Computer Vision and AI Project
