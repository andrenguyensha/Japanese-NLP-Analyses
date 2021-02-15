import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import analysis
import past_present_output

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/getfile', methods=['GET','POST'])
def getfile():
    if request.method == 'POST':

        # for secure filenames. Read the documentation.
        file = request.files['myfile']
        filename = secure_filename(file.filename) 

        # os.path.join is used so that paths work in every operating system
        file.save(os.path.join("wherever","you","want",filename))

        # You should use os.path.join here too.
        with open("wherever/you/want/filename") as f:
            file_content = f.read()

        return file_content     


    else:
        result = request.args.get['myfile']
    return result

@app.route()
def run_analysis():
    file = open(r'analysis.py', 'r').read()  # Want flask app to show analysis.py output
    return exec(file)


@app.route()
def run_output():
    file = open(r'past_present_output.py', 'r').read() # Want flask app to show the past_present_output.py output
    return exec(file)

if __name__ == "__main__":
    app.run()