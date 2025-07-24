import streamlit as st
import tempfile
import os
import random
import requests
import cv2  # OpenCV for frame extraction

st.set_page_config(page_title="Islamic Deepfake Detector", layout="centered")
st.title("🧠 Islamic Video Authenticity Checker")
st.write("Upload a video to check if it might be AI-generated, deepfaked, or manipulated.")

uploaded_file = st.file_uploader("Upload Video File (MP4, MOV)", type=["mp4", "mov", "mkv"])

if uploaded_file:
    # Save uploaded video to a temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    st.video(uploaded_file)

    # --- STEP 1: Extract a frame (thumbnail) ---
    st.info("🎥 Extracting a frame from the video...")
    cap = cv2.VideoCapture(tmp_path)
    success, frame = cap.read()
    frame_path = "frame.jpg"
    if success:
        cv2.imwrite(frame_path, frame)
        st.image(frame_path, caption="Frame from video", use_column_width=True)
    cap.release()

    # --- STEP 2: Simulate Upload (you'll replace this with real hosting) ---
    st.info("🖼️ Sending frame to Hive API for analysis...")

    # This is where your Hive API call goes:
    hive_api_key = "6HY/Om18iH+UyOXphpokRQ=="  # Replace this
    url = "https://api.thehive.ai/api/v3/chat/completions"
    headers = {
        "authorization": f"Bearer {hive_api_key}",
        "Content-Type": "application/json"
    }

    # TEMP: Simulate using their hosted example image (replace later)
    image_url = "https://d24edro6ichpbm.thehive.ai/example-images/vlm-example-image.jpeg"

    data = {
        "model": "hive/moderation-11b-vision-language-model",
        "max_tokens": 1000,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Does this image look fake, AI-generated, or inappropriate?"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url  # 👈 Replace this with uploaded frame URL in future
                        }
                    }
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        st.success("✅ Hive API response received")
        st.json(result)
    else:
        st.error(f"Error from Hive API: {response.status_code}")
        st.text(response.text)

    # Cleanup
    os.remove(tmp_path)
    if os.path.exists(frame_path):
        os.remove(frame_path)
