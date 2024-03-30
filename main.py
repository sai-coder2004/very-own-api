from flask import Flask,request
from collections import namedtuple
from datetime import date
from time import time
app=Flask(__name__)
@app.route('/')
def index():
    return{'Test':'This is an example',
           'Date':date.today(),
           'Timestamp':time()}
@app.route('/chat')
def chat():
    user_input:str=request.args.get('input')
    response:Response=generate_response(user_input)
    json={
        'input':user_input,
        'resonse':response.response,
        'accuracy':response.accuracy
    }
    return json

Response=namedtuple('Response','response accuracy')


def generate_response(user_input:str)->Response:
    lc_input:str=user_input.lower()
    if lc_input=='hello':
        return Response('Hey there',1)
    elif lc_input=='goodbye':
        return Response('See you later',1)
    else:
        return Response('Could not understand',0)
if __name__ == '__main__':
    app.run()