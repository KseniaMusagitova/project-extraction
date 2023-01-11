import moviepy.editor
from pathlib import Path


# #1 audio extraction.
# video = moviepy.editor.VideoFileClip('my_video5.mp4')
# audio = video.audio
# audio.write_audiofile('my_audio.mp3')
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


#4 cut video into sub clip.
video = moviepy.editor.VideoFileClip('my_video6.mp4')
clip = video.subclip(0, 10)
clip.write_videofile('my_video7.mp4', fps=60)


