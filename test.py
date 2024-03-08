from flask import Flask

app = Flask(__name__)

@app.route('/test')
def index():
	return "hello word"
	
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)
