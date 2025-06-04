import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

df = pd.read_json("data.json")

# Parsing dates
df['date_added'] = pd.to_datetime(df['date_added'])
print(df['date_added'])

# Clean duration
def clean_duration(row):
    if "Season" in row:
        return int(row.split()[0]), "seasons"
    elif "min" in row:
        return int(row.split()[0]), "minutes"
    else:
        return None, None

df[['duration_clean', 'duration_type']] = df['duration'].apply(
    lambda x: pd.Series(clean_duration(x))
)
print(df['duration_type'])

# Pie chart to show most common genres
genres = df['listed_in'].str.split(', ').explode()
genres.value_counts().plot(kind='pie', autopct='%1.1f%%', figsize=(8, 8), title='Genre Distribution')
plt.ylabel('')
plt.show()

# Bar chart: Top 5 directors by content count
top_directors = df['director'].value_counts()
plt.bar(top_directors.index, top_directors.values, color="skyblue")
plt.xlabel("Directors")
plt.ylabel("Content Count")
plt.title("Directors Series/movies count", fontweight="bold")
plt.tight_layout()
plt.show()