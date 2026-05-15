# SpeakSense - Speech Emotion & Sentiment Analysis System

SpeakSense is an AI-powered speech emotion and sentiment analysis application developed using Python, machine learning, and audio processing techniques. The project analyzes speech/audio input to identify emotions and sentiments from human voice data.

---

# Project Overview

The project focuses on:

- Speech/audio processing
- Emotion detection from voice
- Sentiment analysis
- Voice sample handling
- Audio recording and playback
- GUI-based interaction
- Database integration

The system is designed for beginner-to-intermediate level AI and speech processing applications.

---

# Features

- Speech recording
- WAV audio processing
- Sentiment analysis
- Emotion detection
- GUI-based system
- User authentication
- Audio playback
- Database integration
- Voice sample management

---

# Technologies Used

- Python
- Tkinter
- Machine Learning
- NLP
- PyAudio
- Wave Processing
- MySQL
- NumPy
- Scikit-learn

---

# Project Structure

```text
SpeakSense/
│
├── admin1.py
├── Login.py
├── spee.sql
├── pyproject.toml
│
├── male.wav
├── new.wav
├── out.wav
│
├── __pycache__/
└── .idea/
```

---

# Main Modules

## Login.py

Handles:

- User login system
- Authentication
- GUI login interface

---

## admin1.py

Handles:

- Admin dashboard
- User management
- Audio management
- Database interaction

---


# Audio Processing

The project uses WAV audio files for:

- Voice input
- Speech analysis
- Playback operations
- Sentiment prediction

Sample audio files:

- male.wav
- new.wav
- out.wav

---

# Database

Database file:

```text
spee.sql
```

Contains:

- Database schema
- Tables
- User records
- Audio-related information

Import database:

```bash
mysql -u root -p < spee.sql
```

---

# Installation

## Create Environment

```bash
conda create -n speech python=3.10
conda activate speech
```

---

# Install Dependencies

```bash
pip install pyaudio numpy scikit-learn mysql-connector-python
```

If Tkinter is missing:

```bash
pip install tk
```

---

# Run Project

## Start Login System

```bash
python Login.py
```

## Run Admin Panel

```bash
python Admin.py
```

---

# Machine Learning & NLP

The project applies AI techniques for:

- Speech feature analysis
- Emotion classification
- Sentiment prediction
- Audio pattern recognition

---


# Troubleshooting

## PyAudio Installation Error

Install PyAudio wheel manually if installation fails.

---

## Database Connection Error

Check:

- MySQL server is running
- Correct username/password
- Database imported successfully

---

# Author

Developed by Shahil Abbass using Python, NLP, and Machine Learning for speech sentiment and emotion analysis applications using PyCharm.
