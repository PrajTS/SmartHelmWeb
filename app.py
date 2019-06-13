from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/error")
def error():
	return render_template('pageNotFound.html')

@app.route("/hospital/<string:hospitalid>")
def viewAccidents(hospitalid):
	return render_template('viewAccidents.html',hospitalid=hospitalid)

@app.route("/hospital/<string:hospitalid>/<string:userid>")
def viewUserAccidentInfo(hospitalid, userid):
	return render_template('viewAccidentHosp.html', passval = {"hospitalId" : hospitalid, "userId" : userid})

@app.route("/emc/<string:userid>")
def emC(userid):
	return render_template('index.html',userid=userid)

if __name__ == '__main__':
	app.run(debug=True)