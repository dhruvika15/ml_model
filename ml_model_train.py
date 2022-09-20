import pandas
dataset= pandas.read_csv('ml_model_training_data.csv')
x= dataset['YearsExperience']
y= dataset['Salary']
x= x.values
x= x.reshape(-1,1)

from sklearn.linear_model import LinearRegression
model= LinearRegression()
model.fit(x,y)

print('Changes Commited')
