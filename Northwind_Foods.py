import mysql.connector
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cnx = mysql.connector.connect(user='root', password='Wrongcider65',
                              host='localhost',
                              database='northwind')

cur = cnx.cursor()

cur.execute("""
            select * from orders;
""") 

data = cur.fetchall()

db = pd.DataFrame(data)
db.columns = ["OrderID", "CustomerID", "EmployeeID", "OrderDate", "RequiredDate", "ShippedDate", "ShipVia", "Freight", "ShipName", "ShipAddress", "ShipCity", "ShipRegion", "ShipPostalCode", "ShipCountry"]

countries = []
sales = []

for _, country_data in db.groupby("ShipCountry"):
    #print(country_data.shape)
    countries.append(np.unique(country_data["ShipCountry"])[0][:5])
    sales.append(country_data.shape[0])

plt.bar(np.array(countries),np.array(sales), color = "#6000FF")
plt.show()

year = []
for entry in db["OrderDate"]:
    year.append(np.datetime64(entry, 'Y'))

years = np.datetime_as_string(np.unique_counts(year)[0])
sales = np.unique_counts(year)[1]

plt.bar(years, sales, color = "#6000FF")
plt.show()

ship_via = []
for entry in db["ShipVia"]:
    ship_via.append(entry)

ship_method = np.unique_counts(ship_via)[0]
sales = np.unique_counts(ship_via)[1]

plt.bar(ship_method, sales, color = "#6000FF")
plt.show()