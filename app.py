from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/hospital/<string:hospitalid>")
def viewAccidents(hospitalId):
	return render_template('viewAccidents.html')

@app.route("/hospital/<string:hospitalid>/<string:userid>")
def viewUserAccidentInfo(hospitalid, userid):
	return render_template(viewUserAccidentInfo.html, hospitalid = hospitalid, userid = userid)

@app.route("emc/<string:userid>")
def emC(userid):
	return render_template('index.html',userid=userid)


if __name__ == '__main__':
	app.run(debug=True)