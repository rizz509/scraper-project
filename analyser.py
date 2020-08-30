import csv
import pandas as pd
def analyse():
    with open('iteminfo.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        j = 0
        filename = "sorted.csv"
        f = open(filename, "w")
        headers = "Item_name,Item_seller,Ad_date,Item_price\n"
        f.write(headers)
        for row in reader:
            name = row['Item_name']
            seller = row['Item_seller']
            date = row['Ad_date']
            raw_price = row['Item_price']
            price = raw_price.replace("|", "").replace("Rs. ", "").replace("(Used)SOLD OUT", "").replace(
                "(Like New)SOLD OUT", "").replace("(Brand New)SOLD OUT", "")
            f.write(name + "," + seller + "," + date + "," + price + "\n")
    f.close()
    csvfile.close()
    df = pd.read_csv('sorted.csv')
    df = df.sort_values('Item_price')
    df.to_csv('sorted.csv',index=False)


