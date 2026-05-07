# Study-Resource-Recommender
A Machine Learning-based web application that recommends personalized study resources based on subject, marks, study hours, and learning level. Built using Flask, Scikit-learn, Pandas, and NumPy with Decision Tree classification for learning level prediction and resource recommendation.
## Features

* Personalized study resource recommendations
* Machine Learning-based learning level prediction
* YouTube tutorial suggestions
* Subject-wise book recommendations
* Beginner, Intermediate, and Advanced level classification
* Simple and user-friendly web interface
* Real-time recommendation generation

---

## Technologies Used

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* Flask

### Machine Learning & Data Processing

* Scikit-learn
* Pandas
* NumPy
* Pickle

---

## Project Structure

```bash
STUDY-RESOURCE-RECOMMENDER/
│
├── templates/
│   └── index.html
│
├── app.py
├── train_model.py
├── visualize.py
├── dataset.csv
├── model.pkl
├── level_encoder.pkl
├── le_level.pkl
├── le_resource.pkl
├── requirements.txt
└── .venv/
```

---

## Application Flow

1. User enters subject, marks, study hours, topic, and preferred learning method.
2. Flask backend receives user input through the web interface.
3. The trained Machine Learning model predicts the student’s learning level.
4. System analyzes the prediction and selects suitable study resources.
5. Recommended YouTube tutorials or books are displayed to the user instantly.

---

## Future Improvements

* Add more subjects and larger datasets
* Integrate advanced ML algorithms for better accuracy
* Include personalized learning analytics
* Add user authentication and progress tracking
* Recommend courses from online learning platforms
* Deploy the application on cloud platforms for public access
