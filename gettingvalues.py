from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('hi.html')

@app.route('/' , methods=['POST'])
def getvalue():
	d=[]
	name = request.form['name']
	if name=='A':
			d.append(1)
	ps=request.form['password']
	if ps=='A':
		d.append(1)
	d=sum(d)
	return render_template('paas.html',n=d)

if __name__ == '__main__':
	app.run(debug=True)
