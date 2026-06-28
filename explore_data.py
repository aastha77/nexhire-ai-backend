import pandas as pd
import json

def load_dataset(file_path):
    print("Loading 100K candidates dataset... ⏳")
    try:
        # File uncompressed hai, isliye sirf lines=True use karenge
        df = pd.read_json(file_path, lines=True)
        print(f"✅ Dataset loaded successfully! Total candidates: {len(df)}")
        
        # Let's inspect what fields we actually have to work with
        print("\n--- Columns Available ---")
        for col in df.columns.tolist():
            print(f"- {col}")
            
        print("\n--- Sample Record (First Candidate) ---")
        # Displaying the first record as a formatted JSON string to understand nested structures
        sample_record = json.loads(df.head(1).to_json(orient='records'))[0]
        print(json.dumps(sample_record, indent=2))
        
        return df
        
    except Exception as e:
        print(f"❌ Error loading dataset: {e}")
        return None

if __name__ == "__main__":
    # Updated file name without .gz
    df_candidates = load_dataset('data/candidates.jsonl')