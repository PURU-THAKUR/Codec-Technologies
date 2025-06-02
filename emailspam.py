import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample dataset (expand this later for better accuracy)
data = {
    'text': [
        'Win a free iPhone now!',
        'Meeting schedule for tomorrow',
        'Congratulations, you have won a lottery!',
        'Important update about your account',
        'Limited time offer, buy now!',
        'Team project deadline extended',
        'You are selected for a prize',
        'Family dinner this weekend'
    ],
    'label': ['spam', 'ham', 'spam', 'ham', 'spam', 'ham', 'spam', 'ham']
}

df = pd.DataFrame(data)

# Convert text to numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['text'])

# Labels (spam = 1, ham = 0)
y = df['label'].map({'ham': 0, 'spam': 1})

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print(f"\n✅ Model trained! Accuracy on sample data: {accuracy_score(y_test, y_pred) * 100:.2f}%\n")

# Continuous loop for input
print("📨 Email Spam Checker (type 'exit' to quit)")

while True:
    new_email = input("\nEnter email text: ").strip()
    if new_email.lower() == 'exit':
        print("👋 Exiting Spam Checker. Goodbye!")
        break
    if new_email == '':
        print("⚠️ Please enter some text.")
        continue

    email_vector = vectorizer.transform([new_email])
    prediction = model.predict(email_vector)
    result = "🚨 Spam" if prediction[0] == 1 else "✅ Not Spam"
    print(f"Result: {result}")
