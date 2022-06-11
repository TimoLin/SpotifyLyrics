SpotifyLyrics
=============
This is a python script to show synced lyrics of your current playing song in Spotify at terminal.  

## Features  
- Show synced lyrics line by line
- No matter what device Spotify are connecting 

## Demo  
![Demo](https://i.imgur.com/j1A5h8a.gif)

## requirements
### python
This repo requires `python3`. 
Related pip packages: `spotipy` `lrc_kit` `beautifulsoup4` `requests` `xmltodict` `psutil` `unidecode`.  
```shell
pip3 install -r requirements.txt
```  
### Spotify  
This feature needs Spotify `authorization_code` to get your current playback status. The scope is `user-read-playback-state`. Detailed information about this can be found at [Spotify for Developer](https://developer.spotify.com/documentation/general/guides/authorization-guide/#authorization-code-flow).  
1. Create an application at [Developer Dashboard](https://developer.spotify.com/dashboard/applications).  
2. Put the `Client ID` and `Client Secret` of the app to `config.ini`.
  - For example:
```ini
[client]
name = taytay
client_id= 1234567890123456789
client_secret = abcdefghijklmnopqrst

[oauth]
scope = user-read-playback-state
redirect_uri = http://localhost/callback/
```

## How to use?  
Clone this repository:  
```shell
git clone git@github.com:TimoLin/SpotifyLyrics.git
```
Run in your terminal after you play a song in Spotify on any device:  
```shell
python3 SpotifyLyrics.py  
```
The lyrics source can be changed by changing this line:
```python
lyricsProvider = [lrc_kit.QQProvider]
```
Available providers can be found at [reteps/lrc_kit/provider.py](https://github.com/reteps/lrc_kit/blob/master/lrc_kit/providers.py) as follows and just select one of them:
```python
MINIMAL_PROVIDERS = [
    SogeciProvider,
    Music163Provider,
    QQProvider,
    KugeciProvider,
    SyairProvider, # Very slow, but contains most sources
]
PROVIDERS = MINIMAL_PROVIDERS + [
    RentanaAdvisorProvider,
    MegalobizProvider
]

EXTENDED_PROVIDERS = PROVIDERS + [
    MooflacProvider, # Uses an email/password
    Flac123Provider # Uses an email/password
]

ALL_PROVIDERS = EXTENDED_PROVIDERS + [
    LyricFindProvider, # Requires a valid API Key
    KugouProvider, # Provides little english lyrics
    XiamiProvider # Was taken offline 2/4.
]
```

## Acknowledgement
- [reteps/lrc_kit](https://github.com/reteps/lrc_kit) & [reteps/lrc_kit](https://github.com/reteps/lrc_kit)
> Thanks to reteps, `lrc_kit` has implemented many lyrics source providers method. 

- [spotipy](https://github.com/plamere/spotipy)
> A light weight Python library for the Spotify Web API. [Docs of spotipy](http://spotipy.readthedocs.org/)

- [fr31/spotifylyrics](https://github.com/fr31/spotifylyrics)  
> Thanks to fr31, the lyrics.py and services.py are copied from this project.


## Todo list
- [x] Add more lyrics search api like `Neatease`, `Xiami`
- [ ] Re-consider synced lyrics implementation to improve performence
- [ ] Save lyrics to local drive and first check local lyrics
- [ ] Exception handling
