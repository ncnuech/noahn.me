#/usr/bin/python
from flask import Blueprint, render_template
from flask import json
main = Blueprint('main', __name__, template_folder='views')

@main.route('/hello')
def main_route():
	return render_template("index.html")

@main.route('/')
def personal_route():
	return render_template("static_website.html")

@main.route('/playlist')
def playlist_route():
	return render_template("playlist.html")

@main.route('/playlistnew')
def playlistnew_route():
        return render_template("musicplayer.html")


@main.route('/returnPlaylist')
def return_playlist():
	songlist = []
	songlist.append("Was A Time")
	songlist.append("Wildfire")
	return json.jsonify(songlist=songlist)

