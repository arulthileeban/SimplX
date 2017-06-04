from flask import Flask
from flask import request
import os
app = Flask(__name__)

language="C"

s_code = ""

app.config['UPLOAD_FOLDER'] = 'uploads/'

app.config['ALLOWED_EXTENSIONS'] = set(['txt','wav', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def nlp_process(data):
#Insert NLP Function here
	code=""
	return code

def ip_process(data):
#Insert IP Function here
	code=""
	return code

def trans_process(data):
#Insert Translate Function here
	trans_data=""
	return trans_data

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/language',methods=['GET','POST'])
def language():
	global language
	language = request.args.get('lang')
	return "hey"

@app.route('/translate',methods=['GET','POST'])
def translate():
    data = request.args.get('text')
    s_data= trans_process(data)
    s_code=nlp_process(data)
    return s_code

@app.route('/vline', methods=['GET', 'POST'])
def vline():
    data = request.args.get('text')
    s_code += nlp_process(data)
    return s_code

@app.route('/clear')
def clear():
	s_code=""
	return s_code

@app.route('/voice', methods=['GET', 'POST'])
def voice():
    data = request.args.get('text')
    s_code= nlp_process(data)
    return s_code

@app.route('/picture',methods=['GET','POST'])
def picture():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename=file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        s_code=ip_process(filename)
        return s_code


@app.route('/')
def index():
    return "Hey"

if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)
