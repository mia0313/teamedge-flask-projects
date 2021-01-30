from flask import Flask, render_template, json, jsonify, request, current_app as app
from datetime import date
import os
import requests

app = Flask(__name__, static_folder="static")
json_info = ''

@app.route('/')
def index():
	name = 'Mia'
	description = "This is my first website made with Flask."
	friends = ['Mira', 'Ally', 'Xavi', 'Charles']
	return render_template('index.html', greeting=name, description=description, friends=friends)

@app.route('/about')
def about():
	return '<h1>About</h1><p>some other content</p>'

@app.route('/api/v1/albums', methods=['GET'])
def album_json():
	album_info = os.path.join(app.static_folder, 'data', 'album.json')
	with open(album_info, 'r') as json_data:
		json_info = json.load(json_data)
		return jsonify(json_info)

@app.route('/album')
def albums():
	album_info = os.path.join(app.static_folder, 'data', 'album.json')
	with open(album_info, 'r') as json_data:
		json_info = json.load(json_data)
	album= json_info[album]
	artist= json_info[artist]
	year= json_info[year]
	songs= json_info[songs]
	return render_template('album.html', album=album, songs=songs, artist=artist, year=year)

@app.route('/nasa')
def show_nasa_pic():
	today = str(date.today())
	response = requests.get('https://api.nasa.gov/planetary/apod?api_key=wjlnR0Xw9B5Sh3WEIJa9kmVd368hNMiUVIGahGPi&date='+today)
	
	data = response.json()
	
	return render_template('nasa.html',data=data)

if __name__ == '__main__':
	app.run(debug=True, host='127.0.0.1')

