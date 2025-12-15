from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training data (tiny but works!)
texts = [
    "I love this class",
    "This is amazing",
    "I feel great today",
    "I hate this",
    "This is terrible",
    "I feel bad"
]

labels = ["positive", "positive", "positive", "negative", "negative", "negative"]

# Convert text → numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Train the AI model
model = MultinomialNB()
model.fit(X, labels)

# Ask the AI to predict
while True:
    user_input = input("\nType a sentence: ")
    if user_input.lower() == "quit":
        break

    X_test = vectorizer.transform([user_input])
    prediction = model.predict(X_test)[0]

    print("AI thinks this is:", prediction)