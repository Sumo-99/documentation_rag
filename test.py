from rag_server import *
import json

raw_query = "how to insert data into astradb with python"

data = {
    "input": {
        "query": raw_query
    }
}

print("Raw Query: ", raw_query)
response = get_relevant_docs(raw_query, "pydantinc_why_markdown", 5)
print(response)

# import os
# import google.generativeai as genai

# # Configure the Gemini API client
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # Define the embedding model
# EMBED_MODEL = "models/gemini-embedding-exp-03-07"

# def test_embedding_access():
#     try:
#         response = genai.embed_content(model=EMBED_MODEL, content="Test text for embedding.")
#         print("Successfully accessed the model.")
#         print("Embedding:", response["embedding"])
#         print("Embedding Length:", len(response["embedding"]))
#     except Exception as e:
#         print("Error accessing the model:", e)

# test_embedding_access()


