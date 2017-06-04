from flask import Flask
from flask import request
from NLP import CodeSpeak
from trans import translat
import os
import base64
# -*- coding: utf-8 -*-
app = Flask(__name__)

language="C"
NLPFunc = None

app.config['UPLOAD_FOLDER'] = 'uploads/'

app.config['ALLOWED_EXTENSIONS'] = set(['txt','wav', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def ip_process(data):
#Insert IP Function here
    code=""
    return code

def trans_process(data):
#Insert Translate Function here
    trans_data=translat(data)
    return trans_data

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/language',methods=['GET','POST'])
def language():
	global NLPFunc
	language = request.args.get('lang')
	NLPFunc = CodeSpeak(language)
	return "Language set"

@app.route('/translate',methods=['GET','POST'])
def translate():
    data = request.args.get('text')
    s_data= trans_process(data)
    return s_data

@app.route('/vline', methods=['GET', 'POST'])
def vline():
	global NLPFunc
	data = request.args.get('text')
	NLPFunc.blockproc(data)
	#s_code += nlp_process(data)
	return "statement Received"

@app.route('/clear')
def clear():
	global NLPFunc
	NLPFunc.wipeout()
	return "wipeout"

# Final source code is fetched here
@app.route('/voice', methods=['GET', 'POST'])
def voice():
	global NLPFunc
    #data = request.args.get('text')
	NLPFunc.assemble()
	s_code= NLPFunc.get_code()
	return s_code

@app.route('/picture',methods=['GET','POST'])
def picture():

    fileval = request.files['file']
	filename = request.files['filename']
	fh = open("uploads/"+str(filename), "wb")
	fh.write(fileval.decode('base64'))
	fh.close()
	s_code=ip_process(filename)
	return s_code


@app.route('/')
def index():
    return "Hey"

if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)
