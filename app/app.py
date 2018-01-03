from flask import Flask, render_template, request, session 

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/vishal')
def vishal():
	return render_template('draw.html')

@app.after_request
def add_header(response):
	response.headers['Cache-Control'] = 'public, max-age=0'
	return response

if __name__ == '__main__':
	app.run()