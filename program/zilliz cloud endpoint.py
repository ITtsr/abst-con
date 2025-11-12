# Connect using a MilvusClient object
from pymilvus import MilvusClient
CLUSTER_ENDPOINT="https://in03-4969f4e73a34796.serverless.gcp-us-west1.cloud.zilliz.com" # Set your cluster endpoint
TOKEN="ee833501d87d20734056e812df9673fdc1b5462fe2be993ea6b8cee62128bb9c41247b648816598cd4ee28287137766ea30b2c5b" # Set your token

# Initialize a MilvusClient instance
# Replace uri and token with your own
client = MilvusClient(
    uri=CLUSTER_ENDPOINT, # Cluster endpoint obtained from the console
    token=TOKEN # API key or a colon-separated cluster username and password
)