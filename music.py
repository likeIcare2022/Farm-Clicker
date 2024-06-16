from pydub import AudioSegment
from pydub.playback import play

while True:
    play(AudioSegment.from_mp3("Farm Music.mp3"))
