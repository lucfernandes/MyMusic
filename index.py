import getPlaylist

# Recebe a url da playlist pública
urlPlaylist = [
    "https://youtube.com/playlist?list=PLXohY8g5ZvptMIV8taTcm3y_aGWl1mHCq"
]

# Busca no yt a url das músicas da playlist
urlList = getPlaylist.getMusicUrlOfPlaylist(urlPlaylist)

print(urlList)
