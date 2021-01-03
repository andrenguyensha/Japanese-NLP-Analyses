import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/') 
def content(): 
	with open('grasshopper.txt', 'r') as f: 
		return render_template('content.html', 
text=f.read())


if __name__ == "__main__":        # on running python app.py
    app.run()                     # run the flask app