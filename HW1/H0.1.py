import pandas as pd
#H0.1 A
data = pd.read_csv('LaborSupply1988.csv')

#H0.1 B
print(data.shape)
print(data)

#H0.1 C
print(data.columns)

#H0.1 D
print(data.loc[0:9])

#H0.1 E
print("min-Age: " + str(data['age'].min()))    
print("max-Age: " + str(data['age'].max()))

#H0.1 F
print(data.groupby('kids')['lnhr'].mean())

#H0.1 G
print("Average number of kids of 40 yr olds: " + str(data.groupby(data['age'] == 40).mean()['kids'].loc[True]))