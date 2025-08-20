from textblob import TextBlob

class TextClassifier:
    def __init__(self):
        # Sample dataset (not used for training, but for demonstration)
        self.dataset = [
            "I love this product!",
            "The movie was terrible and boring.",
            "It's just okay, nothing special.",
            "What a fantastic experience!",
            "I'm not happy with the service.",
            "The food was delicious and fresh.",
            "I hate waiting in long lines.",
            "The book was interesting and informative.",
            "It was the worst day of my life.",
            "The staff were polite and helpful.",
            "I don't know how to feel about it.",
            "Everything was perfect!",
            "The app crashes all the time.",
            "I feel great today!",
            "The package arrived late.",
            "Customer support was amazing.",
            "This makes no sense.",
            "Not bad, not great either.",
            "The quality is outstanding.",
            "I would never recommend this."
        ]

    # Function to classify the sentiment of a single sentence
    def classify_sentiment(self, text):
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity

        if polarity > 0.1:
            return "Positive 😊"
        elif polarity < -0.1:
            return "Negative 😠"
        else:
            return "Neutral 😐"

    # Function to display sentiment labels for the dataset
    def show_dataset_analysis(self):
        print("📦 Sample Dataset Sentiment Labels:\n")
        for sentence in self.dataset:
            sentiment = self.classify_sentiment(sentence)
            print(f"\"{sentence}\" → Sentiment: {sentiment}")

    # Function to interact with the user for input classification
    def user_input_loop(self):
        print("\n💬 Enter a sentence to classify its sentiment (type 'exit' to quit):")
        while True:
            user_input = input("🧠 You: ")

            if user_input.lower() == "exit":
                print("👋 Exiting the sentiment classifier. Goodbye!")
                break

            result = self.classify_sentiment(user_input)
            print(f"📊 Sentiment: {result}")
if __name__ == "__main__":
    classifier = TextClassifier()
    classifier.show_dataset_analysis()
    classifier.user_input_loop()
