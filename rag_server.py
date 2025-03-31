import os
from typing import Any
from dotenv import load_dotenv
import google.generativeai as genai
from astrapy import DataAPIClient
from mcp.server.fastmcp import FastMCP
from openai import OpenAI

# Load environment variables
load_dotenv()

OPENAI_CLIENT = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
EMBEDDING_MODEL = "text-embedding-3-large"
GENERATION_MODEL = "gpt-4o-2024-11-20"

# Setup Astra DB
astra_client = DataAPIClient(os.getenv("ASTRA_DB_APPLICATION_TOKEN"))
database = astra_client.get_database(os.getenv("ASTRA_DB_API_ENDPOINT"))

# Initialize FastMCP server
mcp = FastMCP("documentation_rag")

def get_embedding(text: str):
    """
    Generate embedding for given text using OpenAI's embedding model.
    Args:
    text (str): Input text to embed
    Returns:
    Embedding vector for the input text
    """
    return OPENAI_CLIENT.embeddings.create(
    input=text, model=EMBEDDING_MODEL
    ).data[0].embedding

@mcp.tool()
def get_relevant_docs(query: str, collection_name: str, n: int = 5) -> str:
    """Fetch documentation information for queries regarding any software documentation.

    Args:
        query: The user's search query
        collection_name: The name of the collection to search in
        n: Number of documents to retrieve
    """
    if not collection_name:
        return "Please provide a collection name."
    
    embedding = get_embedding(query)
    collection = database.get_collection(
        name=collection_name,
        keyspace=os.getenv("ASTRA_DB_KEYSPACE")
    )
    results = collection.find(sort={"$vector": embedding}, limit=n)
    
    docs = [doc.get("content", "[No content]") for doc in results]

    if not docs:
        return "No relevant documents found."

    return "\n".join(
        [f"\n\n===== Document {i+1} =====\n{doc}" for i, doc in enumerate(docs)]
    )


if __name__ == "__main__":
    mcp.run(transport="stdio")
