import spotipy
from spotipy import util
from pprint import pprint
name = 'Run'


token = util.prompt_for_user_token("eeeebta", scope='playlist-modify-private,playlist-modify-public', client_id='e60c633355494fbd8617730255800a61', client_secret='8b820c62c9fb4e71a5cff63281079c01', redirect_uri='http://localhost:8080')
spotify = spotipy.Spotify(token)

results = spotify.search(q=name)

grab_result = results["tracks"]["items"][0]["external_urls"]

pprint(grab_result)
