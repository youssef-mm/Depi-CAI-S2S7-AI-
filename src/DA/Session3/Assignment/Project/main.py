from config.config import DATA_PATH, COLS_TO_DROP
from preprocessing import (
    read_data_file,
    drop_unnecessary_features,
    check_data_type
)

def run_pipeline():
    print("=" * 50)
    print("🚀 Starting Data Preprocessing Pipeline...")
    print("=" * 50)

    # 1. Read the Dataset
    try:
        df = read_data_file(DATA_PATH)
        print(f" Dataset loaded successfully! Shape: {df.shape}\n")
    except Exception as e:
        print(e)
        return

    # 2. Inspect Dataset Before Cleaning
    print("--- 1. Initial Data Inspection Report ---")
    initial_report = check_data_type(df)
    print(initial_report)
    print("\n" + "-" * 50)

    # 3. Drop Unnecessary Features
    print(f"--- 2. Removing Configured Columns: {COLS_TO_DROP} ---")
    df_cleaned = drop_unnecessary_features(df, COLS_TO_DROP)
    print(f"Columns remaining: {list(df_cleaned.columns)}")
    print(f"New Shape: {df_cleaned.shape}\n")
    print("-" * 50)

    # 4. Final Data Inspection Report
    print("--- 3. Cleaned Data Inspection Report ---")
    cleaned_report = check_data_type(df_cleaned)
    print(cleaned_report)
    print("=" * 50)
    print(" Pipeline completed successfully!")

if __name__ == "__main__":
    run_pipeline()