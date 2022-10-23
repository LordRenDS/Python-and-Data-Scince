import pandas as pd
import matplotlib.pyplot as plt

data_path = r"C:\Users\serge\Documents\Study\Практика\CVS\OSMI 2019 Mental Health in Tech Survey Results - OSMI " \
            r"Mental Health in Tech Survey 2019.csv"
mental_health_2019 = pd.read_csv(data_path)
print(mental_health_2019)
# 1.   What is an age distribution among respondent working in tech companies?
tech_emp = mental_health_2019[mental_health_2019['Is your employer primarily a tech company/organization?'] == True]
result = tech_emp['What is your age?'].value_counts()
result.plot.bar(title='Age', figsize=(10, 5), xlabel='Emploee age', ylabel='Count')
# plt.show()
# 2.   What is a distribution of respondents among countries?
country = mental_health_2019['What country do you *live* in?'].value_counts()
country.plot.bar(title='Distribution of respondents among countries', figsize=(10, 10), xlabel='Country',
                 ylabel='Count')
# plt.show()
# 3.   What are the sizes of companies among respondents?
result = mental_health_2019['How many employees does your company or organization have?'].value_counts()
result.plot.pie(title='Number of employees', figsize=(11, 11), autopct='%1.1f%%')
# plt.show()
# 4.   What is proportion of women working in tech companies among respondents?
gen_edited = mental_health_2019.copy()
print(gen_edited)
man = ['Male', 'male', 'M', 'm', 'Man', 'man']
women = ['Female', 'female', 'F', 'f', 'Women', 'woman']


def sort_gen(row):
    if row['What is your gender?'] in man:
        return 'Man'
    elif row['What is your gender?'] in women:
        return 'Woman'
    else:
        return 'Other'


gen_edited['What is your gender?'] = gen_edited.apply(sort_gen, axis=1)
data = gen_edited['What is your gender?'].value_counts()
data.plot.pie(title='Proportion of women working', figsize=(10, 10), autopct='%1.1f%%', explode=(0, 0.1, 0),
              startangle=90)
# plt.show()
# 5.   What is the difference in proportion of holding tech positions by gender?
data = gen_edited['What is your gender?'].value_counts()
data.plot.pie(title='Difference in proportion of holding tech positions by gender', figsize=(10, 10),
              autopct='%1.1f%%')
# plt.show()
# 6.   Do companies put more attention to physical or mental health?
health = mental_health_2019.loc[:, ['Overall, how much importance did your previous employer place on physical health?',
                                    'Overall, how much importance did your previous employer place on mental health?',
                                    'Overall, how much importance does your employer place on physical health?',
                                    'Overall, how much importance does your employer place on mental health?']].mean(
    axis=0)
phys_h = health.loc[['Overall, how much importance did your previous employer place on physical health?',
                     'Overall, how much importance does your employer place on physical health?']].mean()
mental_h = health.loc[['Overall, how much importance did your previous employer place on mental health?',
                       'Overall, how much importance does your employer place on mental health?']].mean()
fig, ax = plt.subplots(figsize=(6, 6))
ax.pie([mental_h, phys_h], labels=['Mental health', 'Physical health'], autopct='%1.1f%%')
ax.set_title('Companies put more attention to physical or mental health')
ax.axis('equal')
# plt.show()
# 7.   How many respondents think that their work is affected by mental issues?
mental_affected = mental_health_2019['Do you believe your productivity is ever affected by a mental health issue?'].value_counts()
mental_affected.plot.pie(title='The number of respondents, who think that their work is affected by mental issues',
                         figsize=(10, 10), autopct='%1.1f%%', explode=(0.1, 0, 0, 0), startangle=90)
# plt.show()
# 8.   What social group is the most at risk to be diagnosed with mental issues?
diagnosted = mental_health_2019[mental_health_2019['Have you ever been *diagnosed* with a mental health disorder?'] == 'Yes']
diagnosted_gen = gen_edited[gen_edited['Have you ever been *diagnosed* with a mental health disorder?'] == 'Yes']
race_group = diagnosted['What is your race?'].value_counts()
age_group = diagnosted['What is your age?'].value_counts()
gen_group = diagnosted_gen['What is your gender?'].value_counts()
