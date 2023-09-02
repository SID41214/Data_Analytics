from pandas import read_csv
from sklearn.model_selection import train_test_split

from sklearn.svm import SVC

fileName = "Energy Meter.csv"
names = ['Voltage', 'Current', 'Power', 'class']
dataset = read_csv(fileName, names=names)

array = dataset.values
X = array[:,0:3]
y = array[:,3]

X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.50, random_state=1)

model = SVC(gamma='auto')

model.fit(X_train, Y_train)

import pickle
filename = 'finalized_model.pkl'
pickle.dump(model, open(filename, 'wb'))

loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_validation, Y_validation)
print(result)

value = [[212.7315,0.84753,180.2963282]]
predictions = loaded_model.predict(value)
print(predictions[0])





