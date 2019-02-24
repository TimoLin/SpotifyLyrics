SpotifyLyrics
=============
This is a python script to show synced lyrics of your current playing song in Spotify at terminal.  

## Features  

- Show synced lyrics line by line
- No matter what device Spotify are connecting 

## requirements
This repo requires `python3`. 
Related pip packages: `spotipy` `beautifulsoup4` `requests` `xmltodict` `psutil` `unidecode`.  
```shell
pip3 install spotipy beautifulsoup4 requests xmltodict psutil unidecode
```  
For spotipy, the pip package is out of date. Install it through github:  
```shell
pip3 install git+https://github.com/plamere/spotipy.git --upgrade
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
> A light weight Python library for the Spotify Web API. [spotipy doc](http://spotipy.readthedocs.org/)

## Todo list
- [ ] Add more lyrics search api like `Neatease`, `Xiami`
- [ ] Re-consider synced lyrics implementation to improve performence
- [ ] Save lyrics to local drive and first check local lyrics
