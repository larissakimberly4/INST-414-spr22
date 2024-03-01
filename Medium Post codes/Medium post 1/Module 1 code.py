import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Exploratory Data Analysis (EDA)

# Read the dataset into a DataFrame
students_exam_df = pd.read_csv(r"C:\Users\Musaga\Desktop\INST 414\INST-414-spr22\Medium Post codes\student_exam_data.csv")

# Display the first few rows of the DataFrame to verify the data has been loaded successfully
print(students_exam_df.head())

# Summary statistics for study hours and previous exam scores
print("Summary Statistics:")
print(students_exam_df[['Study Hours', 'Previous Exam Score']].describe())

# Scatter plot of study hours vs. exam scores with color-coded pass/fail groups
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Study Hours', y='Previous Exam Score', hue='Pass/Fail', data=students_exam_df, palette={0: 'red', 1: 'green'})
plt.title('Study Hours vs. Previous Exam Score')
plt.xlabel('Study Hours')
plt.ylabel('Previous Exam Score')
plt.legend(title='Pass/Fail', loc='upper right', labels=['Fail', 'Pass'])
plt.show()

# Histogram of study hours with color-coded pass/fail groups
plt.figure(figsize=(8, 6))
sns.histplot(students_exam_df[students_exam_df['Pass/Fail'] == 0]['Study Hours'], color='red', label='Fail', kde=True)
sns.histplot(students_exam_df[students_exam_df['Pass/Fail'] == 1]['Study Hours'], color='green', label='Pass', kde=True)
plt.title('Distribution of Study Hours by Pass/Fail')
plt.xlabel('Study Hours')
plt.ylabel('Frequency')
plt.legend()
plt.show()

# Data Cleaning

# Check for missing values
print("Missing Values:")
print(students_exam_df.isnull().sum())

# Impute missing values
students_exam_df['Study Hours'].fillna(students_exam_df['Study Hours'].mean(), inplace=True)

# Remove duplicate entries
students_exam_df.drop_duplicates(inplace=True)

# Insights and Visualizations

# Box plot comparing exam scores between pass and fail groups
sns.boxplot(x='Pass/Fail', y='Previous Exam Score', data=students_exam_df)
plt.title('Previous Exam Score by Pass/Fail')
plt.xlabel('Pass/Fail')
plt.ylabel('Previous Exam Score')
plt.show()

