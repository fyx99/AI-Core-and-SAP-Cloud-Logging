import base64
import json

secrets = {
    "CLOUD_LOGGING_INGEST_MTLS_CERT": "-----BEGIN CERT....IFICATE-----\n",
    "CLOUD_LOGGING_INGEST_MTLS_ENDPOINT": "ingest-mtls-sf....hana.ondemand.com",
    "CLOUD_LOGGING_INGEST_MTLS_KEY": "-----BEGIN PRIVA....---END PRIVATE KEY-----\n"
}
def base64_encode(value):
    encoded_bytes = base64.b64encode(value.encode('utf-8'))
    encoded_str = encoded_bytes.decode('utf-8')
    return encoded_str

encoded_secrets = {key: base64_encode(value) for key, value in secrets.items()}    # Base64 encode all the values in the secrets dictionary

print(json.dumps(encoded_secrets))