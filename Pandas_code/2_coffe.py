import pandas as pd
import numpy as np


coffe = pd.read_csv('../warmup-data/coffee.csv')
result = pd.read_parquet('../data/results.parquet')
olympic_data = pd.read_excel('../data/olympics-data.xlsx', sheet_name='results')
bios = pd.read_csv('../data/bios.csv')
noc_data = pd.read_csv('../data/noc_regions.csv')

#Todo:  Fetch any values based on rows & columns: loc[#Rows index, #Columns name]

# res= coffe.loc[0]   # Fetch 0 index row
# res= coffe.loc[[0,1,5]]     # Fetch 0, 1, 5 index row
# res= coffe.loc[0:3]     # Fetch 0, 1, 2 index row
# res= coffe.loc[[0,1,2], 'Day']      # Fetch 0, 1, 2 index row & Day column
# res= coffe.loc[[0,1,2], ['Day', 'Units Sold']]      # Fetch 0, 1, 2 index row & Day, Unit sold column
# res= coffe.loc[3:9, ['Day', 'Units Sold']]



#Todo: Fetch any values based on rows & columns: iloc[#Rows index, #Columns index]
# iloc is only used for default index, If we change the index then iloc won't return the DF

# res = coffe.iloc[[0,1,2]]   # Fetch 0, 1, 2 index row & all columns
# res = coffe.iloc[[0,1,2], [0,2]]    # Fetch 0, 1, 2 index row & 1, 3 columns
# res = coffe.iloc[0:5, [0,2]]


#Todo:  If we change the index value then only loc will work & iloc won't work
coffe.index = coffe['Day']
res = coffe.loc['Monday':'Tuesday', ['Day', 'Unit Solds']]      # This will work
res = coffe.iloc['Monday':'Tuesday', [0,1]]  # This won't work

#Todo: Update any columns based on row index
coffe.loc[1, 'Unit Sold'] = 10

#Todo: at[] & iat[] , It will return a single cell value
res = coffe.at[0, 'Day']    # It will fetch cell value of row 0 & column 'Day'
res = coffe.iat[0, 0]   # IT will fetch cell value of row 0 & column 0

#Todo: Sort Values
coffe.sort_values(["Units Sold", "Coffee Type"], ascending=[False, True])

# Todo: Iterate over the rows
for index, row in coffe.iterrows():
    print(index)
    print(row)
    print('\n')

# Todo: Filtering the data
res = bios.loc[bios['height_cm'] > 215, ['name', 'height_cm']]
res = bios[bios['height_cm'] > 215][['name', 'height_cm']]
res = bios[(bios['height_cm'] > 215) & (bios['born_country'] == 'USA')][['name', 'height_cm']]

# Todo: String operations
res = bios[bios['name'].str.contains('Keith|Patrick', case=False, na=False)]
res = bios[(bios['born_country'].isin(['USA','GBR','FRA'])) & (bios['name'].str.startswith('Keith'))]
res = bios.query(' born_county=="USA" and born_city=="Seattle" ')

# Todo: Add / Remove column
coffe['price'] = 4.9
coffe['new_price'] = np.where(coffe['Coffe Type'] == 'Espresso', 3.9, 5.9)

coffe.drop(0, inplace=True)     # Drop 0 index row, & inplace is used for save changes in same DF copy
coffe.drop(columns=['price'], inplace=True)     # Drop entire column & inplace is used for save changes in same DF copy

# Todo: Copy with different Pointer
coffe_new = coffe.copy()

# Todo : Rename column
coffe.rename(columns={'new_price':'price'}, inplace=True)

# Todo: Split columns
bios_new = bios.copy()
bios_new['first_name'] = bios['name'].str.split(' ').str[0]
res = bios_new.query(' first_name == "Keith" ')

# Todo : datatime

bios_new['born_datetime'] = pd.to_datetime(bios_new['born_date'], format='%Y-%m-%d')
bios_new['born_year'] = bios_new['born_datetime'].dt.year
print(bios_new[['first_name', 'born_year']].head())
bios_new.to_csv('output.csv', index=False)

# Todo: apply

bios['height_category'] = bios['height_cm'].apply(lambda x : 'Short' if x < 165 else ('Avg' if x < 185 else 'Tall'))

def category_select(row):
    if row['height_cm'] < 175 and row['weight_kg'] < 70:
        category = 'LeightWeight'
    if row['height_cm'] < 175 and row['weight_kg'] < 70:
        category = 'MiddleWeight'
    else:
        category = 'HeavyWeight'

    return category

bios['category'] = bios.apply(category_select, axis=1)

# Todo: Merge & Concat data

bios_region = pd.merge(bios, noc_data, left_on='born_country', right_on='NOC', how='left')
bios_region.rename(columns={'region': 'born_country_full'}, inplace=True)

usa = bios_region[bios_region['born_country'] == 'usa'].copy()
gbr = bios_region[bios_region['born_country'] == 'gbr'].copy()
new_df = pd.concat([usa, gbr])

# Todo: notna

coffe.loc[[2,3], 'Units Sold'] = np.nan
coffe.loc[[0,1], 'Units Sold'] = 15
coffe['Units Sold'] = coffe['Units Sold'].interpolate()
coffe['Units Sold'] = coffe.fillna(coffe['Units Sold'].mean())
print(coffe['Units Sold'].isna())
print(coffe['Units Sold'].notna())

coffe.dropna(subset=['Units Sold'], inplace=True)

# Todo: Values_count

res = bios['born_country'].values_count()

res = bios[bios['born_country']=='USA']['born_region'].values_count()

res =coffe.groupby(['Coffe Type', 'Day'])['Units Sold'].sum()

res = bios.groupby(['Coffe Type']).agg({'Units Sold': 'sum', 'price': 'mean'})


# Todo : pivot

coffe['revenue'] = coffe['price'] * coffe['Units Sold']
pivot = coffe.pivot(index='Day', columns='Coffe Type', values='revenue')

# Todo shift : Shift is used to compare the data
coffe['yesterday_revenue'] = coffe['revenue'].shift(2)

# Todo Rank : To give rank based on columns
bios['height_rank'] = bios['height_cm'].rank(ascending=False)
bios.sort_values(['height_rank'])

# Todo rolling : Get 3 days sum data
latte = coffe[coffe['Coffe Type']=='Latte']['Units Sold'].rolling(3).sum()



print(res)


