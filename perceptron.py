import pandas as pd
import numpy as np
import sys
import csv
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report




print(csv.field_size_limit())




df = pd.read_csv('train.txt', sep=' ', engine='python',quoting=csv.QUOTE_NONE ,error_bad_lines=False, nrows=50000)


print(df.head())

print(df.isnull().sum())
df = df.fillna(method='ffill')

print(df.groupby('Tag').size().reset_index(name='counts'))

X = df.drop('Tag', axis=1)
v = DictVectorizer(sparse=False)
X = v.fit_transform(X.to_dict('records'))
y = df.Tag.values
classes = np.unique(y)
del(df)

classes = classes.tolist()
#nbrtest=int(X.shape[0]*0.33)
#nbrtrain=X.shape[0]-nbrtest

#X_train=X[:nbrtrain]
#X=np.delete(X,range(nbrtrain), 0)
#X_test=X
#del(X)

#y_train=y[:nbrtrain]
#y=np.delete(y, range(nbrtrain))
#y_test=y
#del(y)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state=0)
#print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)

per = Perceptron(verbose=10, n_jobs=-1, max_iter=5)



per.partial_fit(X_train, y_train, classes)


new_classes = classes.copy()
print(new_classes.pop())
print(new_classes)
print(classification_report(y_pred=per.predict(X_test), y_true=y_test, labels=new_classes))

