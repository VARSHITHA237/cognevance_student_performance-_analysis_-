import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/student_performance.csv")

# Basic cleaning
df = df.drop_duplicates()
df = df.dropna()

subjects = ["Mathematics","Science","English","History","Computer Science"]

# Summary statistics
print(df.describe())

# Subject averages
subject_means = df[subjects].mean().sort_values(ascending=False)
print("\nSubject averages:\n", subject_means)

# Attendance vs score correlation
correlation = df["Attendance_Percentage"].corr(df["Overall_Score"])
print(f"\nAttendance/score correlation: {correlation:.3f}")

# Visualizations
plt.figure(figsize=(8,5))
plt.hist(df["Overall_Score"], bins=12)
plt.title("Distribution of Overall Scores")
plt.xlabel("Overall Score")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("../visualizations/marks_distribution.png", dpi=150)
plt.close()

plt.figure(figsize=(8,5))
plt.hist(df["Attendance_Percentage"], bins=10)
plt.title("Attendance Distribution")
plt.xlabel("Attendance (%)")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("../visualizations/attendance_distribution.png", dpi=150)
plt.close()

plt.figure(figsize=(9,5))
plt.bar(subject_means.index, subject_means.values)
plt.title("Average Performance by Subject")
plt.ylabel("Average Score")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("../visualizations/subject_performance.png", dpi=150)
plt.close()

plt.figure(figsize=(7,5))
df["Grade"].value_counts().sort_index().plot(kind="pie", autopct="%1.1f%%")
plt.title("Grade Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("../visualizations/grade_distribution.png", dpi=150)
plt.close()

plt.figure(figsize=(8,5))
plt.scatter(df["Attendance_Percentage"], df["Overall_Score"], alpha=0.6)
plt.title("Attendance vs Overall Score")
plt.xlabel("Attendance (%)")
plt.ylabel("Overall Score")
plt.tight_layout()
plt.savefig("../visualizations/attendance_vs_score.png", dpi=150)
plt.close()
