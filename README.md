# Islamic Deepfake Detector

A Streamlit web app to help detect whether a video might be AI-generated, deepfaked, or manipulated.  
It extracts a thumbnail frame from the uploaded video and sends it to the Hive AI API for analysis.

---

## Features

- Upload MP4, MOV, or MKV video files
- Extract a frame from the video using OpenCV
- Send the frame to Hive AI’s Vision-Language Model API for deepfake/fake content detection
- Display AI analysis results in real time
- Simple and intuitive Streamlit UI

---

## Tech Stack

- Python  
- Streamlit (Web UI)  
- OpenCV (Video frame extraction)  
- Requests (HTTP API calls)  
- Hive AI API (Deepfake/fake content detection)

---

## Setup & Usage

1. Clone the repo:
   ```bash
   git clone https://github.com/moebaker/islamic-deepfake-detector.git
   cd islamic-deepfake-detector
