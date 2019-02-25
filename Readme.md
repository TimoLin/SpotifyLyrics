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
Related pip packages: `spotipy` `beautifulsoup4` `requests` `xmltodict` `psutil` `unidecode`.  
```shell
pip3 install spotipy beautifulsoup4 requests xmltodict psutil unidecode
```  
For spotipy, the pip package is out of date. Install it through github:  
```shell
pip3 install git+https://github.com/plamere/spotipy.git --upgrade
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
## Acknowledgement
- [fr31/spotifylyrics](https://github.com/fr31/spotifylyrics)  
> Thanks to fr31, the lyrics.py and services.py are copied from this project  

- [spotipy](https://github.com/plamere/spotipy)
> A light weight Python library for the Spotify Web API. [Docs of spotipy](http://spotipy.readthedocs.org/)

## Todo list
- [ ] Add more lyrics search api like `Neatease`, `Xiami`
- [ ] Re-consider synced lyrics implementation to improve performence
- [ ] Save lyrics to local drive and first check local lyrics
- [ ] Exception handling
