import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import pickle

data = pd.read_csv("dataset.csv")

le = LabelEncoder()
data["Level"] = le.fit_transform(data["Level"])

X = data[["Marks","StudyHours"]]
y = data["Level"]

model = DecisionTreeClassifier()
model.fit(X,y)

pickle.dump(model,open("model.pkl","wb"))
pickle.dump(le,open("level_encoder.pkl","wb"))

print("Model trained successfully")