from pytube import YouTube
import os

link = input("Link: ")
video = YouTube(link, use_oauth=True, allow_oauth_cache=True)
title = video.title
endswith = ".mp4"
newtitle = video.title + "mp4"
stream = video.streams.get_by_itag(140)
stream.download()
for i in os.listdir():
    if i.endswith(endswith):
        d = i
os.rename(d, title + ".mp3")