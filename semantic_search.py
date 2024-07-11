from sentence_transformers import SentenceTransformer, util

# Initialize the sentence transformer model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Function to perform semantic search
def semantic_search(corpus, query):
    corpus_embeddings = model.encode(corpus, convert_to_tensor=True)
    query_embedding = model.encode(query, convert_to_tensor=True)
    hits = util.semantic_search(query_embedding, corpus_embeddings)
    return hits

# Test the semantic search function
if __name__ == "__main__":
    corpus = [
        "The weather is nice today.",
        "How is the weather tomorrow?",
        "It will rain today.",
        "Sunny weather expected tomorrow."
    ]
    query = "What is the weather like?"
    hits = semantic_search(corpus, query)
    print(f"Search Results: {hits}")
