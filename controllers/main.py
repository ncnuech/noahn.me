#/usr/bin/python
import sys
from flask import Blueprint, render_template
from flask import json
import MySQLdb
from flask import *
import time
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

@main.route('/getCurPlayerOfDay')
def getCurPlayerOfDay():
	records = executeAll("SELECT * FROM curPlayerOfDay ORDER BY id LIMIT 3;")
        #print("_______how formed________")
        players = []
        for i in range(0,len(records)):
        #       print(records[i][0])
        #       print(records[i][1])
        #       print(records[i][2])
                players.append({"day":records[i][1],"name":records[i][2],"url":records[i][3],"stats":records[i][4],"teamPic":records[i][5]})
                response = json.jsonify(players=players,status=200)
        return response

@main.route('/setCurPlayerOfDay')
def setCurPlayerOfDay():
	nameList = request.args.get('message').split('_')
	urlList = request.args.get('url').split('_')
        day = request.args.get('day')
        statsList = request.args.get('stats').split('_')
	teamPicList = request.args.get('teamPic').split('_')
        #print(str(message) + " " + str(url) + " " + str(day))
        for i in range(len(nameList)):
		update("update curPlayerOfDay set day='"+day + "',name='"+nameList[i]+"',url='"+urlList[i]+"',stats='"+statsList[i]+"',teamPic='" + teamPicList[i] + "' where id = " + str(i+1) + ";")
                #update('insert into playerOfDay (day,message,url,stats) values ("'+day+'","'+message + '","' + url+'","' + stats + '");')
        #print(message)
        #print(dateStr)
        return 'OK'


@main.route('/setPlayerOfDay')
def setPlayerOfDay():
	message = request.args.get('message')
	url = request.args.get('url')
	day = request.args.get('day')
	stats = request.args.get('stats')
	#print(str(message) + " " + str(url) + " " + str(day))
	if message != "":
		print(stats)
		update('insert into playerOfDay (day,message,url,stats) values ("'+day+'","'+message + '","' + url+'","' + stats + '");')
	#print(message)
	#print(dateStr)
	return 'OK'

@main.route('/returnPlayersOfDay')
def returnPlayersOfDay():
	records = executeAll("SELECT * FROM playerOfDay ORDER BY id DESC LIMIT 7;")
	#print("_______how formed________")
	players = []
	for i in range(0,len(records)):
	#	print(records[i][0])
	#	print(records[i][1])
	#	print(records[i][2])
		players.append({"day":records[i][1],"name":records[i][2],"url":records[i][3],"stats":records[i][4]})
		response = json.jsonify(players=players,status=200)
	return response

@main.route('/getPhoneForActions')
def getPhoneForActions_route():
	subtype=request.args.get('type')
	if subtype=="action":
		subtype="scoringPlays"
	elif subtype=="playerOfDay":
		subtype="playerOfDay"
	elif subtype=="playerOfWeek":
		subtype="playerOfWeek"
	elif subtype=="weekSummary":
		subtype="weekSummary"
	print("______________________")
	records = executeAll("SELECT phone FROM subscription WHERE " + subtype + " = TRUE;")
	phoneStr = ""
	for record in records:
		print(record)
		phoneStr+=record[0]+" ";
	print(phoneStr)
	if phoneStr != "":
		phoneStr=phoneStr[:-1]
	print("_______________________")
	return phoneStr



@main.route('/getMessage')
def getMessage_route():
	#print("received message from RPI")
	message = request.args.get('message')
	update('UPDATE messages SET message="' + message + '" WHERE name="message";')
	return 'OK'
@main.route('/checkForUpdate')
def checkForUpdate_route():
	#print("returning from checkForUpdate")
	rval = execute('SELECT message FROM messages WHERE name="message";')
	#print(rval)
	if rval==None:
		return ""
	else:
	#	print("returning to JAVASCRIPT")
	#	print(rval[0])
		#update('UPDATE messages SET message="" WHERE name="message";')
		return rval[0]

@main.route('/checkSubscription')
def checkSubscription_route():
	phone = request.args.get('phone')
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
	phone = request.form['phone']
	#phone = data.get('phone')
	name = request.form['name']
	gameUpdates = request.form['scoringPlays']
	playerOfDay = request.form['playerOfDay']
	record = execute("select phone from subscription where phone=" + phone)
		
	print("{}{}{________________}{}{}{}")
	print(playerOfDay)
	if record==None:
		update('insert into subscription values ("'+name+'","'+phone + '",' + gameUpdates+"," + playerOfDay + ",FALSE,FALSE);")
	else:
		update('UPDATE subscription SET name="'+name+'",scoringPlays=' + gameUpdates + ',playerOfDay=' + playerOfDay + ' WHERE phone="' +phone + '";')
	return 'OK'

def execute(query):
	print("Executing a thing")
        con = MySQLdb.connect(host="localhost",user="root",passwd="marcopolo",db="hockey")
        cursor = con.cursor()
        cursor.execute(query)
        newrow = cursor.fetchone()
        con.close()
	return newrow
def executeAll(query):
        print("Executing a thing")
        con = MySQLdb.connect(host="localhost",user="root",passwd="marcopolo",db="hockey")
        cursor = con.cursor()
        cursor.execute(query)
        newrows = cursor.fetchall()
        con.close()
        return newrows

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

