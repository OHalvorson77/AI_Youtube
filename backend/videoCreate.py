import os
from moviepy import VideoFileClip, AudioFileClip, concatenate_videoclips



def videoCreate():
    
    STOCK_FOLDER = "stock_clips"  # Folder with your .mp4 stock clips
    AUDIO_PATH = "output.mp3"  # Your ElevenLabs narration
    OUTPUT_PATH = "final_video.mp4"
    CLIP_DURATION = 8  # seconds per clip

    
    audio = AudioFileClip(AUDIO_PATH)
    audio_duration = audio.duration

    
    clip_paths = [os.path.join(STOCK_FOLDER, f) for f in os.listdir(STOCK_FOLDER) if f.endswith(".mp4")]
    stock_clips = []

    
    for path in clip_paths:
        try:
            clip = VideoFileClip(path)
            trimmed = clip.subclipped(0, min(8, clip.duration))
            stock_clips.append(trimmed)
        except Exception as e:
            print(f"Skipping {path} due to error: {e}")

    
    final_clips = []
    current_time = 0
    index = 0

    while current_time < audio_duration:
        clip = stock_clips[index % len(stock_clips)]
    
        
        trimmed_clip = clip.subclipped(0, min(CLIP_DURATION, clip.duration)).resized(height=720).with_fps(24)
    
        final_clips.append(trimmed_clip)
        current_time += CLIP_DURATION
        index += 1



    
    video = concatenate_videoclips(final_clips, method="compose").with_duration(audio_duration)
    video = video.with_audio(audio)

    
    video.write_videofile(OUTPUT_PATH, codec="libx264", audio_codec="aac", fps=24)
