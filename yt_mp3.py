#https://dev.to/stokry/download-youtube-video-to-mp3-with-python-26p

from pytube import YouTube
import os
from pathlib import Path


def youtube2mp3 (url, outdir):
    # url input from user
    yt = YouTube(url)

    ##@ Extract audio with 160kbps quality from video
    video = yt.streams.filter(abr='160kbps').last()

    ##@ Downloadthe file
    out_file = video.download(output_path=outdir)
    base, ext = os.path.splitext(out_file)
    new_file = Path(f'{base}.mp3')
    os.rename(out_file, new_file)
    ##@ Check success of download
    if new_file.exists():
        print(f'{yt.title} has been successfully downloaded.')
    else:
        print(f'ERROR: {yt.title}could not be downloaded!')

outdir = os.getcwd() + "/Data/kirtan/Basant"
url = "https://www.youtube.com/watch?v=prV6xqFuQq4&ab_channel=SukhjitSukhi"

youtube2mp3(url, outdir=outdir)