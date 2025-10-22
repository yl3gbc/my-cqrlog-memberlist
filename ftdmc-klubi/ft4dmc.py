import pandas as pd
import requests


# Fetch the data from the URL
url = "https://epc-mc.de/FT4DMC.php"
response = requests.get(url)
data = response.content.decode('utf-8-sig')

# Split the data by lines and then by semicolons
lines = data.strip().split("\n")
data_list = [line.split(";") for line in lines]

# Create a DataFrame from the list
df = pd.DataFrame(data_list, columns=['num', 'id'])
df = df[["id", "num"]]
print(df)
# Save DataFrame to CSV
df.to_csv('ft4dmc.txt', index=False, sep=';', encoding='utf-8')