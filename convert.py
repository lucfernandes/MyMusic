import os
import setMetaTag

from moviepy.editor import AudioFileClip

def convertToMP3(videoTitle, downloadPath, fileName):
    
    filePath = downloadPath + '/' + fileName
    
    musicFolderPath = os.path.dirname(os.path.abspath(__file__)) + '/musicas'
    
    os.makedirs(musicFolderPath, exist_ok=True)
    
    musicPath = os.path.join(musicFolderPath, (videoTitle).replace("/"," - ") + ".mp3")
    
    if os.path.exists(filePath):
        
        # Converte o MP4 para MP3 para aplicar meta tags.
        mp4WithoutFrames = AudioFileClip(filePath)
        mp4WithoutFrames.write_audiofile(musicPath)
        mp4WithoutFrames.close()
        
        os.remove(filePath)
        
        setMetaTag.setMetaTagDefault(videoTitle, musicPath)