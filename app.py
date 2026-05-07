from flask import Flask, render_template, request
import pickle
import urllib.parse

app = Flask(__name__)

# Load ML model
model = pickle.load(open("model.pkl", "rb"))
encoder = pickle.load(open("level_encoder.pkl", "rb"))

# Book recommendations
books = {
    "Machine Learning":[
        ("Tom Mitchell - Machine Learning","Pages 45-80"),
        ("Ethem Alpaydin - Introduction to ML","Pages 120-160"),
        ("Christopher Bishop - Pattern Recognition","Pages 210-250")
    ],
    "DBMS":[
        ("Korth - Database System Concepts","Pages 150-190"),
        ("Elmasri & Navathe - Fundamentals of DBMS","Pages 220-260"),
        ("Ramakrishnan - Database Management Systems","Pages 300-340")
    ],
    "Operating Systems":[
        ("Galvin - Operating System Concepts","Pages 100-140"),
        ("Tanenbaum - Modern Operating Systems","Pages 200-240"),
        ("William Stallings - Operating Systems","Pages 180-220")
    ]
}

def suggest_resource(level):
    if level == "Beginner":
        return "YouTube"
    elif level == "Intermediate":
        return "YouTube + Books"
    else:
        return "Books"


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/recommend', methods=["POST"])
def recommend():

    subject = request.form["subject"]
    marks = int(request.form["marks"])
    study = int(request.form["study_hours"])
    topic = request.form["topic"]
    method = request.form["method"]

    prediction = model.predict([[marks,study]])
    level = encoder.inverse_transform(prediction)[0]

    ml_suggestion = suggest_resource(level)

    youtube_link = None
    book_list = None

    if method == "YouTube":
        query = urllib.parse.quote(topic + " " + subject + " tutorial")
        youtube_link = f"https://www.youtube.com/results?search_query={query}"

    elif method == "Books":
        book_list = books.get(subject, [])

    return render_template(
        "index.html",
        subject=subject,
        marks=marks,
        study=study,
        topic=topic,
        method=method,
        level=level,
        ml_suggestion=ml_suggestion,
        youtube_link=youtube_link,
        books=book_list
    )


if __name__ == "__main__":
    app.run(debug=True)