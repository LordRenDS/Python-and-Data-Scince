import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_path = r"C:\Users\serge\Documents\Study\Практика\CVS\OSMI 2019 Mental Health in Tech Survey Results - OSMI " \
            r"Mental Health in Tech Survey 2019.csv"
raw_data = pd.read_csv(data_path)
print(raw_data)
# select columns for our needs and rename it for easier access
needed_cols = raw_data.iloc[:, [0, 1, 2, 3, 19, 20, 27, 45, 46, 48, 75, 76, 77]]
new_columns = ['self_employed', 'company_size', 'company_is_tech', 'is_tech_role',
               'physical_importance', 'mental_importance', 'productivity_affected',
               'physical_importance_was', 'mental_importance_was', 'diagnosed', 'age',
               'gender', 'country']

needed_cols.columns = new_columns
print(needed_cols)
# some preparation the data
# choosing the people who work in the company
df = needed_cols[~needed_cols.self_employed].reset_index()
# change 'More than 1000' in company size for a shorter name
df['company_size'].replace(to_replace=['More than 1000'], value='1000+', inplace=True)
# edit long countries names for visualizations
df['country'].replace(to_replace=['United States of America'], value='USA', inplace=True)
df['country'].replace(to_replace=['United Kingdom'], value='UK', inplace=True)
# restrict age 18+
df = df[df.age >= 18]
# edit gender column
df.gender.replace(to_replace=['Male', 'male', 'm', 'M', 'Identify as male', 'Male ', 'Make', 'Man'], value='M',
                  inplace=True)
df.gender.replace(to_replace=['female', 'Female', 'F', 'f', 'Woman', 'femmina', 'Female ', 'Femile'], value='F',
                  inplace=True)
df.gender.replace(to_replace=[np.nan, 'Let\'s keep it simple and say "male"', 'Non-binary', 'Non binary', 'Masculine',
                              'Cishet male', 'None', 'Nonbinary', 'agender', 'Questioning', 'Cis Male', 'cis woman',
                              'Agender trans woman', '43', 'Trans man', 'masculino', 'Trans non-binary/genderfluid',
                              'CIS Male', 'Non-binary and gender fluid', 'Female (cis)'], value='Other', inplace=True)
# set colors for visualization
colors = ('orchid', 'cornflowerblue', 'mediumpurple', 'slateblue', 'hotpink', 'lightsteelblue')
print(df)
# 1.   What is an age distribution among respondent working in tech companies?
is_tech = df[df.company_is_tech]
age_col = is_tech.age
age_col.plot.hist(title='Age distribution in tech companies', grid=True, xlabel='Emploee age', ylabel='Count')
# 2.   What is a distribution of respondents among countries?
countries_df = df[['country', 'company_is_tech']]
grouped_df = countries_df.groupby('country').count()
grouped_df.sort_values('company_is_tech', ascending=False)
pop_countries = list(grouped_df[grouped_df.company_is_tech >= 12].sort_values('company_is_tech', ascending=False).index)
pop_countries_df = countries_df[countries_df.country.isin(pop_countries)]
sns.countplot(x=pop_countries_df['country'], hue=pop_countries_df['company_is_tech'],
              palette=colors).set(title='Distribution of respondents among countries')
# 3.   What are the sizes of companies among respondents?
comp_size_df = df[['company_is_tech', 'company_size']]
sns.countplot(x=comp_size_df['company_size'], hue=comp_size_df['company_is_tech'],
              palette=colors).set(title='Sizes of companies')
# 4.   What is proportion of women working in tech companies among respondents?
gender_df = df[['company_is_tech', 'gender']]
tech_gender_df = gender_df[gender_df.company_is_tech]
grouped_gender_count_df = tech_gender_df.groupby('gender').count()
grouped_gender_count_df.plot.pie(subplots=True, autopct='%1.1f%%', explode=(0.1, 0, 0), startangle=90,
                                 title='Proportion of women working', colors=colors)
# 5.   What is the difference in proportion of holding tech positions by gender?
gender_tech_pos_df = df[['gender', 'is_tech_role']]
gender_tech_pos_df = gender_tech_pos_df[gender_tech_pos_df.is_tech_role]
grouped_gender_tech_role_df = gender_tech_pos_df.groupby('gender').count()
grouped_gender_tech_role_df.plot.pie(subplots=True, autopct='%1.1f%%', startangle=90,
                                     title='Proportion of holding tech positions by gender', colors=colors)
# 6.   Do companies put more attention to physical or mental health?
health_df = df[['physical_importance', 'mental_importance',
                'physical_importance_was', 'mental_importance_was']]
physical_mean = round(health_df.physical_importance.mean(), 1)
mental_mean = round(health_df.mental_importance.mean(), 1)
physical_was_mean = round(health_df.physical_importance_was.mean(), 1)
mental_was_mean = round(health_df.mental_importance_was.mean(), 1)
health = health_df.describe().loc['mean'].round(1)
# making figure
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].pie([health.physical_importance, health.mental_importance], labels=['Physical health', 'Mental health'],
          autopct='%1.1f%%', colors=colors)
ax[1].pie([health.physical_importance_was, health.mental_importance_was],
          labels=['Physical health was', 'Mental health was'],
          autopct='%1.1f%%', colors=colors)
fig.suptitle('Companies put more attention to physical or mental health')
ax[0].set_title('Present')
ax[1].set_title('Past')
plt.show()
# 7.   How many respondents think that their work is affected by mental issues?
sns.heatmap(data=df.isna())
# 8.   What social group is the most at risk to be diagnosed with mental issues?
diagnosed_df = df[df.diagnosed == 'Yes']
# Most common age
diagnose_ages = diagnosed_df.groupby('age').country.count()
diagnose_ages.plot.bar(title='Most common age', ylabel='count', figsize=(10, 5))
# Most common country
diagnosed_country = diagnosed_df.groupby('country').age.count().sort_values(ascending=False)
diagnosed_country.plot.bar(title='Most common country', ylabel='count', figsize=(14, 5), rot=0)
# Most common gender
diagnosed_gender = diagnosed_df.groupby('gender').age.count().sort_values(ascending=False)
diagnosed_gender.plot.pie(subplots=True, autopct='%1.1f%%', startangle=90, title='Most common gender', colors=colors)
# Most common company
diagnosed_comp = diagnosed_df.groupby('company_size').age.count().sort_values(ascending=False)
diagnosed_comp.plot.pie(colors=colors, autopct='%1.1f%%', startangle=90, figsize=(6, 6))
sizes = df.company_size.value_counts()
comparison_df = pd.concat([sizes, diagnosed_comp], axis=1)
comparison_df['probability'] = (comparison_df['age'] / comparison_df['company_size']) * 100
comparison_df = comparison_df.sort_values('probability', ascending=False)
print(comparison_df)
