import random
import logging
from flask import Flask, jsonify
from cloud_logging_handler.cloud_logging_handler import CloudLoggingHandler

logger = logging.getLogger("SampleAIApp")
logger.setLevel(logging.DEBUG)

# Set up the custom Cloud Logging handler
cloud_logging_handler = CloudLoggingHandler()  
logger.addHandler(cloud_logging_handler)

logger.info("Init Server!!")

# Initialize FastAPI app
app = Flask(__name__)


@app.route("/v2/predict/", methods=['POST'])
def predict():
    logger.info(f"Request to /v2/predict/")
    logger.info(f"Input Data Recieved, preparing prediction")
    
    prediction = round(random.uniform(0, 1), 2)     # Perform inference using the loaded model
    logger.info(f"Successfully predicted a value: {prediction}")
    
    return jsonify({"prediction": prediction })   # Return the prediction as JSON response
    
@app.route("/v2/hello/", methods=['POST'])
def hello():
    logger.info(f"Request to /v2/hello/")
    logger.info("Hello World!!")
    return jsonify({"world": "hello"})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)    # should not be used in production
    
    
    
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)  # add this one if you want to continut to get logs to the normal console