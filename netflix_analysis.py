import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs('data', exist_ok=True)
os.makedirs('outputs', exist_ok=True)

print("🚀 Netflix Data Visualization Started...")

try:
    df = pd.read_csv('data/netflix_titles.csv')
except FileNotFoundError:
    print("❌ data/netflix_titles.csv not found! Download from Kaggle and place it in data/ folder.")
    exit()

print(f"✅ Dataset loaded: {df.shape[0]} rows")

# Cleaning
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['year_added'] = df['date_added'].dt.year
df = df.dropna(subset=['type', 'release_year'])
df['genres'] = df['listed_in'].str.split(', ')
df_genres = df.explode('genres')

sns.set_style("whitegrid")

# 1. Movies vs TV Shows
plt.figure(figsize=(8,6))
type_counts = df['type'].value_counts()
plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', colors=['#E50914','#141414'])
plt.title('Movies vs TV Shows on Netflix')
plt.savefig('outputs/01_movies_vs_tvshows.png', dpi=300, bbox_inches='tight')
plt.close()

# 2. Content Added Per Year
plt.figure(figsize=(10,6))
yearly = df['year_added'].value_counts().sort_index()
sns.lineplot(x=yearly.index, y=yearly.values, marker='o', color='#E50914')
plt.title('Content Added to Netflix Over Years')
plt.savefig('outputs/02_content_added_per_year.png', dpi=300, bbox_inches='tight')
plt.close()

# 3. Top 10 Genres
plt.figure(figsize=(10,6))
top_genres = df_genres['genres'].value_counts().head(10)
sns.barplot(y=top_genres.index, x=top_genres.values, palette='Reds_r')
plt.title('Top 10 Genres on Netflix')
plt.savefig('outputs/03_top_genres.png', dpi=300, bbox_inches='tight')
plt.close()

# 4. Top 10 Countries
plt.figure(figsize=(10,6))
top_countries = df['country'].value_counts().head(10)
sns.barplot(y=top_countries.index, x=top_countries.values, palette='Reds')
plt.title('Top 10 Countries')
plt.savefig('outputs/04_top_countries.png', dpi=300, bbox_inches='tight')
plt.close()

# 5. Rating Distribution
plt.figure(figsize=(10,6))
rating_counts = df['rating'].value_counts().head(10)
sns.barplot(y=rating_counts.index, x=rating_counts.values, palette='Reds_r')
plt.title('Rating Distribution')
plt.savefig('outputs/05_rating_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

print("\n✅ All charts saved in 'outputs/' folder! Open them to see results.")