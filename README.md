# Android vs iOS Market Share Analysis

This project explores global mobile operating system usage, focusing on Android vs iOS adoption by country. Using data from early 2025, the analysis reveals where each platform dominates and includes visualizations like bar charts, direct country comparisons, and interactive choropleth maps.

## Data Source

This dataset was pulled from [StatCounter Global Stats](https://gs.statcounter.com/) and reflects mobile OS market share across the world from **February to April 2025**.

> StatCounter provides monthly aggregated market share data across operating systems, browsers, and platforms. To access map-level breakdowns, the date range must be limited to 3 months or less — hence the Feb–Apr 2025 window used in this project.

Data was downloaded in CSV format via the "Map" view export tool for **Mobile Operating System → Worldwide → Monthly**.

## What This Includes

-  Cleaned and remapped territory-level data to countries
-  Bar charts of top 10 Android/iOS countries
-  Deep dive: Android vs iOS in the U.S.
-  Country comparison charts (U.S. vs Australia, Canada, India, Germany, etc.)
-  Interactive maps showing global OS distribution

##  Files

- `analysis.py` – full Python script for data cleaning, analysis, and visualizations
- `data/` – contains the input CSV file (Feb–Apr 2025)
- `requirements.txt` – minimal package list to recreate the environment
- `README.md` – project overview and setup instructions

## Setup

Clone the repo and install the required packages:

```bash
git clone https://github.com/yourusername/android_vs_ios_analysis.git
cd android_vs_ios_analysis
pip install -r requirements.txt
python analysis.py

## Example Outputs

- Market OS Market Shared in the United States
- Global iOS Market Share by Country (%)
- Global Android Market Share by Country (%)

￼<img width="636" alt="Pasted Graphic 1" src="https://github.com/user-attachments/assets/f06d253b-ccf1-40f4-afff-e194e26b87ed" />
<img width="1453" alt="Pasted Graphic 2" src="https://github.com/user-attachments/assets/4f1362bf-fc88-44ec-8fed-6d8625b41c11" />
<img width="1414" alt="Pasted Graphic 3" src="https://github.com/user-attachments/assets/b91cb134-f276-42b6-a958-6ba65d6f3b10" />


## Tools Used
- pandas for data processing
- matplotlib + seaborn for static visualizations
- plotly for interactive choropleth maps

## Created By
Ashley Cortez — [GitHub Profile](https://github.com/ashleyncortez)

