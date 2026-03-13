import pandas as pd

data = {
    'Name': ['Kalose', 'Mentor', 'Junior'],
    'Age': [25, 35, 20],
    'Job': ['Student', 'Senior DE', 'Begineer'],
    'City': ['Seoul', 'Busan', 'Incheon']
}

df = pd.DataFrame(data)

print("--- Generated Data Frame ---")
print(df)
print("\n--- Data Information ---")
print(df.info())

df.to_csv('practice_result.csv', index=False)
print('\nCSV File Saved!')