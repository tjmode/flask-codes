from flask import Flask ,render_template,request,url_for,redirect,logging
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)
@app.route("/")
def home():
	return redirect(url_for("login"))

@app.route("/login",methods=["GET","POST"])
def login():
	d=["tony","wilson","aron","wilson123"]
	da=[]
	if request.method == "POST":
		name=request.form.get("name")
		da.append(str(name))
		passw=request.form.get("pass")
		da.append(str(passw))
	c=0
	for i in range(len(da)):
		if da[i] in d:
			c=c+1
	if c==2:
		return redirect(url_for("heloo"))
	else:
		return redirect(url_for("helo1"))


	return render_template("welcome.html")

@app.route("/heloo")
def heloo():
	return render_template("heloo.html")

@app.route("/helo1")
def helo1():
	return render_template("helo1.html")

if __name__ == '__main__':
	app.run(debug=True)

