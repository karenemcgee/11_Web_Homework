import pandas as pd

csvfile = "cities.csv"
cities_df = pd.read_csv(csvfile)
cities_df.head()