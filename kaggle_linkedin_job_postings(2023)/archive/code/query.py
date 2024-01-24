import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import sqlite3 

csv_linkedin_job_postings = r'C:\Users\Vulcan\OneDrive - Madison College\dataSetExplore\kaggle_linkedin_job_posting(2023)\archive\job_postings.csv'
df = pd.read_csv(csv_linkedin_job_postings)

print(df.columns)

# Creates a clustered bar graph displaying hte top 10 most posted job titles.

top_titles = df['title'].value_counts().nlargest(15)

plt.figure(figsize=(12, 6))
top_titles.plot(kind='bar', color='royalblue')
plt.title('Top 15 Most Posted Job Titles on LinkedIN')
plt.xlabel('Job Title')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.show()

# End clustered bar graph.