# MyMusic
![tests](https://img.shields.io/badge/Tests-10-red)
![status](https://img.shields.io/badge/Status-stable-green)


Fast download of your playlists music easily!

## Features

1. **Download yours playlist musics from YouTube**: Fast download of your playlists music from YouTube! Just add the link in the code, and run!
2. **Automatic add of meta tags**: Add meta tags in your music files automatically when finish the download

## Instalation
| Type | Package / Requirements | Version | Description |
| --- | -- | -- | -- |
| Language Programming | Python | 3.9.12 | Language |
| Dependence | pytube | 12.1.0 | Download youtube videos |
| Dependence | moviepy | 1.0.3 | Convert to MP3 |
| Dependence | mutagen | 1.45.1 | Add metatags |

## Usage

To use the My Music, first install the language programming Python and the dependencies what are listed above in the table.

Add the url of your YouTube playlist in the code.
In file `index.py`, add your url how the example.

```python
urlPlaylist = [
    "https://youtube.com/playlist?list=PLXohY8g5ZvptMIV8taTcm3y_aGWl1mHCq",
    # Add your playlist url here.
]

```

> I recommend to you listen this playlist.<br>**Jesus loves you**

After installation, run in your terminal:

```shell
python3 ./index.py
```

When runned, the code will download your playlists music in a folder called by "musicas".


## Licence

MIT