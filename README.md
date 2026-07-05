# Netflix Data Analysis and Visualization

An end-to-end Netflix data analysis project built using Python. This project performs data cleaning, exploratory data analysis (EDA), and generates multiple professional visualizations to uncover trends and insights from the Netflix catalog.

## 📌 Project Overview

This project analyzes the popular Netflix Titles dataset to understand content distribution, genre popularity, rating patterns, and growth trends over the years. It follows a clean, structured data analytics workflow ideal for Data Analyst and Data Science roles.

## ✨ Visualizations Generated

The project automatically generates the following visualizations and saves them in the `outputs/` folder:

| File Name                          | Description                                      |
|------------------------------------|--------------------------------------------------|
| `01_movies_vs_tvshows.png`         | Distribution of Movies vs TV Shows on Netflix    |
| `02_content_added_per_year.png`    | Trend of content added to Netflix over the years |
| `03_top_genres.png`                | Top 10 most common genres on Netflix             |
| `04_top_countries.png`             | Top 10 countries producing content for Netflix   |
| `05_rating_distribution.png`       | Distribution of content ratings (TV-MA, TV-14, etc.) |
| `06_release_year_trend.png`        | Release year trend comparison between Movies and TV Shows |

## 📊 Dataset

- **Source**: [Netflix Movies and TV Shows Dataset](https://www.kaggle.com/datasets/shivamb/netflix-shows) (Kaggle)
- **File**: `netflix_titles.csv` (placed inside `data/` folder)
- Contains details like show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in (genres), and description.

## 🛠️ Technologies Used

- **Python 3**
- **Pandas** – Data loading, cleaning, and manipulation
- **Matplotlib** – Creating visualizations
- **Seaborn** – Statistical and aesthetic visualizations

## 📁 Project Structure
Netflix_Data_Visualization_Project/
├── data/
│   └── netflix_titles.csv                 # Netflix dataset
├── outputs/                               # Generated charts (PNG files)
│   ├── 01_movies_vs_tvshows.png
│   ├── 02_content_added_per_year.png
│   ├── 03_top_genres.png
│   ├── 04_top_countries.png
│   ├── 05_rating_distribution.png
│   └── 06_release_year_trend.png
├── venv/                                  # Virtual environment
├── netflix_analysis.py                    # Main analysis script
├── requirements.txt                       # Python dependencies
└── README.md


## 🚀 How to Run the Project

### Step 1: Setup Virtual Environment (Recommended)
```powershell
python -m venv venv
venv\Scripts\activate

### Step 1: Install Dependencies
pip install -r requirements.txt

Step 3: Add the Dataset

Download netflix_titles.csv from Kaggle
Place the file inside the data/ folder

Step 4: Run the Analysis
PowerShell
python netflix_analysis.py

📈 Key Insights

Netflix’s catalog is dominated by Movies compared to TV Shows.
There has been a significant increase in content addition after 2015.
International Movies, Dramas, and Comedies are among the most frequent genres.
The United States produces the highest number of titles available on Netflix.
Most content is rated TV-MA and TV-14.
Both Movies and TV Shows show consistent growth in release trends over the years.

💡 Why This Project is Useful

Demonstrates complete EDA workflow (Data Loading → Cleaning → Visualization)
Generates multiple meaningful visualizations
Clean and well-structured code
Suitable for portfolio and job applications (Data Analyst / Data Science roles)
Easy to understand and extend

👩‍💻 Author
Somarouthu Rajyalakshmi
B.Tech in Computer Science & Engineering (AIML)
Data Analytics | Python | Full Stack Development
