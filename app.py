from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from cnnClassifier.utils.common import decodeImage
from cnnClassifier.pipeline.prediction import PredictionPipeline

# Set environment variables
os.putenv("LANG", "en_US.UTF-8")
os.putenv("LC_ALL", "en_US.UTF-8")

app = Flask(__name__)
CORS(app)

# Create a client application class
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

# Initialize ClientApp
clApp = ClientApp()

@app.route("/", methods=["GET"])
@cross_origin()
def home():
    return render_template("home.html")

@app.route("/service")
@cross_origin()
def service():
    return render_template("index.html")

@app.route("/train", methods=["GET", "POST"])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    return "Training done successfully!"

@app.route("/predict", methods=["POST"])
@cross_origin()
def predictRoute():
    try:
        image = request.json["image"]
        decodeImage(image, clApp.filename)
        result = clApp.classifier.predict()  # This should return "Normal" or "Tumor"
        
        # Return the plain string result, ensuring no object wrapping
        return result  # Directly returning the string "Normal" or "Tumor"
        
    except Exception as e:
        return str(e), 500  # Return error message and HTTP 500 status


if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=8080, debug=True)  # for LOCALHOST
    # app.run(host="0.0.0.0", port=8080)  # for AWS
    app.run(host="0.0.0.0", port=80,debug=True)  # for AZURE
