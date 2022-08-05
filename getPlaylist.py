from pytube import Playlist

import re
import downloadMusic

def getMusicUrlOfPlaylist(urlPlaylists):

    urls = []
    
    for playlist in urlPlaylists:
        
        # Busca playlist
        playlist = Playlist(playlist)
        # Corrige o erro da lista vázia
        playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
                
        for video in playlist:
            
            downloadMusic.downloadYoutubeVideo(video)