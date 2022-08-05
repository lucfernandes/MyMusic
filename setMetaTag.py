from mutagen.id3 import ID3, TIT2

import os

def setMetaTagDefault(videoTitle, musicPath):
    
    if os.path.exists(musicPath):
        
        tags = ID3(musicPath)
        
        tags["TIT2"] = TIT2(enconding = 3, text=videoTitle)
        
        tags.save()