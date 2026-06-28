import pandas as pd

def preprocess_candidates(file_path):
    print("Loading and preprocessing candidates for NexHire-AI... ⏳")
    
    # Load the raw dataset
    df = pd.read_json(file_path, lines=True)
    
    # --- 1. Flatten the Skills ---
    # Loop through the list of skill dictionaries and extract just the names into a single string
    df['flat_skills'] = df['skills'].apply(
        lambda x: " ".join([skill['name'] for skill in x]) if isinstance(x, list) else ""
    )
    
    # --- 2. Extract Key Heuristics for Fast Filtering ---
    # Extracting these directly into separate columns so we can filter them mathematically later
    df['years_experience'] = df['profile'].apply(lambda x: x.get('years_of_experience', 0))
    df['current_title'] = df['profile'].apply(lambda x: x.get('current_title', ''))
    df['location'] = df['profile'].apply(lambda x: x.get('location', ''))
    
    # Extracting notice period from redrob_signals (default to 90 if missing)
    df['notice_period'] = df['redrob_signals'].apply(lambda x: x.get('notice_period_days', 90) if isinstance(x, dict) else 90)
    
    # --- 3. Build the "Master Text" for Semantic AI ---
    # Combining summary, flattened skills, and the latest job description for the AI to "read"
    def build_master_text(row):
        summary = row['profile'].get('summary', '')
        skills = row['flat_skills']
        
        # Take description of only the last 2 jobs to save processing time
        history = " ".join([job.get('description', '') for job in row.get('career_history', [])[:2]])
        
        return f"{summary} {skills} {history}"
    
    df['master_text'] = df.apply(build_master_text, axis=1)
    
    print(f"✅ Preprocessing complete! Reduced complexity for {len(df)} candidates.")
    
    # Return only the columns we actually need for the engine to save memory
    clean_df = df[['candidate_id', 'current_title', 'years_experience', 'location', 'notice_period', 'master_text']]
    return clean_df

if __name__ == "__main__":
    # Test the preprocessor
    # File path format goes one folder up to root, then into data
    clean_data = preprocess_candidates('data/candidates.jsonl')
    
    print("\n--- NexHire-AI: Clean Data Preview ---")
    print(clean_data.head(2)) # Show first 2 records
    clean_data.to_csv('data/cleaned_candidates.csv', index=False)
    print("✅ Clean data saved to data/cleaned_candidates.csv")