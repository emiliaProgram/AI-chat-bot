### Application Summary:

The application is a web-based chatbot that interacts with users through a simple and modern interface. When a user submits a message, the chatbot processes it and provides an appropriate response based on pre-defined categories. The user's interface is built using HTML and styled with CSS for a modern, abstract look, complete with an input field for user messages and a dynamically updating display for both the conversation history and the count of messages exchanged.

#### Key Features:

- **Message Handling**: Users can type messages into a text field and submit them to the chatbot.
- **Session Management**: Each user's conversation is tracked using Flask's session management, ensuring individual interactions remain isolated and persistent during the session.
- **Dynamic Updates**: The conversation thread and the count of messages are updated in real-time as the interaction progresses.
- **Clear on Refresh**: When the page is refreshed, the session is cleared to reset the conversation, providing a fresh start for the user.

### Machine Learning Model Explanation:

The backbone of the chatbot's understanding capability is a machine learning model built with `scikit-learn`, a powerful library for machine learning in Python.

#### Vectorization:
- **CountVectorizer**: This converts the text data into a numerical format that machine learning algorithms can process. It creates vectors of word counts to represent the text, forming the feature set for the model.

#### Model Training:
- **Logistic Regression**: A classification algorithm used to predict the category of a user's message. It distinguishes between different types of messages, such as greetings or farewells, based on the features created by the vectorizer.

#### Workflow:
1. **Data Preparation**: The model is trained on a dataset consisting of sample text messages labeled according to their intended categories (e.g., greeting, farewell).
2. **Training**: The Logistic Regression model learns from this dataset, understanding how different words and phrases correlate with the categories.
3. **Prediction**: When a user inputs a message, the model predicts its category based on what it has learned.
4. **Response Generation**: Based on the predicted category, the chatbot selects an appropriate response from a predefined list of responses.

#### Start application
Run `python app.py`

https://github.com/emiliaProgram/AI-chat-bot/assets/146941756/b1b20bc6-7c4e-4a0d-854d-062c5b1f6b01

#### Next step
Increase the data input
