

from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import save, play
load_dotenv()

client = ElevenLabs(
  api_key= "...",
  timeout=120
)


def tts(script):
    
    audio = client.text_to_speech.convert(
    text=script,
    voice_id="IZl7aMcWb3WnBsxQFo8H",
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
)
    
    save(audio, "output.mp3")
