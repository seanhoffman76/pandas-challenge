import pandas as pd

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)
print(purchase_data.head())

# Store the basic calculations for Purchasing Analysis (Total) as individual variables
numunqitems = purchase_data['Item ID'].nunique()
numpurch = purchase_data['Purchase ID'].count()
totalrev = purchase_data['Price'].sum()
avgprice = totalrev/numpurch

total_purch_df = pd.DataFrame({
    'Number of Unique Items': [numunqitems],
    'Average Price': avgprice,
    'Number of Purchases': [numpurch],
    'Total Revenue': totalrev
})

total_purch_df['Average Price'] = total_purch_df['Average Price'].astype(float).map("${:,.2f}".format)
total_purch_df['Total Revenue'] = total_purch_df['Total Revenue'].astype(float).map("${:,.2f}".format)

print(total_purch_df)

heroes_gender = purchase_data.loc[:, ['SN', 'Gender']] 
# dropping ALL duplicate values 
heroes_gender.drop_duplicates(subset ='SN', 
                     keep = False, inplace = True) 
print(heroes_gender.groupby(['Gender']))