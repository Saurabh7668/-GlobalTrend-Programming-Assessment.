Question_4 = """
Using pandas, write a Python function to clean and preprocess a given DataFrame, which involves handling missing values, normalizing numerical columns, and encoding categorical columns.
"""
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

def clean_and_preprocess(df):
    # Separate features and target if the target column is provided (assuming last column is the target)
    if 'target' in df.columns:
        X = df.drop(columns=['target'])
        y = df['target']
    else:
        X = df
        y = None
    
    # Identify numerical and categorical columns
    num_cols = X.select_dtypes(include=['float64', 'int64']).columns
    cat_cols = X.select_dtypes(include=['object', 'category']).columns
    
    # Preprocessing for numerical data: impute missing values and normalize
    num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])
    
    # Preprocessing for categorical data: impute missing values and one-hot encode
    cat_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])
    
    # Combine numerical and categorical pipelines into a single ColumnTransformer
    preprocessor = ColumnTransformer([
        ('num', num_pipeline, num_cols),
        ('cat', cat_pipeline, cat_cols)
    ])
    
    # Fit and transform the data
    X_clean = preprocessor.fit_transform(X)
    
    # Convert the preprocessed data back into a DataFrame for easier inspection (optional)
    X_clean_df = pd.DataFrame(X_clean, columns=num_cols.tolist() + list(preprocessor.named_transformers_['cat']['onehot'].get_feature_names_out(cat_cols)))
    
    return (X_clean_df, y) if y is not None else X_clean_df

# Example usage:
# df = pd.read_csv('your_dataset.csv')
# cleaned_df, target = clean_and_preprocess(df)

