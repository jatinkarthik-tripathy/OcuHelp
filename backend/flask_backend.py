from flask import Flask,Blueprint,request,render_template,jsonify,Response,send_file
import numpy as np
import json
import base64
import generate_caption as gc

app = Flask(__name__)

@app.route('/api', methods=['GET','POST'])
def apiHome():
    r = request.method
    if(r=="GET"):
        with open("/mnt/f/Projects/OcuHelp/backend/data.json") as f:
            data=json.load(f)
        return data
    elif(r=='POST'):
        with open('image.jpg',"wb") as fh:
            fh.write(base64.decodebytes(request.data))
        captions=gc.generate_captions('image.jpg')
        cap={"captions":captions}
        with open("/mnt/f/Projects/OcuHelp/backend/data.json","w") as fjson:
            json.dump(cap,fjson)
    
    return jsonify({
        "captions":"Refresh again !"
        })  

@app.route('/result')
def sendImage():
    return send_file('image.jpg',mimetype='image/gif')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)