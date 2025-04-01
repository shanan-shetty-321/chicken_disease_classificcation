from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from cnnClassifier.utils.common import decodeImage #to decode the image to base 64 string then again convert to image(encode)
from cnnClassifier.pipeline.predict import PredictionPipeline


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg" #save input as inputimage.jpg formart 
        self.classifier = PredictionPipeline(self.filename)

#default route home page 
@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html') #home page

##route for training the model
@app.route("/train", methods=['GET','POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py") #can also use dvc repro instead of python main.py
    return "Training done successfully!"


#prediction route
@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']  #take image from web app
    decodeImage(image, clApp.filename) #decode the image to base 64 string then again convert to image(encode)
    result = clApp.classifier.predict() #predict the image
    return jsonify(result) # #return the result in json format


if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8080) #local host
    # # app.run(host='0.0.0.0', port=8080) #for AWS
    # app.run(host='0.0.0.0', port=80) #for AZURE