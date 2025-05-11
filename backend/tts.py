

from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import save, play
load_dotenv()

client = ElevenLabs(
  api_key= "sk_ba917cf0377e04f274e02e21d41e7b5a53c1262627456538",
  timeout=120
)


def tts(script):
    # Generate and play audio from text
    audio = client.text_to_speech.convert(
    text=script,
    voice_id="IZl7aMcWb3WnBsxQFo8H",
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
)
    
    save(audio, "output.mp3")
