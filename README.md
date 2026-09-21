# Cognevance Technologies — Student Performance Analysis

## Project Overview
This Level 1 project analyzes student academic performance using Python, pandas, NumPy, and Matplotlib. The analysis focuses on marks, attendance, study habits, assignments, and grade distribution.

## Objectives
- Clean and preprocess student data.
- Analyze academic performance and attendance.
- Visualize trends using charts.
- Examine the relationship between attendance and scores.
- Generate practical recommendations.

## Tools
- Python
- pandas
- NumPy
- Matplotlib
- Jupyter Notebook

## Dataset
The included sample dataset contains 200 student records with demographic, attendance, study, assignment, sleep, subject-score, overall-score, and grade fields.

## Workflow
1. Load the dataset.
2. Remove duplicate and missing records.
3. Calculate descriptive statistics and subject averages.
4. Analyze attendance and academic scores.
5. Create visualizations.
6. Summarize insights and recommendations.

## Key Result
The Pearson correlation between attendance and overall score in this dataset is **0.260**, indicating a positive relationship.

## Repository Structure
- `data/` — dataset
- `notebooks/` — Jupyter notebook
- `src/` — Python analysis script
- `visualizations/` — generated charts
- `report/` — project report
- `requirements.txt` — Python dependencies

## How to Run
```bash
pip install -r requirements.txt
cd src
python analysis.py
```

## Disclaimer
This is a synthetic educational dataset created for project practice and does not represent real student records.
