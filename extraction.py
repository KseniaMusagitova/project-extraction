import moviepy.editor
from pathlib import Path
import wave
import json

from vosk import Model, KaldiRecognizer, SetLogLevel
import word as custom_word


#1 audio extraction.
video = moviepy.editor.VideoFileClip('my_video6.mp4')
audio = video.audio
audio.write_audiofile('my_audio_main.mp3')
#
#
# #2 extracting audio while retaining the title.
# video_file = Path('my_video6.mp4')
# video = moviepy.editor.VideoFileClip(f'{video_file}')
# audio = video.audio
# audio.write_audiofile(f'{video_file.stem}.mp3')
#
#
# #3 cutting a video clip from a video file.
# video = moviepy.editor.VideoFileClip('my_video6.mp4')
# clip = video.cutout(0, 5)
# clip.write_videofile('my_video6.mp4')
#
#
# #4 cut video into sub clip.
# video = moviepy.editor.VideoFileClip('my_video6.mp4')
# clip = video.subclip(0, 10)
# clip.write_videofile('my_video7.mp4', fps=60)

SetLogLevel(-1)
model_path = "models/vosk-model-small-ru-0.22"
audio_filename = "my_audio.wav"

model = Model(model_path)
wf = wave.open(audio_filename, "rb")
rec = KaldiRecognizer(model, wf.getframerate())
rec.SetWords(True)

# get the list of JSON dictionaries
results = []

while True:
    data = wf.readframes(9000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        part_result = json.loads(rec.Result())
        results.append(part_result)
part_result = json.loads(rec.FinalResult())
results.append(part_result)

list_of_words = []
for sentence in results:
    if len(sentence) == 1:
        continue
    for obj in sentence['result']:
        w = custom_word.Word(obj)  # create custom Word object
        list_of_words.append(w)

wf.close()  # close audiofile

# output to the screen
for word in list_of_words:
    print(word.to_string())


