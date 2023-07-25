

import pandas as pd

customer = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack'],
    'Age': [25, 30, 35, 40, 22, 28, 33, 26, 29, 31],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Boston', 'Seattle', 'Denver', 'Atlanta', 'Miami', 'Dallas'],
    'Country': ['USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA']
}

orders = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hannah', 'Ivy'],
    'Product Name': ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'TV', 'Camera', 'Smartwatch', 'Speaker', 'Gaming Console'],
    'Price': [1200, 800, 500, 100, 1500, 600, 300, 200, 400]
}

customer=pd.DataFrame(customer)
orders=pd.DataFrame(orders)
print(customer.head())
print(orders.head())

def tolist(customer):
  customer['customerdata']= customer[['City','Country']].to_dict(orient='records')
  customer.drop(['City','Country'],axis=1,inplace=True)
  customer.rename(columns={'customerdata':'customerdata'} , inplace= True)
  return customer



def toorder(orders):
  orders['transact']=orders[['Product Name','Price']].to_dict(orient='records')

  orders.drop(['Product Name','Price'],axis=1,inplace=True)
  orders.rename(columns={'transacts':'transacts'},inplace=True)
  return orders


result=customer.groupby(['Name','Age'],group_keys=False).apply(tolist)
result2=orders.groupby('Name',group_keys=False).apply(toorder)

print(result)
print(result2)

combined=pd.merge(result,result2,on='Name')

print(combined[combined['Name'] == 'Alice'])