from concurrent.futures import ThreadPoolExecutor
import gzip
import os
import json
import logging
import requests

from cloud_logging_handler.secret_utils import mtls_client_cert_from_env, mtls_endpoint_from_env

executor = ThreadPoolExecutor(max_workers=1)

class CloudLoggingHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.endpoint = mtls_endpoint_from_env()
        self.client_cert = mtls_client_cert_from_env()
        self.executor = executor  # Configure the number of worker threads

    def emit(self, record):
        try:
            # Prepare log message payload
            log_message_formatted = self.format(record)
            payload = {
                "msg": log_message_formatted,
                "date": record.created,
                "filename": record.filename,
                "level": record.levelname,
                "thread": record.threadName,
                "deployment_id": os.environ.get("HOSTNAME", "")[:16],  # a env variable set by ai core gives us some info on the deployment_id
                "deployment_name": os.environ.get("DEPLOYMENT_NAME", "")  # a env variable set us to give the workload a name
            }
            # Submit the background task to the ThreadPoolExecutor
            self.executor.submit(self._send_log, payload)
        except Exception as e:
            logging.error(e)

    def _send_log(self, payload):
        try:
            # Convert payload to gzipped JSON
            json_bytes = json.dumps(payload).encode('utf-8')
            gzipped_data = gzip.compress(json_bytes)
            
            # Send the log to the cloud service
            response = requests.put(
                self.endpoint,
                data=gzipped_data,
                headers={'Content-Encoding': 'gzip'},
                cert=self.client_cert
            )
            response.raise_for_status()
        except Exception as e:
            logging.error(e)
