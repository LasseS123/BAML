import pandas as pd
import matplotlib.pyplot as plt

#H0.2 A
data = pd.read_csv('LaborSupply1988.csv')

#H0.2 B
data['age'].plot.hist(x='age', title='Age Distribution Histogram', xlabel='Age', ylabel='Frequency', bins=50)
plt.show()

#H0.2 C
datac = data.groupby('age')['kids'].mean()
datac.plot.line(title='Average Number of Kids by Age', xlabel='Age', ylabel='Average Number of Kids')
plt.show()

#H0.2 D
data.plot.scatter(x='age', y='lnhr', title='Scatter Plot of Age vs lnhr', xlabel='Age', ylabel='lnhr')
plt.show()

#H0.2 E
datad = data.groupby('age')['lnhr'].mean()
datad.plot.line(title='Average lnhr by Age', xlabel='Age', ylabel='Average lnhr')
plt.show()

datadd = data[['age', 'lnhr']]
print(datadd.corr().loc['lnhr', 'age'])

#H0.2 F
datafR = data[data['disab'] == 1]
datafNR = data[data['disab'] == 0]

ax = datafR.plot.scatter(x='age', y='lnhr', color = 'blue', label = 'Disabled', title='Scatter Plot of Age vs lnhr Colored by Disability', xlabel='Age', ylabel='lnhr')
datafNR.plot.scatter(x='age', y='lnhr', color = 'red', label = 'Not Disabled', ax=ax)
plt.show()

#H0.2 G
data.plot.box(column='lnhr', by='kids', title='Box Plot of lnhr by Number of Kids', xlabel='Number of Kids', ylabel='lnhr')
plt.show()