#/usr/bin/python
import sys
from flask import Blueprint, render_template
from flask import json
import MySQLdb
from flask import *
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

@main.route('/nhl')
def nhl_route():
	return render_template("nhl.html")


@main.route('/checkSubscription')
def checkSubscription_route():
	phone = request.args.get('phone')
	print("hello")
	print(phone)
	record = execute('Select name,scoringPlays from subscription where phone="'+phone + '";')
	if record==None:
		response = json.jsonify(name='',update="TRUE",status=200)
		return response
	else:
		response = json.jsonify(name=record[0],update=record[1],status=200)
		return response
	return 'OK'

@main.route('/subscription',methods=['POST','GET'])
def subscription_route():
	print("hellohere")
	phone = request.form['phone']
	#phone = data.get('phone')
	name = request.form['name']
	gameUpdates = request.form['scoringPlays']
	record = execute("select phone from subscription where phone=" + phone)
	print(record)
	if record==None:
		update('insert into subscription values ("'+name+'","'+phone + '",' + gameUpdates+",FALSE,FALSE,FALSE);")
	else:
		update('UPDATE subscription SET phone="' + phone + '",name="'+name+'",scoringPlays=' + gameUpdates + ";")
	print("done")
	return 'OK'

def execute(query):
	print("Executing a thing")
        con = MySQLdb.connect(host="localhost",user="root",passwd="marcopolo",db="hockey")
        cursor = con.cursor()
        cursor.execute(query)
        newrow = cursor.fetchone()
        con.close()
	return newrow

def update(query):
	print("updating a thing")
        con = MySQLdb.connect(host="localhost",user="root",passwd="marcopolo",db="hockey")
        cursor = con.cursor()
        cursor.execute(query)
	con.commit()
        con.close()
	return 

@main.route('/test')
def test_route():
	return render_template("test.html")

@main.route('/returnPlaylist')
def return_playlist():
	songlist = []
	artistlist = []
	filelist = []
	songlist.append("Was A Time")
	artistlist.append("Anthony D'Amato")
	filelist.append("wasatime.mp3")
	songlist.append("The Things I Regret")
	artistlist.append("Brandi Carlile")
	filelist.append("TheThingsIRegret.mp3")

	return json.jsonify(songlist=zip(songlist,artistlist,filelist))

