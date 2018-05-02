import json
from flask import Flask, jsonify, render_template, request


app = Flask(__name__)


with open('music_data.json') as json_data:
    d = json.load(json_data)
    list_of_music = []
    for data in d['music']:
    	list_of_music.append(data)


@app.route('/', methods =['GET'])
def test():
	return render_template("index.html")

@app.route('/music', methods =['GET'])
def test1():
	return render_template("index.html",list_data=list_of_music)

@app.route('/music/<string:idd>', methods =['GET'])
def test2(idd):
	g = [music for music in list_of_music if music['id'] == idd]
	return render_template("index.html",list_data=g)


@app.route('/music/<string:idd>', methods =['GET'])
def test3(idd):
	g = [music for music in list_of_music if music['Artist'] == idd]
	return render_template("index.html",list_data=g)

@app.route('/music/<string:idd>', methods =['GET'])
def test4(idd):
	g = [music for music in list_of_music if music['Song'] == idd]
	return render_template("index.html",list_data=g)


if __name__ == '__main__':
	 app.run(debug=True, host='0.0.0.0')