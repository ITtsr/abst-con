# Connect using a MilvusClient object
from pymilvus import MilvusClient
CLUSTER_ENDPOINT="https://in03-4969f4e73a34796.serverless.gcp-us-west1.cloud.zilliz.com" # Set your cluster endpoint
TOKEN="ee833501d87d20734056e812df9673fdc1b5462fe2be993ea6b8cee62128bb9c41247b648816598cd4ee28287137766ea30b2c5b" # Set your token
DB_NAME="conjecture_vector_database"


# Initialize a MilvusClient instance
# Replace uri and token with your own
client = MilvusClient(
    uri=CLUSTER_ENDPOINT, # Cluster endpoint obtained from the console
    token=TOKEN, # API key or a colon-separated cluster username and password
    db_name=DB_NAME
)



def insert_ID_vector(primarykey,vector):
    client.insert(
    collection_name=DB_NAME,
    data={
        'primary_key': primarykey,
        'vector': vector
    }
)


vector=[
        0.6186516144460161,
        0.5927442462488592,
        0.848608119657156,
        0.9287046808231654,
        -0.42215796530168403
    ]

primarykey=4

insert_ID_vector(primarykey,vector)

