import numpy as np
import pandas as pd
pd.set_option("display.max_columns", None)

countries_url = "https://dqlab.id/data/country_details.json"
df_countries = pd.read_json(countries_url)
print(df_countries.head())