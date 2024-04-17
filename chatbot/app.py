from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session
import pandas as pd
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Load data from CSV
data = pd.read_csv('data.csv', header=None)
inputs = data[0].tolist()
labels = data[1].tolist()

vectorizer = CountVectorizer()
model = LogisticRegression()
X = vectorizer.fit_transform(inputs)
model.fit(X, labels)

# Define a route for the home page
@app.route('/')
def home():
    session.clear()
    return render_template('index.html')

@app.route('/clear-session')
def clear_session():
    session.clear()
    return redirect(url_for('home'))

# Define a route to handle form submission
@app.route('/chat', methods=['POST'])
def chat():
    if 'conversation' not in session:
        session['conversation'] = []

    user_input = request.form['message']
    transformed_input = vectorizer.transform([user_input])
    prediction = model.predict(transformed_input)[0]
    responses = {
        0: ["Hello! How can I help you today?", "Hi there! What can I do for you?", "Good day! What are you looking for?"],
        1: ["Goodbye! Have a great day!", "See you later! Take care!", "Bye! Come back soon!"]
    }
    response = random.choice(responses[prediction])

    # Save the user input and bot response to the conversation
    session['conversation'].append(("user", user_input))
    session['conversation'].append(("bot", response))
    session.modified = True 

    # Calculate the total number of messages
    message_count = len(session['conversation']) // 2

    # Render the same page with the conversation updated
    return render_template('index.html', conversation=session['conversation'], message_count=message_count)

if __name__ == '__main__':
    app.run(debug=True)
