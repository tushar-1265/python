import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips_data=pd.read_csv('tips.csv')
print("Top 10 rows of data")
print(tips_data.head(10))

sns.scatterplot(x='day',y='tip',data=tips_data)
plt.title("Scatter plot of day vs tip")
plt.show()

sns.lineplot(x='day',y='tip',data=tips_data,ci=None)
plt.title("Line plot of day vs tip")
plt.show()

sns.barplot(x='day',y='tip',data=tips_data,ci=None)
plt.title("Bar plot of day vs tip")
plt.show()

plt.hist(tips_data['total_bill'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Total Bills')
plt.xlabel("total_bill")
plt.ylabel("Frequency")
plt.show()
