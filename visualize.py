import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score

# Load dataset
data = pd.read_csv("dataset.csv")

# -----------------------------
# 1️⃣ Scatter Plot
# -----------------------------

plt.figure()

plt.scatter(data["StudyHours"], data["Marks"])

plt.title("Marks vs Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.show()


# -----------------------------
# 2️⃣ Learning Level Distribution
# -----------------------------

plt.figure()

data["Level"].value_counts().plot(kind="bar")

plt.title("Distribution of Learning Levels")
plt.xlabel("Learning Level")
plt.ylabel("Number of Students")

plt.show()


# -----------------------------
# 3️⃣ Encode Labels
# -----------------------------

le = LabelEncoder()

data["Level"] = le.fit_transform(data["Level"])

# Features
X = data[["Marks", "StudyHours"]]

# Target
y = data["Level"]


# -----------------------------
# 4️⃣ Train Decision Tree Model
# -----------------------------

model = DecisionTreeClassifier()

model.fit(X, y)


# -----------------------------
# 5️⃣ Decision Tree Visualization
# -----------------------------

plt.figure(figsize=(10,6))

plot_tree(
    model,
    feature_names=["Marks","StudyHours"],
    class_names=le.classes_,
    filled=True
)

plt.title("Decision Tree Model")

plt.show()


# -----------------------------
# 6️⃣ Predictions
# -----------------------------

y_pred = model.predict(X)


# -----------------------------
# 7️⃣ Confusion Matrix
# -----------------------------

cm = confusion_matrix(y, y_pred)

plt.figure()

sns.heatmap(cm, annot=True, cmap="Blues")

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.show()


# -----------------------------
# 8️⃣ Model Accuracy
# -----------------------------

accuracy = accuracy_score(y, y_pred)

print("Model Accuracy:", accuracy)