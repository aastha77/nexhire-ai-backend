import pandas as pd
from engine.embedder import SemanticRanker

def get_final_rankings(df, jd_text):
    # 1. Faster Rule-Based Scoring (The 'Sieve' Layer)
    def quick_score(row):
        score = 0
        text = str(row['master_text']).lower()
        # JD ke main keywords jo 'Senior AI Engineer' role ke liye zaruri hain
        if 'python' in text: score += 1
        if 'ai' in text or 'ml' in text: score += 1
        if 'rank' in text or 'retrieval' in text: score += 1
        if 'embedding' in text: score += 1
        return score

    print("Filtering candidates with Fast Keyword Sieve...")
    df['pre_score'] = df.apply(quick_score, axis=1)
    
    # 2. Only pick top 1000 candidates based on quick keywords
    # Yeh step 77,000 se 1,000 par le aayega (Super Fast!)
    df_top_1000 = df.sort_values(by='pre_score', ascending=False).head(1000).copy()
    print(f"✅ Filtered down to top 1000 potential matches.")

    # 3. Only run expensive AI on these 1000
    ranker = SemanticRanker()
    scores, indices = ranker.rank_candidates(jd_text, df_top_1000['master_text'].tolist())
    
    df_top_1000['ai_score'] = scores
    return df_top_1000.sort_values(by='ai_score', ascending=False).head(100)

if __name__ == "__main__":
    # Load your preprocessed data from the root folder
    df = pd.read_csv('data/cleaned_candidates.csv')
    
    jd = "Senior AI Engineer with production experience in embeddings, retrieval, ranking systems, vector databases, and Python."
    
    print("🚀 Starting Ranking Pipeline...")
    final_list = get_final_rankings(df, jd)
    
    # Ensure 'output' folder exists
    import os
    if not os.path.exists('output'): os.makedirs('output')
    
    final_list.to_csv('output/ranked_candidates.csv', index=False)
    print("🏆 Top 100 Candidates saved to output/ranked_candidates.csv")