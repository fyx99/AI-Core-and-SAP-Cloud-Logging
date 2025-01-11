from flask import Flask, jsonify
import random
import os
import logging

from cloud_logging_handler.cloud_logging_handler import CloudLoggingHandler

logger = logging.getLogger("SampleAIApp")
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)  # add this one if you want to continut to get logs to the normal console
# # Set up the custom HTTP handler
cloud_logging_handler = CloudLoggingHandler()   # add to send to cloud logging
logger.addHandler(cloud_logging_handler)


# Get all environment variables
env_vars = os.environ

# Print each environment variable
for key, value in env_vars.items():
    logger.info(f"{key}: {value}")


logger.info("Init Server!!")
print("Init Server!")
# Initialize FastAPI app
app = Flask(__name__)


# Define a POST endpoint for model inference
@app.route("/v2/predict/", methods=['POST'])
def predict():
    logger.info(f"Input Data Recieved, preparing prediction")
    
    # Perform inference using the loaded model
    prediction = round(random.uniform(0, 1), 2)
    logger.info(f"Successfully predicted a value: {prediction}")
    
    # Return the prediction as JSON response
    return jsonify({"prediction": prediction })

@app.route("/v2/hello/", methods=['POST'])
def hello():
    logger.info("Hello World!!")
    return jsonify({"world": "hello"})


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8880)    # should not be used in production