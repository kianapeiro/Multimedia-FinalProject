import ffmpeg
import os

input_file = 'static/media/movie4.mp4'
output_directory = 'static/media/movie4/dash/'

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

representations = [
    (256, 144, '95k', '64k'),
    (426, 240, '150k', '94k'),
    (640, 360, '276k', '128k'),
    (854, 480, '750k', '192k'),
    (1280, 720, '2048k', '320k'),
    (1920, 1080, '4096k', '320k'),
    (2560, 1440, '6144k', '320k'),
    (3840, 2160, '17408k', '320k')
]

for width, height, video_bitrate, audio_bitrate in representations:
    output_file = os.path.join(output_directory, f'{width}x{height}.mp4')
    (
        ffmpeg
        .input(input_file)
        .output(output_file, vf=f'scale={width}:{height}', video_bitrate=video_bitrate, audio_bitrate=audio_bitrate, format='mp4')
        .run()
    )

inputs = [
    ffmpeg.input(os.path.join(output_directory, '256x144.mp4')),
    ffmpeg.input(os.path.join(output_directory, '426x240.mp4')),
    ffmpeg.input(os.path.join(output_directory, '640x360.mp4')),
    ffmpeg.input(os.path.join(output_directory, '854x480.mp4')),
    ffmpeg.input(os.path.join(output_directory, '1280x720.mp4')),
    ffmpeg.input(os.path.join(output_directory, '1920x1080.mp4')),
    ffmpeg.input(os.path.join(output_directory, '2560x1440.mp4')),
    ffmpeg.input(os.path.join(output_directory, '3840x2160.mp4'))
]

ffmpeg.output(*inputs, os.path.join(output_directory, 'dash.mpd'), f='dash', use_timeline=1, use_template=1, init_seg_name='init_$RepresentationID$.m4s', media_seg_name='chunk_$RepresentationID$_$Number$.m4s').run()
