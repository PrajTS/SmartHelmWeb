from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/<string:userid>")
def emC(userid):
	return render_template('index.html',userid=userid)


if __name__ == '__main__':
	app.run(debug=True)