from flask import Flask

app = Flask(__name__) # creatting the flask class and objrect

#for custom port (127.0.0.1:420)
app.run(host="0.0.0.0", port=420, debug=True)

if __name__== '__main__':
	app.run(debug = True)