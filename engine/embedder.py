from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class SemanticRanker:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        print(f"Loading AI Model: {model_name}... 🧠")
        # Initialize the lightweight NLP model
        self.model = SentenceTransformer(model_name)
        
    def generate_embeddings(self, texts):
        print(f"Generating embeddings for {len(texts)} candidates...")
        # batch_size=128 karein taaki CPU ka poora fayda utha sakein
        return self.model.encode(texts, convert_to_numpy=True, show_progress_bar=True, batch_size=128)
        
    def rank_candidates(self, jd_text, candidate_texts):
        print("Converting Job Description and Candidates to Vectors... ⚡")
        # 1. Embed the Job Description (Query)
        jd_vector = self.model.encode([jd_text], convert_to_numpy=True)
        
        # 2. Embed the Candidate Profiles (Database)
        candidate_vectors = self.generate_embeddings(candidate_texts)
        
        print("Building FAISS Index for Lightning-Fast Search... 🔍")
        # 3. Create FAISS index
        dimension = candidate_vectors.shape[1]
        index = faiss.IndexFlatIP(dimension) # IP = Inner Product
        
        # Normalize vectors to calculate Cosine Similarity
        faiss.normalize_L2(jd_vector)
        faiss.normalize_L2(candidate_vectors)
        
        # Add candidate vectors to the index and search for the best matches
        index.add(candidate_vectors)
        
        # search() returns the distances (scores) and the indices (positions) of the top candidates
        k = len(candidate_texts) # Get rankings for all provided candidates
        distances, indices = index.search(jd_vector, k)
        
        return distances[0], indices[0]

if __name__ == "__main__":
    # A quick mock test to see if the engine works
    ranker = SemanticRanker()
    
    sample_jd = "Looking for a Backend Engineer with Python, API design, and SQL experience."
    sample_candidates = [
        "Frontend developer skilled in HTML, CSS, and React.js",
        "Backend professional with 5 years experience in Python, Django, and PostgreSQL", # Expected Winner
        "Data Scientist working with Machine Learning and deep neural networks"
    ]
    
    scores, positions = ranker.rank_candidates(sample_jd, sample_candidates)
    
    print("\n--- AI Ranking Results ---")
    for rank, (score, pos) in enumerate(zip(scores, positions)):
        print(f"Rank {rank+1} (Score: {score:.4f}): {sample_candidates[pos]}")