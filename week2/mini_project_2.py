import pandas as pd
import numpy as np

data = {
    'id': [1, 2, 3, 4, 5],
    'product': ['Apple', 'Samsung', 'LG', 'Apple', 'Samsung'],
    'price': [1200, np.nan, 900, 1200, 1500],
    'store': ['Seoul', 'Busan', 'Seoul', None, 'Busan']
}


pd.DataFrame(data).to_csv('dirty_data.csv', index=False)
df = pd.read_csv('dirty_data.csv')

dict = {'price': df['price'].mean(), 'store':'Unknown'} # filtering
result_df = df.fillna(value=dict) # NULL Exception
final_df = result_df[result_df['price'] >= 1000]
final_df.to_parquet('cleaned_data.parquet', engine='pyarrow')
print("Parquet Saved!")
print("------------------------")
print(pd.read_parquet('cleaned_data.parquet'))


