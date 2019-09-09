from flask import Flask, render_template
app = Flask(__name__) # creatting the flask class and objrect

@app.route('/')
def home():
	return "hello!!"

@app.route('/message')
def message():
	return render_template('index.html')



#for custom port (127.0.0.1:420)
app.run(host="0.0.0.0", port=420, debug=True)

if __name__== '__main__':
	app.run(debug = True)