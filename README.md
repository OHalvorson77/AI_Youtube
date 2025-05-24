# AI_Youtube

🎬 AutoVideoCreator
Generate and upload narrated video content from a single prompt — fully automated.

Powered by: Groq + ElevenLabs + ChatGPT + Pexels API + YouTube API + React + Python

🧠 Project Overview
AutoVideoCreator is a full-stack project that lets you enter a topic into a React app, which triggers a Python backend workflow that:

Sends the topic to Groq for fast script generation.

Converts the script into spoken audio using ElevenLabs in your own voice.

Extracts key topics and keywords using ChatGPT.

Fetches relevant stock video clips from Pexels API.

Compiles the audio and stock footage into a cohesive MP4 video.

Uploads the finished video to your YouTube channel.

🛠️ Tech Stack
Layer	Technology Used
Frontend	React
Backend	Python (Flask / FastAPI)
AI Model	Groq (for script)
Audio	ElevenLabs (voice synthesis)
NLP	ChatGPT (OpenAI API)
Video	Pexels API (stock footage)
Editing	MoviePy (Python)
Uploading	YouTube Data API v3

🚀 Workflow
User Input

You enter a topic into a custom React frontend.

Script Generation

Topic is sent to Groq API to generate a concise, engaging script.

Voice Generation

The script is converted into an MP3 using your ElevenLabs custom voice.

Keyword Extraction

ChatGPT analyzes the script and extracts key visual keywords.

Stock Footage Fetching

Each keyword is sent to the Pexels API to retrieve short video clips.

Video Compilation

Python combines the audio with the retrieved footage using MoviePy into a single MP4.

Upload to YouTube

The video is uploaded to your YouTube channel with an auto-generated title, description, and tags.

