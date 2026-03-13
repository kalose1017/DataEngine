import pandas as pd
import numpy as np

df = pd.read_csv('practice_result.csv')

print("--- Data Head(2 Line) ---")
print(df.head(2))

senior_users = df[df['Age'] >= 25]

print("\n--- Over 25 Age User List ---")
print(senior_users)

name_city = df[['Name', 'City']]
print("\n--- Only Name and City ---")
print(name_city)


#new_data = {'Name': ['Error_User'], 'Age': [np.nan], 'Job': ['Unknown'], 'City': [None]}
#df = pd.concat([df, pd.DataFrame(new_data)], ignore_index=True)

print("--- result ---")
df = df.fillna('Unknown')
print(df)
print("--- INFO ---")
print(df.info())
#df.to_csv('practice_result.csv', index=False)