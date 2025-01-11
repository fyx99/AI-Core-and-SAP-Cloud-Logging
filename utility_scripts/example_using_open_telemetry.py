"""this is a sample unrelated to the blog post that uses open telemetry - it works and the hard part is to figure out how to setup the mtls stuff - this is for traceing, theoretically one would need the example for regular logs as well"""


from grpc import ssl_channel_credentials
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
import logging
logging.basicConfig(level=logging.DEBUG)

grpc_logger = logging.getLogger("grpc")
grpc_logger.setLevel(logging.DEBUG)



trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

CLIENT_CERT = "oltp-client.crt"
CLIENT_KEY = "oltp-client.key"
SERVER_CA = "server-ca.crt"

with open(CLIENT_CERT, 'rb') as cert_file, \
        open(CLIENT_KEY, 'rb') as key_file, \
        open(SERVER_CA, 'rb') as ca_file:
    client_cert = cert_file.read()
    client_key = key_file.read()
    ca_cert = ca_file.read()

# Create SSL/TLS credentials
credentials = ssl_channel_credentials(
    root_certificates=ca_cert,
    private_key=client_key,
    certificate_chain=client_cert,
)


otlp_exporter = OTLPSpanExporter(endpoint="https://ingest-otlp-sf-db275af0-25c2-4ebf-902a-c40382441b6c.cls-01.cloud.logs.services.sap.hana.ondemand.com:443", credentials=credentials, insecure=True)

span_processor = BatchSpanProcessor(otlp_exporter)

trace.get_tracer_provider().add_span_processor(span_processor)

with tracer.start_as_current_span("foo") as span:
    # Set attributes to the span
    token_count = 422  # Example token count
    span.set_attribute("token_count", token_count)
    span.set_attribute("model_name", "gpt4")
    print("Hello world! see the number of tokens")