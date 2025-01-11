import tempfile
import os

endpoint = os.environ["CLOUD_LOGGING_INGEST_MTLS_ENDPOINT"]
cert = os.environ["CLOUD_LOGGING_INGEST_MTLS_CERT"]
key = os.environ["CLOUD_LOGGING_INGEST_MTLS_KEY"]


def mtls_client_cert_from_env():
    """takes care of loading the env variables and storing the certificates in a temporary file"""
    cert_str = os.environ["CLOUD_LOGGING_INGEST_MTLS_CERT"]
    key_str = os.environ["CLOUD_LOGGING_INGEST_MTLS_KEY"]

    # Create temporary files to store the cert and key
    with tempfile.NamedTemporaryFile(delete=False) as cert_file, tempfile.NamedTemporaryFile(delete=False) as key_file:
        cert_file.write(cert_str.encode('utf-8'))
        key_file.write(key_str.encode('utf-8'))
        cert_file_path = cert_file.name
        key_file_path = key_file.name

    return (cert_file_path, key_file_path)

def mtls_endpoint_from_env():
    """return endpoint from env variable"""
    return "https://" + os.environ["CLOUD_LOGGING_INGEST_MTLS_ENDPOINT"]