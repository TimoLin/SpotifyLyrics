
import sys
import time
import spotipy
import spotipy.util as util
import services as s
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

name = config['client']['name']
client_id = config['client']['client_id']
client_secret = config['client']['client_secret']
scope = config['oauth']['scope']
redirect_uri = config['oauth']['redirect_uri']

token = util.prompt_for_user_token(
        username=name,
        scope=scope,
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri)

is_daemon = True
lag_time = 1.0 # s

if token:
    sp = spotipy.Spotify(auth=token)

    result = sp.current_playback()

    if result is not None:

        is_playing = result['is_playing']

        progress_ms = result['progress_ms']

        device = result['device']['name'] # current playing device

        song = result['item']['name'] # song name

        song_id = result['item']['id'] # song's unique id

        artist = result['item']['artists'][0]['name'] # only get the first artist

        album = result['item']['album']['name'] # alubm name

        # convert the Full width quote to Half width quote
        # in my case, Taylor Swift's "Don't blame me" was "Don’t blame me", so the minilyrics can't find its lyrics
        song = song.replace('’','\'')
        artist = artist.replace('’','\'')

        # get lyrics with timestamps from MiniLyrics
        lyrics, url, service_name, timed = s._minilyrics(artist, song)
        # error message in lyrics if can't get lyrics
        error = "Error: Could not find lyrics."

        if lyrics != error:
            timeline, lrc = s.lyricSplit(lyrics)

        while (is_daemon):
            # update status because search lyrics may take a while
            result = sp.current_playback()

            is_playing = result['is_playing']

            progress_ms = result['progress_ms']

            print('\033[2J\033[2;0H\t♫ \033[1;35m {0} \033[0m - \033[1;32m {1} \033[0m'.format(artist,song))
            while is_playing:
                if (is_daemon == False):
                    # turn off lyrics
                    break
                if lyrics == error:
                    # only show the error message
                    current_line = " >: Don't have lyrics right now :< "
                    print('\033[4;0H\033[K\t \033[1;36m {}\033[0m'.format(current_line))
                    sleep_time=30.0
                    time.sleep(sleep_time)
                    break
                else:
                    if is_playing:
                        for n in range(1,len(timeline)):
                            if progress_ms <= timeline[n] and progress_ms >= timeline[n-1]:
                                #print(progress_ms, lrc[n-1])
                                current_line = lrc[n-1]
                                print('\033[4;0H\033[K\t \033[1;36m {}\033[0m'.format(current_line))
                                # sleep a while [s]
                                sleep_time = abs(timeline[n]-progress_ms)/1000.0+lag_time
                                time.sleep(sleep_time)
                                print('\033[10;0H\033[?25h')
                                break
                    else:
                        current_line = " >: Paused :<"
                        print('\033[4;0H\033[K\t \033[1;36m {}\033[0m'.format(current_line))
                        # if paused, request api every 2.0s to update status
                        sleep_time=60.0
                        time.sleep(sleep_time)

                # update playback status
                result = sp.current_playback()
                if result is not None:
                    is_playing = result['is_playing']
                    progress_ms = result['progress_ms']
                    song = result['item']['name'] # song name
                    _song_id = result['item']['id']
                    artist = result['item']['artists'][0]['name'] # only get the first artist

                    # is still playing this song or not?
                    if is_playing:
                        if _song_id != song_id:
                            # refresh screen
                            print('\033[2J\033[2;0H\t♫ \033[1;35m {0} \033[0m - \033[1;32m {1} \033[0m'.format(artist,song))

                            lyrics, url, service_name, timed = s._minilyrics(artist,song)
                            if lyrics != error:
                                timeline, lrc = s.lyricSplit(lyrics)
                            song_id = _song_id
                    else:
                        break
                else:
                    # result is None, Spotify Client is not opened
                    break
            if (is_daemon):
                if result is not None:
                    if not is_playing:
                        # paused but still opened the Spotify client
                        current_line = " >: Paused :< "
                        print('\033[4;0H\033[K\t \033[1;36m {}\033[0m'.format(current_line))
                        time.sleep(10.0)
                    else:
                        # Spotify is not opened, stop the daemon
                        break
            else:
                current_line = ""
                break
    else:
        current_line = " >: Spotify is sleeping :< "
        print('\033[4;0H\033[K\t \033[1;36m {}\033[0m'.format(current_line))


else:
    current_line =" Can't get token for "+name
    print('\033[4;0H\033[K\t \033[1;36m {}\033[0m'.format(current_line))
