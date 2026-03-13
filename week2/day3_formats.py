import pandas as pd

df = pd.read_csv('practice_result.csv')
df = df.fillna('Unknown')

df = df.astype(str)

df.to_json('data.json', orient='records', force_ascii=False, indent=4)
print('JSON Saved!')

df.to_parquet('data.parquet', engine='pyarrow')
print('Parquet Saved!')