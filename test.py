import spotipy
name = '2Cellos'
spotify = spotipy.Spotify()
results = spotify.search(q='artist:' + name, type='artist')
print(results)
