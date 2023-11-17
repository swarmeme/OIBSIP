#%%
import pandas as pd
import matplotlib.pyplot as plt
# %%
unemployment_df = pd.read_csv('/Users/swarnim/Desktop/Unemployment_Rate_upto_11_2020.csv')
# %%
unemployment_df
# %%
unemployment_df.rename(columns={'Region': 'State'}, inplace=True)
unemployment_df.rename(columns={'Region.1':'Direction'}, inplace=True)
# %%
unemployment_df.head()
# %%
unemployment_df.isnull().sum()
# %%
unemployment_df.info()
#%%
unemployment_df.columns
# %%
avg_unemployment_estimate = unemployment_df.groupby('State')[' Estimated Unemployment Rate (%)'].mean().reset_index()
# %%
avg_unemployment_estimate
#%%
avg_unemployment_estimate.set_index('State', inplace=True)

# %%
avg_unemployment_estimate.plot(kind='bar', figsize=(10, 8))
plt.ylabel('Unemployment Rate')
plt.xlabel('State')
plt.title('Average Estimated Unemployed by State')
plt.xticks(rotation=45, ha='right')

# %%
data = {
    'Region': ['North', 'South', 'East', 'West', 'Northeast'],
    ' Estimated Unemployment Rate (%)': [556.64, 1255.28, 416.11, 627.28, 411.95]
}
#%%
unemployment_region_df = pd.DataFrame(data)
#%%
region_colors = ['skyblue', 'lightcoral', 'lightgreen', 'lightpink', 'gold']
#%%
plt.figure(figsize=(8, 8))
plt.pie(unemployment_region_df[' Estimated Unemployment Rate (%)'], labels=unemployment_region_df['Region'], autopct='%1.1f%%', startangle=90, colors=region_colors)
plt.title('Distribution of Unemployed Individuals by Region')
plt.show()

# %%
