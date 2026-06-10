import pandas as pd

# Load dataset
df = pd.read_csv("../datasets/spam.csv", encoding='latin-1')

# Show first 5 rows
print(df.head())

# Dataset info
print(df.info())

# Check missing values
print(df.isnull().sum())

# Count spam and ham
print(df['label'].value_counts())