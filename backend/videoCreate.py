import os
from moviepy import VideoFileClip, AudioFileClip, concatenate_videoclips



def videoCreate():
    # --- Configuration ---
    STOCK_FOLDER = "stock_clips"  # Folder with your .mp4 stock clips
    AUDIO_PATH = "output.mp3"  # Your ElevenLabs narration
    OUTPUT_PATH = "final_video.mp4"
    CLIP_DURATION = 8  # seconds per clip

    # --- Load audio ---
    audio = AudioFileClip(AUDIO_PATH)
    audio_duration = audio.duration

    # --- Load and trim stock video clips to 8 seconds each ---
    clip_paths = [os.path.join(STOCK_FOLDER, f) for f in os.listdir(STOCK_FOLDER) if f.endswith(".mp4")]
    stock_clips = []

    
    for path in clip_paths:
        try:
            clip = VideoFileClip(path)
            trimmed = clip.subclipped(0, min(8, clip.duration))
            stock_clips.append(trimmed)
        except Exception as e:
            print(f"Skipping {path} due to error: {e}")

    # --- Loop through videos until audio is covered ---
    final_clips = []
    current_time = 0
    index = 0

    while current_time < audio_duration:
        clip = stock_clips[index % len(stock_clips)].copy().with_duration(CLIP_DURATION)
        final_clips.append(clip)
        current_time += CLIP_DURATION
        index += 1

    # --- Concatenate and add audio ---
    video = concatenate_videoclips(final_clips).with_duration(audio_duration)
    video = video.with_audio(audio)

    # --- Export the video ---
    video.write_videofile(OUTPUT_PATH, codec="libx264", audio_codec="aac", fps=24)
