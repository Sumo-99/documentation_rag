# 📄 documentation_rag — Claude MCP Server for RAG Over Technical Docs

This is a lightweight MCP server built using the [FastMCP](https://modelcontextprotocol.io) framework to enable retrieval-augmented generation (RAG) over internal technical documentation.

It uses:
- **OpenAI's embedding model** (`text-embedding-3-large`) for vector generation
- **Astra DB** for vector storage and retrieval
- **Claude Desktop** as the MCP client

---

## 🚀 Features

- 🔍 Query indexed documentation using semantic search
- 📦 Built for Claude Desktop MCP interface
- 🧠 FastMCP-powered tool declaration
- 🛠️ Fully environment-configurable

---

## ⚙️ Setup Instructions

### 1. Clone the Repo and Install Dependencies

Make sure you have [`uv`](https://github.com/astral-sh/uv) installed:

```bash
brew install astral-sh/uv/uv  # or use curl installer
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

Clone [my fork](https://github.com/Sumo-99/UNS-MCP/tree/uns_hack_documentation_rag) of UNS-MCP to make firecrawl generate markdown: 

### 2. Create a `.env` File

Here are the environment variables you need to set up:

```env
# OpenAI
OPENAI_API_KEY=sk-...

# Astra DB
ASTRA_DB_ID=your-uuid-here
ASTRA_DB_REGION=your-region
ASTRA_DB_APPLICATION_TOKEN=your-token
ASTRA_DB_API_ENDPOINT=https://your-app-id-your-region.apps.astra.datastax.com
ASTRA_DB_KEYSPACE=your-keyspace
```

You must have already indexed your documents into Astra DB using Unstructured or another pipeline.

---

## ▶️ Run the MCP Server

```bash
uv run your_script_name.py
```

Or to test a single request:

```bash
echo '{"method":"get_relevant_docs","params":{"query":"How does logging work?", "collection_name": "my_docs"}}' | uv run your_script_name.py
```

---

## 🧠 Claude Desktop Integration

To use this tool from Claude Desktop, open your `config.json` and add the following entry:

```json
"documentation_rag": {
  "command": "/Users/yourname/.local/bin/uv",
  "args": ["run", "your_script_name.py"],
  "cwd": "/Users/yourname/path/to/project/documentation_rag",
  "disabled": false
}
```

Be sure to replace:
- `your_script_name.py` with your actual file name
- `cwd` with the full path to the project directory

---

## 🧪 Usage Example in Claude

Try typing this into Claude Desktop:

> Use the documentation_rag tool to answer: “How can I redact sensitive fields using logwise?”

Claude will:
- Embed the query
- Perform semantic search in Astra DB
- Return top relevant documents for context-aware answering

---

## 🧱 Built With

- [FastMCP](https://github.com/mcprotocol/fastmcp)
- [AstraPy](https://github.com/datastax/astra-db-python)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Claude Desktop](https://modelcontextprotocol.io/tools/claude-desktop)
- [Unstructured APIs](https://docs.unstructured.io/open-source/introduction/overview)

---

## 👥 Maintainer

- Sumanth Ramesh

Feel free to fork and extend this with additional tools or new source connectors!
