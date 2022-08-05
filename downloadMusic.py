import os

from pytube import YouTube
import convert

def downloadYoutubeVideo(urlVideo):
    
    downloadPath = os.path.dirname(os.path.abspath(__file__)) + '/videos'
    
    os.makedirs(downloadPath, exist_ok=True)
    
    ytVideo = YouTube(urlVideo)
        
    videoSelected = ytVideo.streams.filter(only_audio=True).first()
    
    videoSelected.download(downloadPath)
    
    ytVideoFilename = videoSelected.default_filename
    
    convert.convertToMP3(ytVideo.title, downloadPath, ytVideoFilename)
