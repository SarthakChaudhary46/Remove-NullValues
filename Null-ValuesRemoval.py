import numpy as nm  
import matplotlib.pyplot as plt
import pandas as pd  
from sklearn import datasets
import csv

dataset = pd.read_csv(r"train.csv")

csvreader = csv.reader(dataset)

headings = list(dataset.columns)
print("headings- ",headings)

df = pd.DataFrame(dataset,columns= ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'])
df[df.columns[df.isnull().any()]]

#replace null value with mean

dataset["Age"].fillna(dataset["Age"].mean(), inplace = True)


E1 = dataset['Embarked'].tolist()
duplicates = [number for number in E1 if E1.count(number) > 1]
unique_duplicates = list(set(duplicates))

first = unique_duplicates.pop(1)
print(first)

dataset["Embarked"].fillna("Q", inplace = True)


Cabin1 = dataset['Cabin'].tolist()
duplicates = [number for number in Cabin1 if Cabin1.count(number) > 1]
unique_duplicates = list(set(duplicates))

first = unique_duplicates.pop(0)
print(first)

dataset["Cabin"].fillna("D17", inplace = True)

df = pd.DataFrame(dataset,columns= ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'])
df[df.columns[df.isnull().any()]]