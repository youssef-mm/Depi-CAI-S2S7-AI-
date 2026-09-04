import pandas as pd

def drop_cols(df: pd.DataFrame, cols_to_drop: list) -> pd.DataFrame:
    """Drops specified columns from dataframe."""
    return df.drop(columns=cols_to_drop, errors="ignore")

def fill_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Handles missing values in Age and Embarked."""
    median_age = df["Age"].median()
    df["Age"] = df["Age"].fillna(median_age)
    
    df = df.dropna(subset=["Embarked"])
    
    if "Cabin" in df.columns:
        df = df.drop(columns=["Cabin"])
        
    return df

def convert_dtypes(df: pd.DataFrame, cat_cols: list) -> pd.DataFrame:
    """Converts selected categorical columns to category dtype."""
    existing_cat_cols = [col for col in cat_cols if col in df.columns]
    df[existing_cat_cols] = df[existing_cat_cols].astype("category")
    return df