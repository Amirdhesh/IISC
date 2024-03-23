from flask import Flask,request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.post('/objectdetection')
def objectdetection():
    file = request.files['image']
    print(file)
    return {"status" : True}



if __name__ == '__main__':
    app.run(debug=True)
