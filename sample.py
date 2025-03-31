import os
from astrapy.db import AstraDB
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the client with your API endpoint and token
db = AstraDB(
    api_endpoint="https://c0ec76ed-e7be-40d3-922d-232136da75c3-us-east-2.apps.astra.datastax.com",
    token=os.getenv("ASTRA_DB_APPLICATION_TOKEN")
)

# Select a collection to work with
collection = db.collection("pydantic_concepts")

# Insert a single document
doc = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "age": 30
}
result = collection.insert_one(doc)
print(f"Inserted document with ID: {result.inserted_id}")

# Insert multiple documents
docs = [
    {"name": "Jane Smith", "email": "jane.smith@example.com", "age": 28},
    {"name": "Bob Johnson", "email": "bob.johnson@example.com", "age": 35}
]
result = collection.insert_many(docs)
print(f"Inserted {len(result.inserted_ids)} documents")