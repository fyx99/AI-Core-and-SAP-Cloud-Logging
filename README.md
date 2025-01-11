# SAP AI Core: Consolidate Logs with SAP Cloud Logging

This repository demonstrates how to send logs from SAP AI Core deployments to SAP Cloud Logging for a unified view of your AI workloads and applications. It uses a custom logging handler implemented in Python to send logs to the SAP Cloud Logging service.

## Blog Reference  

This repository is a companion to the SAP Community blog post:  
**[SAP AI Core: Consolidate Logs with SAP Cloud Logging](https://community.sap.com/t5/technology-blogs-by-sap/monitor-token-usage-with-sap-generative-ai-hub/ba-p/13979768)**  


## Prerequisites

Before you begin, you will need the following:
1. An instance of **SAP AI Core** deployed on SAP Business Technology Platform (BTP).
2. An instance of **SAP Cloud Logging** on BTP.
3. A service key for both SAP AI Core and SAP Cloud Logging services.

You can refer to the official documentation to set up both services. The service key for Cloud Logging will be used to authenticate your logs and includes details such as certificates and endpoints.

## Installation

### 1. Clone the Repository

Start by cloning this repository to your local machine:

```bash
git clone https://github.com/your-username/sap-ai-core-logging-example.git
cd sap-ai-core-logging-example
```

### 2. Install Python Dependencies

You will need Python 3.x installed. The required dependencies can be installed using `pip`:

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Set the following environment variables using the Cloud Logging service credentials from the service key:

```bash
export CLOUD_LOGGING_INGEST_MTLS_ENDPOINT="your-ingest-mtls-endpoint"
export CLOUD_LOGGING_INGEST_MTLS_CERT="your-ingest-mtls-cert"
export CLOUD_LOGGING_INGEST_MTLS_KEY="your-ingest-mtls-key"
```

These credentials and variables are necessary for the log ingestion process and mTLS authentication.

### 4. Debug

Start the Flask application locally or in your AI Core environment. This application will simulate an AI service and log events.

```bash
python serve.py
```

The Flask app exposes two endpoints:

- `POST /v2/predict/`: Simulates model inference and logs predictions.
- `POST /v2/hello/`: A simple endpoint that logs a greeting.

### 5. Dockerization

To containerize the application, use the provided `Dockerfile` to build and run a Docker container:

```bash
docker build -t cloudlogging-example .
docker run -p 8080:8080 cloudlogging-example
```

### 6. Send Logs to SAP Cloud Logging

The custom logging handler, `CloudLoggingHandler`, is responsible for sending logs to the SAP Cloud Logging service. It uses the mTLS certificates for authentication and gzips the log payload before sending it to the ingest endpoint.

To use the custom handler in your project:

```python
import logging
from cloud_logging_handler.cloud_logging_handler import CloudLoggingHandler

logger = logging.getLogger("SampleAIApp")
logger.setLevel(logging.DEBUG)

cloud_logging_handler = CloudLoggingHandler()
logger.addHandler(cloud_logging_handler)

logger.info("This is an info message")
logger.error("This is an error message")
```

## License  

This project is licensed under the [MIT License](LICENSE).  

