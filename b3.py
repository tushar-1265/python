import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


result_data=pd.read_csv('results.csv')
print("Top 10 rows of dataset")
print(result_data.head(10))

subjects=result_data.columns[1:6]

pass_fail_count={'Overall':{'Pass':0,'Fail':0}}

for subject in subjects:
    pass_fail_count[subject]={'Pass':result_data[result_data[subject]>=40][subject].count(),
                              'Fail':result_data[result_data[subject]<40][subject].count()}

    pass_fail_count['Overall']['Pass']+= pass_fail_count[subject]['Pass']
    pass_fail_count['Overall']['Fail']+= pass_fail_count[subject]['Fail']

print('\nPass/Fail counts')

print(pd.DataFrame(pass_fail_count))

sns.scatterplot(x='Maths',y='Science',hue='Results',data=result_data)
plt.title("Scatter plot of subject1 vs subject2")
plt.show()


pass_fail_df=pd.DataFrame(pass_fail_count).T
pass_fail_df.plot(kind='bar',stacked=True)
plt.title("Subject wise pass/fail counts")
plt.xlabel('Subject')
plt.ylabel('count')
plt.show()


pass_fail_overall=pd.DataFrame(pass_fail_count['Overall'],index=['Overall'])
pass_fail_overall.plot(kind='bar',stacked=True)
plt.title("Overall pass/fail counts")
plt.xlabel('Overall')
plt.ylabel('count')
plt.show()


plt.hist(result_data['Total'],bins=20,color='skyblue',edgecolor='black')
plt.title('Histogram of Total Marks')
plt.xlabel('Total Marks')
plt.ylabel('Frequency')
plt.show()

    
    